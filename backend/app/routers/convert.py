import logging
import uuid
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from starlette.concurrency import run_in_threadpool

from app.services.pdf_convert import pdf_to_docx, pdf_to_image
from app.services.docs_convert import docx_to_pdf
from app.services.image_convert import image_to_pdf, jpg_to_png
from app.services.execel import excel_to_pdf
from app.services.csv import csv_to_xl

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/convert", tags=["Convert"])

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "output"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MAX_UPLOAD_BYTES = 25 * 1024 * 1024  # 25 MB

CONVERTER = {
    ('.pdf', 'docx'): pdf_to_docx,
    ('.pdf', 'png'): pdf_to_image,

    ('.docx', 'pdf'): docx_to_pdf,

    ('.jpg', 'pdf'): image_to_pdf,
    ('.jpeg', 'pdf'): image_to_pdf,
    ('.png', 'pdf'): image_to_pdf,

    ('.csv', 'xlsx'): csv_to_xl,

    ('.xlsx', 'pdf'): excel_to_pdf,
}


@router.post("/")
async def convert_file(
    file: UploadFile = File(...),
    convert_to: str = Form(...),
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file name provided")

    original_name = Path(file.filename).name
    suffix = Path(original_name).suffix.lower()
    stem = Path(original_name).stem
    target_format = convert_to.lower().lstrip(".")

    key = (suffix, target_format)
    if key not in CONVERTER:
        raise HTTPException(
            status_code=400,
            detail=f"Conversion {suffix} -> {target_format} not supported",
        )

    content = await file.read()
    if len(content) > MAX_UPLOAD_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"File exceeds max upload size of {MAX_UPLOAD_BYTES // (1024*1024)} MB",
        )
    if not content:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")

    # Namespace every request so concurrent uploads never collide and
    # download URLs aren't guessable from the original filename alone.
    request_id = uuid.uuid4().hex
    source_path = UPLOAD_DIR / f"{request_id}_{original_name}"

    with open(source_path, "wb") as f:
        f.write(content)

    if target_format == "png":
        output_name = f"{request_id}_{stem}"
    else:
        output_name = f"{request_id}_{stem}.{target_format}"
    output_path = OUTPUT_DIR / output_name

    converter = CONVERTER[key]

    try:
        await run_in_threadpool(converter, str(source_path), str(output_path))
    except FileNotFoundError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except RuntimeError as exc:
        logger.exception("Conversion failed for %s -> %s", source_path, target_format)
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    except Exception as exc:
        logger.exception("Unexpected error converting %s -> %s", source_path, target_format)
        raise HTTPException(
            status_code=500, detail=f"Server process failure: {exc}"
        ) from exc
    finally:
        source_path.unlink(missing_ok=True)

    if not output_path.exists():
        raise HTTPException(
            status_code=502,
            detail="Conversion did not produce an output file",
        )

    return {
        "filename": original_name,
        "converted_filename": output_path.name,
        "download_url": f"/download/{output_path.name}",
        "status": "Converted and saved successfully",
    }