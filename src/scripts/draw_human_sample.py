"""Task 2: draw the human-verification sample (50 of the 193 scenarios, excluding the earlier 25).

    uv run python -m src.scripts.draw_human_sample

Set the paths and the seed below, then run from the repo root.

Pre-registration: SEED is fixed here BEFORE the sample is drawn. Commit this file (with the
seed) first, then run it, so the git history shows the seed was chosen before anyone saw the
sample. Never change the seed after a run.

Sampling:
    pool      all scenarios in the merged judgements sheet (one row per paper_id + scenario_id)
    excluded  the 25 scenarios of the earlier human coding round
    draw      random.Random(SEED).sample(eligible, N_SAMPLE), where `eligible` is sorted by
              (paper_id, scenario_id) so the draw does not depend on the row order of the sheet

For every sampled scenario x component, the three models' uncertainty tags are listed, and the
component is marked "Verify" if at least 2 of the 3 models tagged it Clear or Ambiguous (i.e.
flagged it present), otherwise "Skip".

Output (one Excel file):
    sample      sample_order, paper_id, scenario_id, scenario_text   (the reproducible record)
    components  one row per sampled scenario x component: the 3 tags, n_present, Verify / Skip
    protocol    seed, method, pool / excluded / eligible sizes, input files, Python version, time
"""

import os
import platform
import random
from datetime import datetime

import pandas as pd

# --- Set these (paths relative to the repo root) ---
INPUT_PATH = "output/07_task_2c_llm_judgements_merged.xlsx"
SHEET_NAME = "judgements"
EXCLUDE_PATH = "materials/25_random_picked_scenario_to_label_FILTERED.xlsx"   # earlier 25
OUTPUT_PATH = "output/07_task_2c_human_sample_50.xlsx"

SEED = 20261026      # pre-registered (date the seed was fixed); do not change after the first run
N_SAMPLE = 50

MODELS = ["kimi_2.5", "glm_5.3", "deepseek_v4.1"]
COMPONENTS = [
    "threat_source", "objective_or_harmful_outcome", "capability", "knowledge",
    "access", "constraints_or_enabling_conditions", "target_or_asset_at_risk",
]
TAGS = {"Clear", "Ambiguous", "Not specified"}
PRESENT = {"Clear", "Ambiguous"}
MIN_PRESENT = 2      # verify a component when at least this many models flagged it present


def keys_of(df: pd.DataFrame, name: str) -> list[tuple[str, str]]:
    """(paper_id, scenario_id) of every row; stop on empty or duplicate keys."""
    keys = list(zip(df["paper_id"].str.strip(), df["scenario_id"].str.strip()))
    if any(not p or not s for p, s in keys):
        raise ValueError(f"{name}: a row has an empty paper_id or scenario_id")
    dupes = sorted({k for k in keys if keys.count(k) > 1})
    if dupes:
        raise ValueError(f"{name}: duplicate scenarios {dupes}")
    return keys


def draw_sample(pool: list[tuple[str, str]], excluded: list[tuple[str, str]],
                seed: int, n: int) -> list[tuple[str, str]]:
    """n scenarios from pool minus excluded, reproducible for a given seed."""
    missing = sorted(set(excluded) - set(pool))
    if missing:
        raise ValueError(f"Excluded scenarios not found in the pool: {missing}")
    eligible = sorted(set(pool) - set(excluded))
    if len(eligible) < n:
        raise ValueError(f"Only {len(eligible)} eligible scenarios, cannot draw {n}")
    return random.Random(seed).sample(eligible, n)


def component_rows(df: pd.DataFrame, sample: list[tuple[str, str]]) -> pd.DataFrame:
    """One row per sampled scenario x component: the three tags and Verify / Skip."""
    by_key = df.set_index(["paper_id", "scenario_id"])
    rows = []
    for order, key in enumerate(sample, start=1):
        r = by_key.loc[key]
        for comp in COMPONENTS:
            tags = {m: r[f"{comp}_uncertainty_{m}"] for m in MODELS}
            bad = {m: t for m, t in tags.items() if t not in TAGS}
            if bad:
                raise ValueError(f"{key[0]}_{key[1]} {comp}: unexpected tags {bad}")
            n_present = sum(t in PRESENT for t in tags.values())
            rows.append({"sample_order": order, "paper_id": key[0], "scenario_id": key[1],
                         "component": comp,
                         **{f"uncertainty_{m}": t for m, t in tags.items()},
                         "n_present": n_present,
                         "action": "Verify" if n_present >= MIN_PRESENT else "Skip"})
    return pd.DataFrame(rows)


def main() -> None:
    df = pd.read_excel(INPUT_PATH, sheet_name=SHEET_NAME, dtype=str, keep_default_na=False)
    df["paper_id"], df["scenario_id"] = df["paper_id"].str.strip(), df["scenario_id"].str.strip()
    ex = pd.read_excel(EXCLUDE_PATH, dtype=str, keep_default_na=False)
    pool, excluded = keys_of(df, INPUT_PATH), keys_of(ex, EXCLUDE_PATH)

    sample = draw_sample(pool, excluded, SEED, N_SAMPLE)
    text = df.set_index(["paper_id", "scenario_id"])["scenario_text"]
    sample_df = pd.DataFrame([{"sample_order": i, "paper_id": p, "scenario_id": s,
                               "scenario_text": text[(p, s)]}
                              for i, (p, s) in enumerate(sample, start=1)])
    comps = component_rows(df, sample)

    protocol = pd.DataFrame([
        ("seed", SEED),
        ("method", "random.Random(seed).sample(eligible sorted by (paper_id, scenario_id), n)"),
        ("n_sample", N_SAMPLE),
        ("pool (scenarios in input)", len(pool)),
        ("excluded (earlier human round)", len(excluded)),
        ("eligible", len(pool) - len(excluded)),
        ("verify rule", f">= {MIN_PRESENT} of {len(MODELS)} models tagged Clear or Ambiguous"),
        ("components to verify", int((comps["action"] == "Verify").sum())),
        ("components skipped", int((comps["action"] == "Skip").sum())),
        ("input", f"{INPUT_PATH} [{SHEET_NAME}]"),
        ("excluded from", EXCLUDE_PATH),
        ("models", ", ".join(MODELS)),
        ("python", platform.python_version()),
        ("drawn at", datetime.now().strftime("%Y-%m-%d %H:%M")),
    ], columns=["item", "value"])

    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with pd.ExcelWriter(OUTPUT_PATH) as writer:
        sample_df.to_excel(writer, sheet_name="sample", index=False)
        comps.to_excel(writer, sheet_name="components", index=False)
        protocol.to_excel(writer, sheet_name="protocol", index=False)

    print(protocol.to_string(index=False))
    print(f"\nSaved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
