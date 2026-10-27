"""Script for Step B: draw the human-verification sample (50 of the 193 scenarios, excluding the earlier 25).

run: uv run python -m src.scripts.pick_50_random_scenarios_proportionally

- Seed: SEED = 42, the seed of the earlier 25-scenario round, reused for consistency .

- Same approach as the earlier 25 (stratified by paper, pandas sample with random_state=42),
 
-Reproducible: running this again gives the same 50 rows, cell for cell, because
    - the inputs are fixed and in git: the merged sheet (INPUT_PATH) and the earlier 25
      (EXCLUDE_PATH); same inputs -> same sample
    - the allocation uses only counts (ties broken by paper_id), no randomness
    - the only random step is pandas sample(random_state=SEED), i.e. numpy's legacy RandomState,
      whose output for a given seed is kept stable across numpy versions
    - rows are sorted by (paper_id, scenario number) first, so re-ordering the rows of the
      input sheet cannot change the sample
    - the sampled paper_id + scenario_id are saved in the output, and the seed, method, input
      files, counts and Python / pandas versions in its protocol sheet

scenarios each paper has left (proportional stratified sample):
    pool        all scenarios in the merged judgements sheet (one row per paper_id + scenario_id)
    excluded    the 25 scenarios of the earlier human coding round (read from their file)
    allocation  every paper with scenarios left gets 1, the rest of the 50 by largest remainder
                of 50 * remaining / total remaining (ties: paper_id), capped at what is left
    draw        per paper: its rows sorted by scenario number, then sub.sample(n=k, random_state=SEED)
"""

import os
import platform
import re
from datetime import datetime

import pandas as pd

# --- Set these (paths relative to the repo root) ---
INPUT_PATH = "output/07_task_2c_llm_judgements_merged.xlsx"
SHEET_NAME = "judgements"
EXCLUDE_PATH = "materials/25_random_picked_scenario_to_label_FILTERED.xlsx"   # earlier 25
OUTPUT_PATH = "output/50_random_scenarios_proportionally.xlsx"

SEED = 42            # same as the earlier 25; for consistency and reproducibility
N_SAMPLE = 50

MODELS = ["kimi_2.5", "glm_5.3", "deepseek_v4.1"]
COMPONENTS = [
    "threat_source", "objective_or_harmful_outcome", "capability", "knowledge",
    "access", "constraints_or_enabling_conditions", "target_or_asset_at_risk",
]
TAGS = {"Clear", "Ambiguous", "Not specified"}
PRESENT = {"Clear", "Ambiguous"}
MIN_PRESENT = 2      # verify a component when at least this many models flagged it present


def scenario_number(scenario_id: str) -> int:
    """'S12' -> 12, so S2 sorts before S10."""
    match = re.fullmatch(r"S(\d+)", scenario_id)
    if not match:
        raise ValueError(f"Unexpected scenario_id {scenario_id!r} (expected S<number>)")
    return int(match.group(1))


def check_keys(df: pd.DataFrame, name: str) -> None:
    """Stop on empty or duplicate (paper_id, scenario_id)."""
    if (df["paper_id"] == "").any() or (df["scenario_id"] == "").any():
        raise ValueError(f"{name}: a row has an empty paper_id or scenario_id")
    dupes = df[df.duplicated(["paper_id", "scenario_id"], keep=False)]
    if len(dupes):
        raise ValueError(f"{name}: duplicate scenarios\n{dupes[['paper_id', 'scenario_id']]}")


def allocate(left: pd.Series, n: int) -> pd.Series:
    """Spread n over the papers in proportion to the scenarios each has left: at least 1 per
    paper, never more than it has left, the rest by largest remainder (ties: paper_id)."""
    left = left[left > 0].sort_index()
    if n < len(left) or n > left.sum():
        raise ValueError(f"Cannot draw {n} from {len(left)} papers with {left.sum()} scenarios left")
    quota = n * left / left.sum()
    alloc = quota.astype(int).clip(lower=1, upper=left)
    while alloc.sum() < n:                    # give the next one to the largest remainder
        open_ = alloc < left
        gap = (quota - alloc)[open_]
        alloc[gap.sort_values(ascending=False, kind="stable").index[0]] += 1
    while alloc.sum() > n:                    # only if the minimum of 1 pushed us over
        over = (alloc - quota)[alloc > 1]
        alloc[over.sort_values(ascending=False, kind="stable").index[0]] -= 1
    return alloc


def draw_sample(eligible: pd.DataFrame, alloc: pd.Series, seed: int) -> pd.DataFrame:
    """Per paper, k rows with sub.sample(n=k, random_state=seed); rows in a fixed order."""
    parts = []
    for paper, k in alloc.items():
        sub = eligible[eligible["paper_id"] == paper]
        parts.append(sub.sample(n=int(k), random_state=seed))
    return sort_rows(pd.concat(parts))


