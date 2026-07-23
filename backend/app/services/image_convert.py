from PIL import Image
import fitz
from pathlib import Path
import io


def image_to_pdf(input_file: str, output_file: str):
    image = Image.open(input_file)

    if image.mode != "RGB":
        image = image.convert("RGB")

    image.save(output_file, "PDF", resolution=100.0)
    image.close()

    return output_file


def jpg_to_png(input_file: str, output_file: str):
    image = Image.open(input_file)
    image.save(output_file, "PNG")
    image.close()

    return output_file

def pdf_to_jpg(input_file: str, output_dir: str):
    pdf = fitz.open(input_file)

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        pix = page.get_pixmap(dpi=300)

        image = Image.open(io.BytesIO(pix.tobytes("png")))

        output_file = output_dir / f"page_{page_num + 1}.jpg"
        image.convert("RGB").save(output_file, "JPEG", quality=95)

    pdf.close()

    return str(output_dir)