from fastapi import FastAPI, Request
from app.api.v1 import router as v1_router
import time, logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Quran App")

@app.middleware("http")
async def log_timing(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    dur_ms = int((time.time() - start) * 1000)
    logging.info("%s %s -> %d (%d ms)", request.method, request.url.path, response.status_code, dur_ms)
    return response

@app.get("/healthz")
async def healthz():
    return {"ok": True}

app.include_router(v1_router, prefix="/api/v1")
