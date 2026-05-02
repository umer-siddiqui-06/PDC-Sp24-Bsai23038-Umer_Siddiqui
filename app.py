from fastapi import FastAPI
from models import LLMRequest, LLMResponse
from llm_service import call_llm
from circuit_breaker import CircuitBreaker

app = FastAPI()

# create circuit breaker instance
cb = CircuitBreaker(failure_threshold=2, recovery_timeout=10)

# -----------------------------
# REQUIRED HEADER (IMPORTANT)
# -----------------------------
@app.middleware("http")
async def add_student_id_header(request, call_next):
    response = await call_next(request)
    response.headers["X-Student-ID"] = "Bsai23038"
    return response


# -----------------------------
# FIXED ENDPOINT
# -----------------------------
@app.post("/generate", response_model=LLMResponse)
def generate(request: LLMRequest):
    try:
        result = cb.call(call_llm, request.prompt)
        return LLMResponse(response=result)

    except Exception as e:
        # fallback response
        return LLMResponse(
            response="⚠️ LLM unavailable. Returning fallback response."
        )