def sort_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Rows by paper_id, then scenario number."""
    order = df.assign(_n=df["scenario_id"].map(scenario_number))
    return order.sort_values(["paper_id", "_n"], kind="stable").drop(columns="_n").reset_index(drop=True)


def component_rows(sample: pd.DataFrame) -> pd.DataFrame:
    """One row per sampled scenario x component: the three tags and Verify / Skip."""
    rows = []
    for _, r in sample.iterrows():
        for comp in COMPONENTS:
            tags = {m: r[f"{comp}_uncertainty_{m}"] for m in MODELS}
            bad = {m: t for m, t in tags.items() if t not in TAGS}
            if bad:
                raise ValueError(f"{r['paper_id']}_{r['scenario_id']} {comp}: unexpected tags {bad}")
            n_present = sum(t in PRESENT for t in tags.values())
            rows.append({"paper_id": r["paper_id"], "scenario_id": r["scenario_id"], "component": comp,
                         **{f"uncertainty_{m}": t for m, t in tags.items()},
                         "n_present": n_present,
                         "action": "Verify" if n_present >= MIN_PRESENT else "Skip"})
    return pd.DataFrame(rows)


def main() -> None:
    df = pd.read_excel(INPUT_PATH, sheet_name=SHEET_NAME, dtype=str, keep_default_na=False)
    ex = pd.read_excel(EXCLUDE_PATH, dtype=str, keep_default_na=False)
    for d in (df, ex):
        d["paper_id"], d["scenario_id"] = d["paper_id"].str.strip(), d["scenario_id"].str.strip()
    check_keys(df, INPUT_PATH)
    check_keys(ex, EXCLUDE_PATH)

    key = ["paper_id", "scenario_id"]
    excluded = ex[key].merge(df[key], how="left", on=key, indicator=True)
    missing = excluded[excluded["_merge"] == "left_only"]
    if len(missing):
        raise ValueError(f"Excluded scenarios not found in {INPUT_PATH}:\n{missing[key]}")
    is_excluded = df.set_index(key).index.isin(ex.set_index(key).index)
    eligible = sort_rows(df[~is_excluded])

    total = df["paper_id"].value_counts()
    n_excluded = df.loc[is_excluded, "paper_id"].value_counts()
    left = eligible["paper_id"].value_counts()
    alloc = allocate(left, N_SAMPLE)
    sample = draw_sample(eligible, alloc, SEED)
    comps = component_rows(sample)

    allocation = pd.DataFrame({"total": total, "excluded": n_excluded, "left": left,
                               "sampled": alloc}).fillna(0).astype(int).sort_index()
    allocation.index.name = "paper_id"
    allocation = allocation.reset_index()
    allocation.loc[len(allocation)] = ["All papers", *allocation.iloc[:, 1:].sum()]

    protocol = pd.DataFrame([
        ("seed", SEED),
        ("method", "proportional stratified by paper: >= 1 per paper with scenarios left, rest by "
                   "largest remainder; per paper sub.sample(n=k, random_state=seed) on rows sorted "
                   "by scenario number"),
        ("n_sample", N_SAMPLE),
        ("pool (scenarios in input)", len(df)),
        ("excluded (earlier human round)", int(is_excluded.sum())),
        ("eligible", len(eligible)),
        ("papers", df["paper_id"].nunique()),
        ("papers sampled", int((alloc > 0).sum())),
        ("verify rule", f">= {MIN_PRESENT} of {len(MODELS)} models tagged Clear or Ambiguous"),
        ("components to verify", int((comps["action"] == "Verify").sum())),
        ("components skipped", int((comps["action"] == "Skip").sum())),
        ("input", f"{INPUT_PATH} [{SHEET_NAME}]"),
        ("excluded from", EXCLUDE_PATH),
        ("models", ", ".join(MODELS)),
        ("python / pandas", f"{platform.python_version()} / {pd.__version__}"),
        ("drawn at", datetime.now().strftime("%Y-%m-%d %H:%M")),
    ], columns=["item", "value"])

    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with pd.ExcelWriter(OUTPUT_PATH) as writer:
        sample.to_excel(writer, sheet_name="sample", index=False)
        allocation.to_excel(writer, sheet_name="allocation", index=False)
        comps.to_excel(writer, sheet_name="components", index=False)
        protocol.to_excel(writer, sheet_name="protocol", index=False)

    print(allocation.to_string(index=False))
    print()
    print(protocol.to_string(index=False))
    print(f"\nSaved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
