from PIL import Image
import fitz

def image_to_pdf(inputFile: str, filename: str):
     
     doc = fitz.open()

     image = Image.open(inputFile)
     pdfbytes = image.convert_to_pdf()
     image.close()
     
     img_pdf = fitz.open('pdf', pdfbytes)
     doc.insert_pdf(img_pdf)
     img_pdf.close()

     doc.save(filename)
     doc.close()

     return filename

def jpg_to_png(inputFile: str, filename:str):
     
     image = Image.open(inputFile)

     image.save(filename)

     return filename

