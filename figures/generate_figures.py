"""Generate the three main figures for the paper.

Figure 1: Horizontal bar chart — Component Specification Rates
Figure 2: Heatmap — Component Specification by Paper
Figure 3: UpSet-style chart — Scenario Archetypes

Data source: drive/loc_definition_project/stages/scenario_final_resolved.xlsx
  (Sheet1 — the human-reviewed, final-resolved 193 scenarios from 29 papers.
   The "deleted 12" sheet contains scenarios excluded during review with
   principled reasons; they are NOT included in any of these figures.)

Citation labels: paper_labels.yaml (Zotero-sourced, single source of truth).
"""

import os
from collections import Counter, defaultdict

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import numpy as np
import openpyxl
import yaml
from matplotlib.colors import LinearSegmentedColormap

# --- Shared style ---
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.labelsize": 11,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": "#333333",
    "axes.linewidth": 0.8,
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "text.color": "#1a1a1a",
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.3,
})

# Color palette
COLOR_HIGH = "#2c6fbb"
COLOR_LOW = "#c44e52"
COLOR_MID_BLUE = "#6baed6"
COLOR_NOT_SPEC = "#e0e0e0"
COLOR_DOT_FILL = "#2d2d2d"


# ============================================================
# DATA LOADING
# ============================================================

_REPO_ROOT = os.path.join(os.path.dirname(__file__), "..")
_XLSX_PATH = os.path.join(
    _REPO_ROOT, "drive", "loc_definition_project", "stages",
    "scenario_final_resolved.xlsx",
)
_LABELS_PATH = os.path.join(_REPO_ROOT, "paper_labels.yaml")

# Column indices in Sheet1 (1-indexed as in Excel, but openpyxl returns 0-indexed tuples)
# Order: paper_id, scenario_id, comments, scenario_text, why_this_is_a_scenario,
# loss_of_control_relevance, causal_elements_present, is_partial,
# threat_source, threat_source_evidence, threat_source_uncertainty,
# objective_or_harmful_outcome, ... evidence, ... uncertainty,
# capability, ..., knowledge, ..., access, ..., constraints..., target...
_COL_PAPER_ID = 0
# Each component has 3 columns: value, evidence, uncertainty.
# We track the *value* column for "is specified" checks.
COMPONENTS = [
    ("threat_source", "Threat Source", 8),
    ("objective_or_harmful_outcome", "Objective / Harmful Outcome", 11),
    ("capability", "Capability", 14),
    ("knowledge", "Knowledge", 17),
    ("access", "Access", 20),
    ("constraints_or_enabling_conditions", "Constraints / Enabling Cond.", 23),
    ("target_or_asset_at_risk", "Target / Asset at Risk", 26),
]
# Uncertainty flag column for each component (parallel order to COMPONENTS)
UNCERTAINTY_COLS = [10, 13, 16, 19, 22, 25, 28]

# Three-state palette for the stacked variant
COLOR_CLEAR = COLOR_HIGH                 # blue — present and clearly stated
COLOR_AMBIGUOUS = "#e8a33d"              # amber — present but uncertain
COLOR_NOT_SPECIFIED_STACK = "#dcdcdc"    # light gray — absent


def _is_specified(value) -> bool:
    """A component is 'specified' if its cell is non-empty and not 'Not specified'."""
    if value is None:
        return False
    s = str(value).strip()
    return bool(s) and s != "Not specified"


