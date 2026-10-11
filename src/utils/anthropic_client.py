"""Anthropic API wrapper (Claude models).

Returns the same dict shape as hf_client.query_llm, plus:
  - stop_reason:  why the model stopped. "end_turn" = finished normally,
                  "max_tokens" = cut off at the length limit,
                  "refusal" = declined (a safety check or the model itself)
  - stop_details: for a refusal, its category (may be None)
  - model_served: the model that actually answered

A refusal is NOT an exception: the API answers normally with stop_reason "refusal".
The caller must check stop_reason before using generated_text (run_1a does).
No automatic fallback to another model: one run = one model.
"""

import time

import anthropic


def query_claude(
    prompt: str,
    model: str,
    api_key: str,
    max_tokens: int = 64000,
    effort: str = "high",
) -> dict:
    """Send one prompt to a Claude model and return its full answer.

    Args:
        prompt: The full prompt string to send.
        model: Claude model ID (e.g. "claude-opus-5-5").
        api_key: Anthropic API key.
        max_tokens: Limit for thinking + answer together.
        effort: How much the model thinks: low / medium / high / xhigh / max.

    Raises:
        anthropic.APIError subclasses (auth, bad request, ...) after the SDK's own
        retries of rate limits (429) and server errors (5xx).
    """
    # max_retries: the SDK retries 408/409/429/5xx and connection errors with backoff
    client = anthropic.Anthropic(api_key=api_key, max_retries=4)

    start = time.time()
    events = 0
    # Streaming: one paper can take minutes; streaming avoids HTTP timeouts.
    # No temperature (rejected by these models) and no thinking setting
    # (adaptive thinking is the default and the only option on Opus 5.5).
    with client.messages.stream(
        model=model,
        max_tokens=max_tokens,
        output_config={"effort": effort},
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for _ in stream:
            events += 1
            # A dot every 200 events so long runs don't look frozen
            if events % 200 == 0:
                print(".", end="", flush=True)
        message = stream.get_final_message()
        request_id = stream.request_id  # quote this id if you ever ask Anthropic about a call
    latency = time.time() - start
    if events >= 200:
        print()

    raw = message.to_dict()
    return {
        "generated_text": "".join(block.text for block in message.content if block.type == "text"),
        "stop_reason": message.stop_reason,
        "stop_details": raw.get("stop_details"),
        "model_served": message.model,
        "usage": {
            "prompt_tokens": message.usage.input_tokens,
            "completion_tokens": message.usage.output_tokens,  # includes thinking tokens
        },
        # Full reply (text, empty thinking blocks, usage) and request id, for auditing
        "raw_response": {"request_id": request_id, "message": raw},
        "latency_seconds": round(latency, 2),
    }
