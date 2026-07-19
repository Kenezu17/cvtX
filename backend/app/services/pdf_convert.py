import os

import fitz
from pdf2docx import Converter


def pdf_to_docx(inputFile: str, outputFile: str):
    cv = Converter(inputFile)
    cv.convert(outputFile)
    cv.close()

    return outputFile


def pdf_to_image(inputFile: str, outputFile: str):
    pdf = fitz.open(inputFile)
    zoom = 300 / 96
    matrix = fitz.Matrix(zoom, zoom)

    os.makedirs(outputFile, exist_ok=True)
    generate_files = []

    for page in pdf:
        file_name = f"page_{page.number + 1}.png"
        file_path = os.path.join(outputFile, file_name)

        pix = page.get_pixmap(matrix=matrix)
        pix.save(file_path)

        generate_files.append(file_path)

    pdf.close()

    return generate_files

