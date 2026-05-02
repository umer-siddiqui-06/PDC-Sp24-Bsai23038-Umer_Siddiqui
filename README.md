Umer Siddiqui — BS-AI-23038

PDC Assignment: Building Resilient Distributed Systems

Project Overview

This project demonstrates a distributed system simulation using FastAPI where an external LLM service is unreliable and slow. The system shows:

- Request failures due to external API instability
- Blocking behavior in synchronous LLM calls
- Circuit Breaker pattern for resilience
- Comparison between failure and improved system behavior

Project Structure

main.py              → Phase 1 (Broken system - no circuit breaker)
app.py               → Phase 2 (Fixed system with circuit breaker)
llm_service.py      → Simulated unreliable external LLM API
models.py           → Request / Response schemas
circuit_breaker.py  → Circuit Breaker implementation
test_fail.py        → Concurrent test (failure scenario)
test_success.py     → Concurrent test (fixed system)
requirements.txt    → Dependencies

Requirements

pip install -r requirements.txt


How to Run the Project

1. Phase 1 (Broken System)

Start server:
uvicorn main:app --reload

Run test:
python test_fail.py

This demonstrates:
- Blocking behavior
- Random LLM failures
- Slow response system
- No recovery mechanism


2. Phase 2 (Fixed System with Circuit Breaker)

Start server:
uvicorn app:app --reload

Run test:
python test_success.py

This demonstrates:
- Circuit breaker activation
- Fallback responses
- Improved system resilience


Testing Behavior

Failure Scenario (Phase 1)
- Random LLM failures occur
- Requests are slow due to blocking sleep
- No recovery mechanism exists

Fixed Scenario (Phase 2)
- Circuit breaker detects repeated failures
- System stops calling failing LLM
- Fallback response is returned instantly