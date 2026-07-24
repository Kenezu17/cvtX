import shutil
import subprocess
from pathlib import Path

SOFFICE_PATH = SOFFICE_PATH = r"C:\Program Files\LibreOffice\program\soffice.exe"

def convert_with_libreoffice(inputPath: str, outputPath: str):
    if not Path(SOFFICE_PATH).exists():
        raise RuntimeError(
            f"LibreOffice not found: {SOFFICE_PATH}"
        )

    output_dir = outputPath.parent

    subprocess.run(
        [
            SOFFICE_PATH,
            '--headless',
            '--convert-to',
            'pdf',
            '--outdir',
            str(output_dir),
            str(inputPath),
        ],
        check=True,
    )

    convert_pdf = output_dir / (inputPath.stem + '.pdf')
    if not convert_pdf.exists():
        raise RuntimeError(
            "LibreOffice did not produce a PDF file for the DOCX conversion."
        )

    if not convert_pdf != output_dir:
        convert_pdf.replace(outputPath)

    return str(outputPath)


def excel_to_pdf(inputFile: str, outputFile: str):
    input_path = Path(inputFile)
    output_path = Path(outputFile)

    return convert_with_libreoffice(input_path, output_path)