def load_data():
    """Load and process the 193-scenario corpus from the Excel file.

    Returns a dict with:
      - scenarios: list of (paper_id, [7 binary flags]) tuples
      - component_rates: list of {key, label, pct} sorted by pct desc
      - per_paper: list of {paper_id, n, vals} sorted by overall_pct desc
      - archetypes: list of {pattern, count} sorted by count desc
    """
    wb = openpyxl.load_workbook(_XLSX_PATH, data_only=True)
    sh = wb["Sheet1"]
    raw_rows = [r for r in sh.iter_rows(min_row=2, values_only=True) if r[_COL_PAPER_ID]]

    # Per-scenario binary flags for the 7 components
    scenarios = []
    for r in raw_rows:
        flags = tuple(1 if _is_specified(r[col]) else 0 for _, _, col in COMPONENTS)
        scenarios.append((r[_COL_PAPER_ID], flags))

    n_total = len(scenarios)

    # Overall component rates + uncertainty breakdown
    component_rates = []
    for i, (key, label, _) in enumerate(COMPONENTS):
        specified = sum(s[1][i] for s in scenarios)
        unc_col = UNCERTAINTY_COLS[i]
        clear = sum(1 for r in raw_rows if str(r[unc_col]).strip() == "Clear" if r[unc_col])
        ambig = sum(1 for r in raw_rows if str(r[unc_col]).strip() == "Ambiguous" if r[unc_col])
        not_spec = n_total - clear - ambig
        component_rates.append({
            "key": key,
            "label": label,
            "pct": 100 * specified / n_total,
            "clear_pct": 100 * clear / n_total,
            "ambiguous_pct": 100 * ambig / n_total,
            "not_specified_pct": 100 * not_spec / n_total,
        })
    component_rates.sort(key=lambda x: -x["pct"])

    # Per-paper rates
    paper_data = defaultdict(lambda: {"n": 0, "counts": [0] * 7})
    for paper, flags in scenarios:
        paper_data[paper]["n"] += 1
        for i, f in enumerate(flags):
            paper_data[paper]["counts"][i] += f

    per_paper = []
    for paper, d in paper_data.items():
        vals = [100 * c / d["n"] for c in d["counts"]]
        per_paper.append({
            "paper_id": paper,
            "n": d["n"],
            "vals": vals,
            "overall_pct": sum(vals) / 7,
        })
    per_paper.sort(key=lambda x: -x["overall_pct"])

    # Archetypes
    pattern_counter = Counter(flags for _, flags in scenarios)
    archetypes = [
        {"pattern": list(p), "count": c}
        for p, c in pattern_counter.most_common()
    ]

    return {
        "n_total": n_total,
        "n_papers": len(paper_data),
        "scenarios": scenarios,
        "component_rates": component_rates,
        "per_paper": per_paper,
        "archetypes": archetypes,
    }


def load_paper_labels() -> dict:
    """Load paper_id → citation_label mapping from Zotero-sourced YAML."""
    with open(_LABELS_PATH, "r", encoding="utf-8") as f:
        labels = yaml.safe_load(f)["papers"]
    return {p["paper_id"]: p["citation_label"] for p in labels}


# Pre-load
DATA = load_data()
PAPER_LABEL = load_paper_labels()

# Column order for the heatmap: TS, OHO, TAR, Cap, CEC, Acc, K
# (sorted by overall specification rate, high → low)
HEATMAP_COL_KEYS = ["threat_source", "objective_or_harmful_outcome",
                    "target_or_asset_at_risk", "capability",
                    "constraints_or_enabling_conditions", "access", "knowledge"]
HEATMAP_COL_LABELS = ["Threat Source", "Objective", "Target", "Capability",
                      "Constraints", "Access", "Knowledge"]
# Map key to component index for cross-referencing
_KEY_TO_IDX = {key: i for i, (key, _, _) in enumerate(COMPONENTS)}

# Short labels for UpSet plot rows
UPSET_COMP_LABELS = ["TS", "OHO", "Cap", "K", "Acc", "CEC", "TAR"]


# ============================================================
# FIGURE 1: Horizontal Bar Chart
# ============================================================

