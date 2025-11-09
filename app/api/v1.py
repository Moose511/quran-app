from fastapi import APIRouter

router = APIRouter()

# Simple sample data — replace later with real lookup
AYAT = [
    {"surah": 1, "ayah": 1, "text": "In the name of Allah, the Most Beneficent, the Most Merciful."},
    {"surah": 1, "ayah": 2, "text": "All praise is due to Allah, Lord of the Worlds."},
    {"surah": 1, "ayah": 3, "text": "The Most Beneficent, the Most Merciful."},
]

@router.get("/version")
def version():
    return {"version": "1.0.0"}

@router.get("/ayah/{surah}/{ayah}")
def get_ayah(surah: int, ayah: int):
 feature/request-logging
    # Placeholder – replace with real data later
    return {
        "surah": surah,
        "ayah": ayah,
        "text": "In the name of Allah..."
    }

    @router.get("/search")
def search(q: str) -> dict:
    results = [v for v in AYAT if q.lower() in v["text"].lower()]
    return {"results": results}

    return {"surah": surah, "ayah": ayah, "text": "In the name of Allah..."}
feature/request-logging

@router.get("/search")
def search(q: str) -> dict:
    results = [v for v in AYAT if q.lower() in v["text"].lower()]
    return {"results": results}

develop
 develop
