import shutil
import subprocess
from pathlib import Path


def excel_to_pdf(input_path: str, output_dir: str):
    if shutil.which("soffice") is None:
        raise RuntimeError(
            "LibreOffice 'soffice' is required for Excel/PDF conversion. Install LibreOffice and ensure it is on your PATH."
        )

    subprocess.run(
        [
            "soffice",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            output_dir,
            input_path,
        ],
        check=True,
    )

    output_file = Path(output_dir) / (Path(input_path).stem + ".pdf")
    return str(output_file)