from pathlib import Path
from docx2pdf import convert




def docx_to_pdf(inputFile: str, outputFile: str):
    input = Path(inputFile)
    output = Path(outputFile)

    convert(str(input), str(output))

    return outputFile