def make_figure1():
    fig, ax = plt.subplots(figsize=(9, 4.8))

    rates = DATA["component_rates"]
    labels = [r["label"] for r in rates]
    values = [r["pct"] for r in rates]
    colors = [COLOR_HIGH if v >= 50 else COLOR_LOW for v in values]

    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, values, height=0.62, color=colors,
                   edgecolor="white", linewidth=0.5)

    for bar, val in zip(bars, values):
        if val > 40:
            ax.text(val - 2, bar.get_y() + bar.get_height() / 2,
                    f"{val:.1f}%", va="center", ha="right", fontsize=10.5,
                    fontweight="bold", color="white")
        else:
            ax.text(val + 1.5, bar.get_y() + bar.get_height() / 2,
                    f"{val:.1f}%", va="center", ha="left", fontsize=10.5,
                    fontweight="bold", color="#333333")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=10.5)
    ax.set_xlim(0, 108)
    ax.set_xlabel(f"Percentage of scenarios specifying component  (n = {DATA['n_total']})",
                  fontsize=10)
    ax.invert_yaxis()

    # Thin separator line between high-spec and low-spec tiers
    # Find the index where pct drops below 50
    sep_idx = next(i for i, r in enumerate(rates) if r["pct"] < 50) - 0.5
    ax.axhline(sep_idx, color="#cccccc", linewidth=1, linestyle="-")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.set_title(
        f"Threat Model Component Specification Rates\nAcross {DATA['n_total']} Loss-of-Control Scenarios",
        pad=16, fontsize=13, fontweight="bold",
    )

    fig.tight_layout()
    fig.savefig("figures/fig1_component_rates.png")
    fig.savefig("figures/fig1_component_rates.pdf")
    print("Figure 1 saved.")
    plt.close(fig)


# ============================================================
# FIGURE 1B: Stacked variant — Clear / Ambiguous / Not specified
# ============================================================

def make_figure1_stacked():
    """Alternative version of Figure 1 showing the full three-category
    uncertainty breakdown as stacked bars summing to 100%."""
    fig, ax = plt.subplots(figsize=(9, 4.8))

    rates = DATA["component_rates"]
    labels = [r["label"] for r in rates]
    clear = np.array([r["clear_pct"] for r in rates])
    ambig = np.array([r["ambiguous_pct"] for r in rates])
    not_spec = np.array([r["not_specified_pct"] for r in rates])

    y_pos = np.arange(len(labels))
    h = 0.62

    bars_clear = ax.barh(y_pos, clear, height=h,
                         color=COLOR_CLEAR, edgecolor="white", linewidth=0.5,
                         label="Clear")
    bars_amb = ax.barh(y_pos, ambig, left=clear, height=h,
                       color=COLOR_AMBIGUOUS, edgecolor="white", linewidth=0.5,
                       label="Ambiguous")
    bars_ns = ax.barh(y_pos, not_spec, left=clear + ambig, height=h,
                      color=COLOR_NOT_SPECIFIED_STACK, edgecolor="white",
                      linewidth=0.5, label="Not specified")

    # Label the Clear segment — always inside, right-aligned at the segment edge.
    # For very narrow bars, shrink the font so it still fits inside.
    for bar, val in zip(bars_clear, clear):
        fs = 10.5 if val >= 14 else 9
        ax.text(val - 1, bar.get_y() + bar.get_height() / 2,
                f"{val:.1f}%", va="center", ha="right", fontsize=fs,
                fontweight="bold", color="white")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=10.5)
    ax.set_xlim(0, 100)
    ax.set_xlabel(f"Percentage of scenarios  (n = {DATA['n_total']})",
                  fontsize=10)
    ax.invert_yaxis()

    # Same tier separator as Figure 1
    sep_idx = next(i for i, r in enumerate(rates) if r["pct"] < 50) - 0.5
    ax.axhline(sep_idx, color="#cccccc", linewidth=1, linestyle="-")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Legend above the bars, between title and plot area — keeps it clear
    # of the x-axis title at the bottom.
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0),
              fontsize=9, framealpha=0.95, edgecolor="#cccccc", ncol=3)

    ax.set_title(
        f"Threat Model Component Specification by Uncertainty Flag\n"
        f"Across {DATA['n_total']} Loss-of-Control Scenarios",
        pad=44, fontsize=13, fontweight="bold",
    )

    fig.tight_layout()
    fig.savefig("figures/fig1b_stacked_uncertainty.png")
    fig.savefig("figures/fig1b_stacked_uncertainty.pdf")
    print("Figure 1B saved.")
    plt.close(fig)


