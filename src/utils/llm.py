"""One entry point for every model: picks the backend named in the config.

    config["backend"] == "huggingface"  ->  hf_client.query_llm  (e.g. Kimi K2.5)
    config["backend"] == "anthropic"    ->  anthropic_client.query_claude  (Claude)

Configs without "backend" (older notebooks) use Hugging Face, as before.
"""

from src.utils.hf_client import query_llm

def call_model(prompt: str, config: dict, api_key: str, dry_run: bool = False) -> dict:
    """Send one prompt with the settings in config; returns the query_llm dict shape.
    dry_run returns the mock reply for every backend: no key, no network, no cost.
    """
    if dry_run:
        return query_llm(prompt, config["model"], hf_token="", dry_run=True)

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
    raise ValueError(f"Unknown backend {backend!r} in config (expected 'huggingface' or 'anthropic')")
