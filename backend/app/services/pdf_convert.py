import os
import pdfplumber
import pandas as pd
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


def pdf_to_excel(inputFile: str, output_file: str):

    table_found = False

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        with pdfplumber.open(inputFile) as pdf:
            sheet = 1

            for page in pdf.pages:
                tables = page.extract_tables()  

              

                for table in tables:
                    if table and len(table) > 1:
                        table_found = True  # <-- Mark that a table was found

                        df = pd.DataFrame(table[1:], columns=table[0])
                        df.to_excel(
                            writer,
                            sheet_name=f"Table{sheet}",
                            index=False,
                        )
                        sheet += 1

                if not tables:
                 raise ValueError("Doesnt have a table!" )
                 break

    if not table_found:
        raise ValueError("No tables were found in the PDF. Conversion aborted.")

    return output_file