# ============================================================
# FIGURE 2: Heatmap
# ============================================================

def make_figure2():
    papers = DATA["per_paper"]
    n_papers = len(papers)
    n_cols = len(HEATMAP_COL_KEYS)

    # Build matrix: rows = papers, cols = components (in heatmap order)
    matrix = np.zeros((n_papers, n_cols))
    for i, p in enumerate(papers):
        for j, key in enumerate(HEATMAP_COL_KEYS):
            matrix[i, j] = p["vals"][_KEY_TO_IDX[key]]

    row_labels = [f"{PAPER_LABEL[p['paper_id']]}  (n={p['n']})" for p in papers]

    fig, ax = plt.subplots(figsize=(8.5, 10.5))

    cmap = LinearSegmentedColormap.from_list("spec", [
        "#f5f5f5", "#fdd8b3", "#f4a259", "#d95f3b", "#a82a2a",
    ])

    im = ax.imshow(matrix, cmap=cmap, aspect="auto", vmin=0, vmax=100)

    for i in range(n_papers):
        for j in range(n_cols):
            val = matrix[i, j]
            if val == 0:
                txt = "—"
                color = "#999999"
            elif val == 100:
                txt = "100"
                color = "white"
            else:
                txt = f"{val:.0f}"
                color = "white" if val >= 60 else "#333333"
            ax.text(j, i, txt, ha="center", va="center",
                    fontsize=7.8, color=color, fontweight="medium")

    ax.set_xticks(range(n_cols))
    ax.set_xticklabels(HEATMAP_COL_LABELS, fontsize=9.5, fontweight="medium",
                       rotation=30, ha="left", rotation_mode="anchor")
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")

    ax.set_yticks(range(n_papers))
    ax.set_yticklabels(row_labels, fontsize=8.2)

    for i in range(n_papers + 1):
        ax.axhline(i - 0.5, color="white", linewidth=1.8)
    for j in range(n_cols + 1):
        ax.axvline(j - 0.5, color="white", linewidth=1.8)

    # Separator before the two gap columns (Access, Knowledge)
    ax.axvline(4.5, color="#333333", linewidth=2.5)

    cbar = fig.colorbar(im, ax=ax, shrink=0.35, aspect=22, pad=0.025)
    cbar.set_label("% of paper's scenarios\nspecifying component", fontsize=8.5)
    cbar.ax.tick_params(labelsize=7.5)

    ax.set_title("Component Specification Rates by Paper",
                 pad=18, fontsize=13, fontweight="bold")

    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig("figures/fig2_heatmap.png")
    fig.savefig("figures/fig2_heatmap.pdf")
    print("Figure 2 saved.")
    plt.close(fig)


# ============================================================
# FIGURE 3: UpSet-style chart
# ============================================================

