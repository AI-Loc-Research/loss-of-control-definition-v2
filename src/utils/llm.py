"""One entry point for every model: picks the backend named in the config.

    config["backend"] == "huggingface"  ->  hf_client.query_llm  (e.g. Kimi K2.5)
    config["backend"] == "nvidia"       ->  hf_client.query_llm with config["base_url"]
                                            (NVIDIA's OpenAI-compatible API, e.g. Kimi K3)
    config["backend"] == "anthropic"    ->  anthropic_client.query_claude  (Claude)

Configs without "backend" (older notebooks) use Hugging Face, as before.
"""

import json

from src.utils.hf_client import query_llm


def call_model(prompt: str, config: dict, api_key: str, dry_run: bool = False,
               mock: dict | None = None) -> dict:
    """Send one prompt with the settings in config; returns the query_llm dict shape.
    dry_run returns the mock reply for every backend: no key, no network, no cost.
    mock: the fake reply to use in a dry run (default: the Task 1A mock in hf_client).
    """
    if dry_run:
        result = query_llm(prompt, config["model"], hf_token="", dry_run=True)
        if mock is not None:
            result["generated_text"] = json.dumps(mock, indent=2)
        return result

    backend = config.get("backend", "huggingface")
    if backend == "huggingface":
        return query_llm(
            prompt=prompt,
            model=config["model"],
            hf_token=api_key,
            temperature=config.get("temperature", 0.1),
            max_new_tokens=config.get("max_new_tokens", 8192),
            provider=config.get("provider", "nscale"),
        )
    if backend == "nvidia":
        # Same client, pointed at NVIDIA's endpoint with an NVIDIA key (no HF billing)
        return query_llm(
            prompt=prompt,
            model=config["model"],
            hf_token=api_key,
            temperature=config.get("temperature", 1.0),
            max_new_tokens=config.get("max_new_tokens", 32768),
            base_url=config["base_url"],
            top_p=config.get("top_p"),
            extra_body=config.get("extra_body"),
        )
    if backend == "anthropic":
        # Imported here so Hugging Face runs work without the anthropic package
        from src.utils.anthropic_client import query_claude

        return query_claude(
            prompt=prompt,
            model=config["model"],
            api_key=api_key,
            max_tokens=config.get("max_new_tokens", 64000),
            effort=config.get("effort", "high"),
        )
    raise ValueError(f"Unknown backend {backend!r} in config (expected 'huggingface', 'nvidia' or 'anthropic')")
