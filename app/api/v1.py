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
