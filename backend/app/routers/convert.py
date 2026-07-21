import os
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

router = APIRouter(prefix="/convert", tags=["Convert"])

# Resolve the absolute path to the backend directory root
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "output"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
print('hello')



@router.post("/")
async def convert_file(
    file: UploadFile = File(...),
    convert_to: str = Form(...),
):
    try:
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file name provided")

        content = await file.read()
        source_path = UPLOAD_DIR / Path(file.filename).name
        source_path.write_bytes(content)

        file_stem = Path(file.filename).stem
        target_filename = f"{file_stem}.{convert_to}"
        output_path = OUTPUT_DIR / target_filename
        output_path.write_bytes(content)

    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Server process failure: {str(exc)}") from exc

    return {
        "filename": file.filename,
        "converted_filename": target_filename,
        "download_url": f"/download/{target_filename}",
        "content_type": file.content_type,
        "convert": convert_to,
        "status": "Converted and saved successfully",
    }
