from fastapi import FastAPI, HTTPException
from models import LLMRequest, LLMResponse
from llm_service import call_llm

app = FastAPI()

# -----------------------------
# REQUIRED HEADER 
# -----------------------------
@app.middleware("http")
async def add_student_id_header(request, call_next):
    response = await call_next(request)
    response.headers["X-Student-ID"] = "Bsai23038"
    return response



@app.post("/generate", response_model=LLMResponse)
def generate(request: LLMRequest):
    try:
        #  DIRECT BLOCKING CALL (PROBLEM)
        result = call_llm(request.prompt)
        return LLMResponse(response=result)

    except Exception as e:
        #  naive error handling (still bad design)
        raise HTTPException(status_code=500, detail=str(e))