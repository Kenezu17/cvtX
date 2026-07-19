import os
import shutil
import subprocess


def docx_to_pdf(inputFile: str, outDir: str):
    if shutil.which("soffice") is None:
        raise RuntimeError(
            "LibreOffice 'soffice' is required for DOCX/PDF conversion. Install LibreOffice and ensure it is on your PATH."
        )

    os.makedirs(outDir, exist_ok=True)

    subprocess.run(
        [
            "soffice",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            outDir,
            inputFile,
        ],
        check=True,
    )

    base_name = os.path.basename(inputFile)
    file_name_only = os.path.splitext(base_name)[0]
    expected_pdf_path = os.path.join(outDir, f"{file_name_only}.pdf")

    return expected_pdf_path