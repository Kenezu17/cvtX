from pathlib import Path
from fastapi import APIRouter, HTTPException,BackgroundTasks
from fastapi.responses import FileResponse
import shutil

router = APIRouter(
    prefix="/download",
    tags=["Download"],
)

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
UPLOAD_DIR = BASE_DIR / "uploads"


def delete_file(folder: Path):
   if not folder.exists():
       raise HTTPException(status_code=404, detail=f'the {folder} not found')
   try:
       for file in folder.iterdir():
           if file.is_file():
               file.unlink()
               print(f'Successful clean the {folder}')
           elif file.is_dir():
               shutil.rmtree(file)
               print(f'delete folder {folder}')

   except Exception as e:
       raise HTTPException (status_code=500 , detail=f'Failed to delete files {str(e)}')
       

   
@router.get("/{filename}")
async def download_file(filename: str, backgound_task: BackgroundTasks):
    safe_filename = Path(filename).name
    file_path = OUTPUT_DIR / safe_filename

    backgound_task.add_task(delete_file, OUTPUT_DIR)
    backgound_task.add_task(delete_file, UPLOAD_DIR)

    try:
        file_path.resolve().relative_to(OUTPUT_DIR.resolve())
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid filename")

    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(
            status_code=404,
            detail=f"file {safe_filename} was not found in the output directory",
        )

    return FileResponse(
        path=file_path,
        filename=safe_filename,
        media_type="application/octet-stream",
    )