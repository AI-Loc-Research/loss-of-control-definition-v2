"""Where each task reads its input and writes its output.

The layout is the same locally and in Colab, always relative to the repo root:

    raw_text_final/<paper_id>.txt        Stage 0 output: plain text of the final papers
    output/scenarios_final.json          the 193 final scenarios (input of Task 2C)
    output/<model_name>/<task>/          everything one task produces for one model
        e.g. output/Kimi-K2.5/02_task_1a/, output/kimi-k3/07_task_2c/
    output/<model_name>_dryrun/<task>/   the same for dry runs (mock replies; git-ignored)

<model_name> is the part of the model id after the "/":
    "moonshotai/Kimi-K2.5"  ->  "Kimi-K2.5"
"""

import os

RAW_TEXT_DIR = "raw_text_final"
OUTPUT_DIR = "output"
# The 193 final scenarios (paper_id, scenario_id, scenario_text): input of Tasks 2B / 2C.
# Built from the phase-1 library Excel by src/scripts/collect_scenarios.py.
SCENARIOS_FILE = os.path.join(OUTPUT_DIR, "scenarios_final.json")


def model_folder_name(model: str) -> str:
    """'moonshotai/Kimi-K2.5' -> 'Kimi-K2.5'"""
    return model.split("/")[-1]


def task_output_dir(repo_root: str, model: str, task: str, dry_run: bool = False) -> str:
    """Folder for one task's results, e.g. <repo>/output/Kimi-K2.5/02_task_1a

    Dry runs (fake model replies) go to <model_name>_dryrun instead, so their mock
    outputs can never be mistaken for real ones, or skipped over by a real run.
    """
    folder = model_folder_name(model) + ("_dryrun" if dry_run else "")
    return os.path.join(repo_root, OUTPUT_DIR, folder, task)


def raw_text_path(repo_root: str, paper_id: str) -> str:
    """Plain text of one paper, e.g. <repo>/raw_text_final/amodei_2026.txt"""
    return os.path.join(repo_root, RAW_TEXT_DIR, f"{paper_id}.txt")


def scenarios_path(repo_root: str) -> str:
    """The final scenario list, e.g. <repo>/output/scenarios_final.json"""
    return os.path.join(repo_root, SCENARIOS_FILE)


def final_papers(papers: list[dict]) -> list[dict]:
    """Papers in the final corpus. A paper marked `final: false` in papers.yaml is skipped."""
    return [p for p in papers if p.get("final", True)]
