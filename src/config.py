"""A run's config = task settings + model preset. The notebook only picks names:

    from src.config import get_config
    config = get_config("1a", "kimi-k2.5")

Task settings (prompt, seed terms) are the same for every model, so all models are
compared on the same input. Dry runs are not a preset: DRY_RUN is a separate switch
in the notebook, so a dry run tests the exact config the real run will use.
"""

# Fixed settings per task (paper settings: prompt v2, seed terms v2, Appendix C)
TASKS = {
    "1a": {
        "prompt_version": "prompt_1a_v2",
        "seed_terms_version": "v2",
    },
    # Threat model extraction per scenario (paper setting: prompt v2, 7 components)
    "2c": {
        "prompt_version": "prompt_2c_v2",
    },
}

MODELS = {
    # The model used in the phase-1 paper, through Hugging Face Inference with a Providers
    "kimi-k2.5": {
        "backend": "huggingface",
        "model": "moonshotai/Kimi-K2.5",
        "provider": "auto",       
        "temperature": 0.0,
        "max_new_tokens": 16384,
    },

    # Newer Kimi models through NVIDIA's free API (build.nvidia.com), called directly
    # with an NVIDIA key. NOT the paper's model (K2.5 is not on NVIDIA): a newer-model run.
    # Both think before answering (always on, by default), and thinking counts toward
    # max_new_tokens, hence the larger limit. Sampling = Moonshot's recommendation for
    # thinking mode (Kimi-K2.6 model card: temperature 1.0, top_p 0.95; Kimi-K3's card
    # reports its results at temperature 1.0). Optional, unverified on NVIDIA:
    # "extra_body": {"reasoning_effort": "high"} for K3 (its card lists low/high/max, default max).
    "kimi-k3-nvidia": {
        "backend": "nvidia",
        "model": "moonshotai/kimi-k3",
        "base_url": "https://integrate.api.nvidia.com/v1",
        "temperature": 1.0,
        "top_p": 0.95,
        "max_new_tokens": 32768,
    },
    "kimi-k2.6-nvidia": {
        "backend": "nvidia",
        "model": "moonshotai/kimi-k2.6",
        "base_url": "https://integrate.api.nvidia.com/v1",
        "temperature": 1.0,
        "top_p": 0.95,
        "max_new_tokens": 32768,
    },

    # Claude, through the Anthropic API. No temperature: these models reject it.
    # Effort is set explicitly so both Claude models run at the same level
    # (their defaults differ: Opus medium, Sonnet high).
    # Thinking counts toward max_new_tokens, hence the larger limit.

    "claude-sonnet-5.5": {
        "backend": "anthropic",
        "model": "claude-sonnet-5-5",
        "effort": "high",
        "max_new_tokens": 64000,
    },
    "claude-opus-5.5": {
        "backend": "anthropic",
        "model": "claude-opus-5-5",
        "effort": "high",
        "max_new_tokens": 64000,
    },
}

API_KEY_NAMES = {
    "huggingface": "HF_TOKEN",
    "nvidia": "NVIDIA_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
}


def get_config(task: str, model_key: str) -> dict:
    """Config for one run, e.g. get_config("1a", "kimi-k2.5").

    Returns a new dict, so editing it in the notebook never changes the presets.
    """
    if task not in TASKS:
        raise KeyError(f"Unknown task {task!r}. Known tasks: {', '.join(TASKS)}")
    if model_key not in MODELS:
        raise KeyError(f"Unknown model {model_key!r}. Known models: {', '.join(MODELS)}")
    return {
        "experiment": f"{task}_{model_key}_{TASKS[task]['prompt_version']}",  # free-text label, saved with the run
        **TASKS[task],
        **MODELS[model_key],
    }


def api_key_name(config: dict) -> str:
    """Name of the env variable / Colab secret with the key for this config's backend."""
    return API_KEY_NAMES[config["backend"]]
