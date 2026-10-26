"""Task 2C: agreement of the uncertainty tags across the three models (no humans).

    uv run python -m src.scripts.tag_agreement

Set the paths below, then run from the repo root.

Input: the merged judgements sheet (src/scripts/merge_judgements.py), one row per scenario,
with one column <component>_uncertainty_<model> per component and model.

For every scenario x component, the three tags (Clear / Ambiguous / Not specified) are
classified as:
    All-3 agree   all three models gave the same tag
    2-of-3 agree  two models gave the same tag, the third a different one
    All differ    all three tags are different
With 3 models and 3 possible tags, every cell falls into exactly one class.

Output: one table, one row per component (plus a row over all components), with the count
and the % of scenarios in each class, and a small "Metadata" table below it (scenarios,
flags, components, models, compared cells). Printed, and saved as a PNG image (matplotlib),
in the same visual style as the Krippendorff-alpha figures (page colour, white cards, font).
"""

import os

import matplotlib

matplotlib.use("Agg")  # render to a file only; no window needed

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

# --- Set these (paths relative to the repo root) ---
INPUT_PATH = "output/07_task_2c_llm_judgements_merged.xlsx"
SHEET_NAME = "judgements"
OUTPUT_PATH = "output/07_task_2c_tag_agreement.png"

TITLE = "LLM LoC scenario judgement, agreement across Kimi K2.5, GLM-5.3 and DeepSeek V4.1"
FLAGS_TEXT = "Clear, Ambiguous and Not specified"
GROUP_HEADER = "Flags (labels) Agreements"   # label row above the three agreement columns
SUMMARY_HEADING = "Metadata"

MODELS = ["kimi_2.5", "glm_5.3", "deepseek_v4.1"]
COMPONENTS = [
    "threat_source", "objective_or_harmful_outcome", "capability", "knowledge",
    "access", "constraints_or_enabling_conditions", "target_or_asset_at_risk",
]
TAGS = {"Clear", "Ambiguous", "Not specified"}
CLASSES = ["All-3 agree", "2-of-3 agree", "All differ"]


def classify(tags: list[str]) -> str:
    """Agreement class of the three tags of one scenario x component."""
    distinct = len(set(tags))
    return {1: "All-3 agree", 2: "2-of-3 agree", 3: "All differ"}[distinct]


def check_tags(df: pd.DataFrame) -> None:
    """Stop if a column is missing, or a tag is empty or not one of the three allowed values."""
    columns = [f"{c}_uncertainty_{m}" for c in COMPONENTS for m in MODELS]
    missing = [c for c in columns if c not in df.columns]
    if missing:
        raise ValueError(f"Columns not found in {INPUT_PATH}: {missing}")
    problems = []
    for col in columns:
        for i, tag in df[col].items():
            if tag not in TAGS:
                problems.append(f"row {i + 2} ({df.at[i, 'paper_id']}_{df.at[i, 'scenario_id']}) {col}: {tag!r}")
    if problems:
        raise ValueError("Unexpected tags (allowed: Clear / Ambiguous / Not specified):\n  "
                         + "\n  ".join(problems[:20]))


def agreement_table(df: pd.DataFrame) -> pd.DataFrame:
    """Per component: count and % of scenarios in each agreement class, plus an 'All components' row."""
    rows, overall = [], {k: 0 for k in CLASSES}
    for comp in COMPONENTS:
        classes = df.apply(lambda r: classify([r[f"{comp}_uncertainty_{m}"] for m in MODELS]), axis=1)
        counts = classes.value_counts()
        row = {"component": comp, "n_scenarios": len(df)}
        for k in CLASSES:
            n = int(counts.get(k, 0))
            overall[k] += n
            row[f"{k} (n)"] = n
            row[f"{k} (%)"] = round(100 * n / len(df), 1)
        rows.append(row)
    total = len(df) * len(COMPONENTS)
    row = {"component": "All components", "n_scenarios": total}
    for k in CLASSES:
        row[f"{k} (n)"] = overall[k]
        row[f"{k} (%)"] = round(100 * overall[k] / total, 1)
    rows.append(row)
    return pd.DataFrame(rows)


def cell_text(pct: float, n: int) -> str:
    """e.g. ' 97.9% (189)', right-aligned to the column width."""
    return f"{pct:.1f}% ({n})".rjust(16)


def print_table(table: pd.DataFrame) -> None:
    print(f"\nTag agreement across {', '.join(MODELS)} "
          f"({table.iloc[0]['n_scenarios']} scenarios per component)\n")
    header = f"{'Component':36} | " + " | ".join(f"{k:>16}" for k in CLASSES)
    print(header)
    print("-" * len(header))
    for _, r in table.iterrows():
        if r["component"] == "All components":
            print("-" * len(header))
        cells = " | ".join(cell_text(r[f"{k} (%)"], r[f"{k} (n)"]) for k in CLASSES)
        print(f"{r['component']:36} | {cells}")
    print("\n(n) = number of cells; the 'All components' row counts scenario x component cells.")


# --- Table image: same theme as the Krippendorff-alpha figures --------------------------
INK, INK_2 = "#0b0b0b", "#4a4641"                        # text: primary / secondary
PAGE, CARD, CARD_EDGE = "#ebeeec", "#ffffff", "#d6dcd8"  # page, white cards, card border
RULE = "#c3c2b7"                                         # thin rules inside a card
STRIPE = "#f5f6f4"                                       # alternate rows

_INSTALLED = {f.name for f in font_manager.fontManager.ttflist}
FONT = next((f for f in ("Segoe UI", "Helvetica Neue", "Arial") if f in _INSTALLED), "DejaVu Sans")


