from fastapi import FastAPI
from app.api.v1 import router as v1_router

app = FastAPI(title="Quran App")

@app.get("/healthz")
def health():
    return {"ok": True}

app.include_router(v1_router, prefix="/api/v1")
