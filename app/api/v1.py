from fastapi import APIRouter

router = APIRouter()

# Sample data for simple search; replace with real data later if you want
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
    # placeholder; swap with your real logic later
    return {"surah": surah, "ayah": ayah, "text": "In the name of Allah..."}

@router.get("/search")
def search(q: str) -> dict:
    """Case-insensitive substring search over AYAT."""
    results = [v for v in AYAT if q.lower() in v["text"].lower()]
    return {"results": results}
