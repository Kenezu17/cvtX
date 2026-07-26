import shutil
import subprocess
from pathlib import Path



import os

# Use environment variable `SOFFICE_PATH` when provided, otherwise rely on `soffice` in PATH.
SOFFICE_PATH = os.environ.get("SOFFICE_PATH", "soffice")


def _convert_with_libreoffice(input_path: Path, output_path: Path):
    # If SOFFICE_PATH is an absolute path, validate it. If it's a binary name, assume it's in PATH.
    soffice_path_obj = Path(SOFFICE_PATH)
    if soffice_path_obj.is_absolute() and not soffice_path_obj.exists():
        raise RuntimeError(f"LibreOffice not found: {SOFFICE_PATH}")

    output_dir = output_path.parent
    subprocess.run(
        [
            SOFFICE_PATH,
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(output_dir),
            str(input_path),
        ],
        check=True,
    )

    converted_pdf = output_dir / (input_path.stem + ".pdf")
    if not converted_pdf.exists():
        raise RuntimeError("LibreOffice did not produce a PDF file for the DOCX conversion.")

    if converted_pdf != output_path:
        converted_pdf.replace(output_path)

    return str(output_path)


def docx_to_pdf(inputFile: str, outputFile: str):
    input_path = Path(inputFile)
    output_path = Path(outputFile)
    return _convert_with_libreoffice(input_path, output_path)




