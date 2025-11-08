from fastapi import APIRouter
router = APIRouter()

@router.get("/version")
def version():
    return {"version": "1.0.0"}

@router.get("/ayah/{surah}/{ayah}")
def get_ayah(surah: int, ayah: int):
    return {"surah": surah, "ayah": ayah, "text": "In the name of Allah..."}
