import img2pdf
from PIL import Image
import os


def convert():
    input_dir = "./input"
    output_path = "./output"
    for file_name in os.listdir(input_dir):
        image = Image.open(f"{input_dir}/{file_name}")
        pdf_bytes = img2pdf.convert(image.filename)
        filename = str(image.filename)[(str(image.filename).rfind("/")) + 1::]
        filename = filename[:filename.rfind("."):]
        file = open(f"{output_path}/{filename}.pdf", "wb")
        file.write(pdf_bytes)
        image.close()
        file.close()


if __name__ == '__main__':
    convert()