def pretty(component: str) -> str:
    """'objective_or_harmful_outcome' -> 'Objective or harmful outcome'."""
    return component.replace("_", " ").capitalize()


def save_table_image(table: pd.DataFrame, n_scenarios: int, path: str) -> None:
    """Title, then the agreement table on one white card and the summary table on another."""
    n_comp, n_models = len(COMPONENTS), len(MODELS)
    summary_rows = [
        ("Total unique scenarios", f"{n_scenarios}"),
        ("Three flags", FLAGS_TEXT),
        ("Total components", f"{n_comp}"),
        ("Models (judges)", f"{n_models}"),
        ("Compared cells (scenario × component)", f"{n_scenarios} × {n_comp} = {n_scenarios * n_comp:,}"),
    ]
    # layout in inches; y is measured downward from the top of the page
    side, pad, row_h = 0.45, 0.32, 0.50        # page margin, padding inside a card, row height
    comp_w, cls_w = 4.3, 2.2                   # component column, each agreement column
    card_w = 2 * pad + comp_w + len(CLASSES) * cls_w
    sum_w = 7.8                                # summary card width
    title_h, gap, group_h = 0.95, 0.40, 0.42   # title band, gap between cards, group label row
    fs, fs_title = 13.5, 17                    # table text, title
    main_h = 2 * pad + group_h + (len(table) + 1) * row_h   # group label + header row + data rows
    sum_h = 2 * pad + (len(summary_rows) + 1) * row_h       # "Metadata" heading + rows
    width, height = 2 * side + card_w, title_h + main_h + gap + sum_h + side

    with plt.rc_context({"font.family": FONT, "font.size": fs}):
        fig = plt.figure(figsize=(width, height), facecolor=PAGE)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, width)
        ax.set_ylim(height, 0)   # y grows downward, like reading a page
        ax.axis("off")

        def card(x, y, w, h):
            ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.20",
                                        facecolor=CARD, edgecolor=CARD_EDGE, linewidth=0.8, zorder=0))

        def stripe(x, y, w):
            ax.add_patch(Rectangle((x, y - row_h / 2), w, row_h, facecolor=STRIPE, edgecolor="none",
                                   zorder=1))

        def hline(y, x0, x1, color=RULE, lw=0.8):
            ax.plot([x0, x1], [y, y], color=color, linewidth=lw, solid_capstyle="butt", zorder=2)

        ax.text(width / 2, title_h / 2, TITLE, ha="center", va="center", fontsize=fs_title,
                fontweight="semibold", color=INK)

        # --- main agreement table ---
        top = title_h
        card(side, top, card_w, main_h)
        x0 = side + pad
        x1 = x0 + comp_w + len(CLASSES) * cls_w
        x_mid = [x0 + comp_w + (i + 0.5) * cls_w for i in range(len(CLASSES))]   # column centres
        # group label over the three agreement columns, with a rule under it
        gy = top + pad + group_h / 2
        ax.text((x0 + comp_w + x1) / 2, gy, GROUP_HEADER, ha="center", va="center", fontsize=fs - 1,
                fontweight="semibold", color=INK_2)
        hline(top + pad + group_h, x0 + comp_w + 0.15, x1 - 0.15, color=INK, lw=1.6)
        y = top + pad + group_h + row_h / 2
        ax.text(x0 + 0.1, y, "Component", ha="left", va="center", fontweight="semibold", color=INK)
        for x, name in zip(x_mid, CLASSES):
            ax.text(x, y, name, ha="center", va="center", fontweight="semibold", color=INK)
        hline(y + row_h / 2, x0, x1, color=INK_2, lw=1.0)
        for i, (_, r) in enumerate(table.iterrows()):
            y += row_h
            total = r["component"] == "All components"
            if total:
                hline(y - row_h / 2, x0, x1, color=INK_2, lw=1.0)
            elif i % 2 == 1:
                stripe(x0, y, x1 - x0)
            weight = "semibold" if total else "normal"
            label = "All components" if total else pretty(r["component"])
            ax.text(x0 + 0.1, y, label, ha="left", va="center", fontweight=weight, color=INK, zorder=3)
            for x, k in zip(x_mid, CLASSES):
                ax.text(x, y, f"{r[f'{k} (%)']:.1f}%  ({r[f'{k} (n)']:,})", ha="center", va="center",
                        fontweight=weight, color=INK, zorder=3)

        # --- summary table (two columns), under a "Metadata" heading ---
        top = title_h + main_h + gap
        card(side, top, sum_w, sum_h)
        sx0, sx1 = side + pad, side + sum_w - pad
        y = top + pad + row_h / 2
        ax.text(sx0 + 0.1, y, SUMMARY_HEADING, ha="left", va="center", fontweight="semibold", color=INK)
        hline(y + row_h / 2, sx0, sx1, color=INK_2, lw=1.0)
        for j, (label, value) in enumerate(summary_rows):
            y += row_h
            if j % 2 == 1:
                stripe(sx0, y, sx1 - sx0)
            ax.text(sx0 + 0.1, y, label, ha="left", va="center", color=INK_2, zorder=3)
            ax.text(sx1 - 0.1, y, value, ha="right", va="center", color=INK, zorder=3)

        fig.savefig(path, dpi=200, facecolor=PAGE)
        plt.close(fig)


def main() -> None:
    df = pd.read_excel(INPUT_PATH, sheet_name=SHEET_NAME, dtype=str, keep_default_na=False)
    check_tags(df)
    table = agreement_table(df)
    print_table(table)

    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    save_table_image(table, len(df), OUTPUT_PATH)
    print(f"\nSaved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
