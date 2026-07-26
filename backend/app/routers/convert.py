import os
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.services.pdf_convert import pdf_to_docx, pdf_to_excel, pdf_to_image
from app.services.docs_convert import docx_to_pdf
from app.services.image_convert import image_to_pdf, pdf_to_jpg
from app.services.execel import excel_to_pdf
from app.services.csv import csv_to_xl

from app.utils.zip_utils import zip_folder

router = APIRouter(prefix="/convert", tags=["Convert"])


BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "output"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


CONVERTER = {
    ('.pdf','docx'): pdf_to_docx,
    ('.pdf', 'png'): pdf_to_image,
    ('.pdf', 'jpg'): pdf_to_jpg,
    ('.pdf', 'xlsx'): pdf_to_excel,

    ('.docx','pdf'): docx_to_pdf,

    ('.jpg', 'pdf'): image_to_pdf,
    ('.jpeg','pdf'): image_to_pdf,
    ('.png', 'pdf'): image_to_pdf,

    ('.csv','xlsx'): csv_to_xl,
    ('.xlsx','pdf'): excel_to_pdf
}

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
        
        with open(source_path, 'wb') as f:
            f.write(content)
        
        suffix = source_path.suffix.lower()
        stem = source_path.stem
        
        key = (suffix, convert_to.lower())


        if key not in CONVERTER:
            raise HTTPException(
                status_code=400,
                detail=f'Conversion {suffix} - {convert_to} not supported'
            )
        converter =CONVERTER[key]
        
        if convert_to.lower() in ('png', 'jpg'):
            output = OUTPUT_DIR / stem

            converter(str(source_path), str(output))

            zip_path = OUTPUT_DIR / f'{stem}.zip'
            zip_folder(str(output), str(zip_path))

            output = zip_path
                       
        else:
            output = OUTPUT_DIR / f"{stem}.{convert_to}"
            converter(str(source_path), str(output))

       

    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Server process failure: {str(exc)}") from exc

    return {
        "filename": file.filename,
        "converted_filename": output.name,
        "download_url": f"/download/{output.name}",
        "status": "Converted and saved successfully",
    }
