from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse


router = APIRouter(
    prefix='/download',
    tags=['Download']
)


BASE_DIR = Path(__file__).resolve().parent.parent

@router.get("/{filename}")
async def download_file(filename: str):
    safe_filename = Path(filename).name
    file_path = BASE_DIR / "output"/safe_filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"file {safe_filename} was not found in the output directory"
        )
    
    return FileResponse(
        path=file_path,
        filename=safe_filename,
        media_type='application/octet-stream'
    )