def make_figure3():
    # Show top N archetypes by frequency
    top_n = 12
    archetypes = DATA["archetypes"][:top_n]
    n_combos = len(archetypes)
    n_comps = 7

    fig = plt.figure(figsize=(11, 7.5))
    gs = gridspec.GridSpec(
        2, 1, height_ratios=[2.2, 1], hspace=0.05,
        left=0.1, right=0.95, top=0.88, bottom=0.05,
    )

    ax_bar = fig.add_subplot(gs[0])
    ax_dot = fig.add_subplot(gs[1])

    x_pos = np.arange(n_combos)

    counts = [a["count"] for a in archetypes]
    bar_colors = []
    for a in archetypes:
        k_present = a["pattern"][3] == 1
        acc_present = a["pattern"][4] == 1
        if k_present:
            bar_colors.append(COLOR_HIGH)
        elif acc_present:
            bar_colors.append(COLOR_MID_BLUE)
        else:
            bar_colors.append(COLOR_LOW)

    bars = ax_bar.bar(x_pos, counts, width=0.68, color=bar_colors,
                      edgecolor="white", linewidth=0.5)

    for bar, val in zip(bars, counts):
        ax_bar.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.6,
                    str(val), ha="center", va="bottom", fontsize=9.5,
                    fontweight="bold", color="#333333")

    ax_bar.set_ylabel("Number of scenarios", fontsize=10.5)
    ax_bar.set_ylim(0, max(counts) * 1.15)
    ax_bar.spines["top"].set_visible(False)
    ax_bar.spines["right"].set_visible(False)
    ax_bar.set_xticks([])
    ax_bar.set_xlim(-0.7, n_combos - 0.3)

    ax_bar.set_title(
        f"Scenario Archetypes: Component Co-occurrence Patterns\n"
        f"(n = {DATA['n_total']} scenarios across {DATA['n_papers']} papers)",
        pad=14, fontsize=13, fontweight="bold",
    )

    legend_elements = [
        mpatches.Patch(facecolor=COLOR_LOW, label="Knowledge & Access absent"),
        mpatches.Patch(facecolor=COLOR_MID_BLUE, label="Access present, Knowledge absent"),
        mpatches.Patch(facecolor=COLOR_HIGH, label="Knowledge present"),
    ]
    ax_bar.legend(handles=legend_elements, loc="upper right", fontsize=8.5,
                  framealpha=0.95, edgecolor="#cccccc")

    # Dot matrix
    dot_size = 140

    # Knowledge row highlight
    ax_dot.axhspan(2.5, 3.5, color="#fff0f0", alpha=0.7, zorder=0)
    for j in range(n_comps):
        ax_dot.axhline(j, color="#f0f0f0", linewidth=0.8, zorder=0)

    for i, a in enumerate(archetypes):
        pattern = a["pattern"]
        filled_y = [j for j in range(n_comps) if pattern[j] == 1]
        empty_y = [j for j in range(n_comps) if pattern[j] == 0]

        if empty_y:
            ax_dot.scatter([i] * len(empty_y), empty_y, s=dot_size,
                           facecolors=COLOR_NOT_SPEC, edgecolors="#cccccc",
                           linewidths=1, zorder=3)
        if filled_y:
            ax_dot.scatter([i] * len(filled_y), filled_y, s=dot_size,
                           facecolors=COLOR_DOT_FILL, edgecolors=COLOR_DOT_FILL,
                           linewidths=0.5, zorder=4)
            ax_dot.plot([i, i], [min(filled_y), max(filled_y)],
                        color=COLOR_DOT_FILL, linewidth=2.5, zorder=2,
                        solid_capstyle="round")

    ax_dot.set_yticks(range(n_comps))
    ax_dot.set_yticklabels(UPSET_COMP_LABELS, fontsize=10, fontweight="medium")
    ax_dot.set_xlim(-0.7, n_combos - 0.3)
    ax_dot.set_ylim(n_comps - 0.6, -0.6)

    ax_dot.spines["top"].set_visible(False)
    ax_dot.spines["right"].set_visible(False)
    ax_dot.spines["bottom"].set_visible(False)
    ax_dot.set_xticks([])

    ax_dot.text(n_combos - 0.2, 3, "← rarely present", fontsize=8.5,
                color=COLOR_LOW, va="center", ha="left", fontstyle="italic")

    fig.savefig("figures/fig3_upset_archetypes.png")
    fig.savefig("figures/fig3_upset_archetypes.pdf")
    print("Figure 3 saved.")
    plt.close(fig)


if __name__ == "__main__":
    print(f"Loaded {DATA['n_total']} scenarios from {DATA['n_papers']} papers.\n")
    make_figure1()
    make_figure1_stacked()
    make_figure2()
    make_figure3()
    print("\nAll figures generated.")
