import time
import random

def call_llm(prompt: str) -> str:
    """
    Simulated external LLM API that is unreliable and slow.
    This represents a real-world external dependency.
    """

    # simulate network latency (BAD BEHAVIOR)
    time.sleep(5)  # change to 60 for stronger demo if needed

    # simulate random failure
    if random.random() < 0.3:
        raise Exception("LLM API failed due to timeout or server error")

    return f"LLM RESPONSE FOR: {prompt}"