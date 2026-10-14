"""Build output/scenarios_final.json (input of Task 2C) from the phase-1 scenario library Excel.

    `uv run python -m src.scripts.collect_scenarios [path/to/scenario_final_resolved.xlsx]`

Reads Sheet1 (the 193 final scenarios) and keeps only paper_id, scenario_id and
scenario_text, the format run_2c expects:

[{"paper_id": "amodei_2026", "scenario_id": "S1", "scenario_text": "..."}, ...]

"""

import json
import os
import sys

import pandas as pd
import yaml

from src.paths import final_papers, scenarios_path

DEFAULT_EXCEL = "materials/scenario_final_resolved.xlsx"
PAPER_ID_FIXES = {"barrett_2026": "barrett_2016"}


def collect_scenarios(excel_path: str = DEFAULT_EXCEL, repo_root: str = ".") -> list[dict]:
    df = pd.read_excel(excel_path, sheet_name="Sheet1", dtype=str)
    df = df.dropna(subset=["scenario_text"])   # the sheet has empty rows after the data

    scenarios = []
    for row in df.itertuples(index=False):
        paper_id = PAPER_ID_FIXES.get(row.paper_id.strip(), row.paper_id.strip())
        if paper_id != row.paper_id.strip():
            print(f"  fixed paper id {row.paper_id!r} -> {paper_id!r} ({row.scenario_id})")
        scenarios.append({
            "paper_id": paper_id,
            "scenario_id": row.scenario_id.strip(),
            "scenario_text": row.scenario_text,
        })

    # Checks: unique keys, every paper is a final paper in papers.yaml
    keys = [(s["paper_id"], s["scenario_id"]) for s in scenarios]
    duplicates = sorted({k for k in keys if keys.count(k) > 1})
    if duplicates:
        raise ValueError(f"Duplicate (paper_id, scenario_id): {duplicates}")
    with open(f"{repo_root}/papers.yaml", encoding="utf-8") as f:
        known = {p["id"] for p in final_papers(yaml.safe_load(f)["papers"])}
    unknown = sorted({s["paper_id"] for s in scenarios} - known)
    if unknown:
        raise ValueError(f"Paper ids not among the final papers in papers.yaml: {unknown}")

    out_path = scenarios_path(repo_root)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)   # output/ may not exist in a fresh clone
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(scenarios, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"{len(scenarios)} scenarios from {len(known & {s['paper_id'] for s in scenarios})} papers -> {out_path}")
    return scenarios


if __name__ == "__main__":
    collect_scenarios(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_EXCEL)
