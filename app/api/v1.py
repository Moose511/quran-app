from fastapi import APIRouter

router = APIRouter()

@router.get("/ayah/{surah}/{ayah}")
def get_ayah(surah: int, ayah: int):
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
