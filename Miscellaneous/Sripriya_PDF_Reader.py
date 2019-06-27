import glob
import os
import pdf2image
import pytesseract


PDF_DIR = '/Users/akshaylaradhaya/Documents/Priya PDFs/*/*'
OUT_DIR = '/Users/akshaylaradhaya/Documents/Priya PDFs/cropped'

pdf_files = glob.glob(PDF_DIR)
pdf_files.sort()

print(len(pdf_files))

for pdf_file in pdf_files[:5]:
    try:
        pdf_name, _ = pdf_file.split('.')
        file_path = os.path.join(PDF_DIR, pdf_file)
        img_path = os.path.join(OUT_DIR, pdf_name + '.png')
        img = pdf2image.convert_from_path(file_path, dpi=300, first_page=1, last_page=1)[0]
        width, height = img.size
        newheight = int(height * 2000 / width)
        img = img.resize((2000, newheight))

        area = (200, 400, 1800, 1800)
        cropped_img = img.crop(area)

        text = pytesseract.image_to_string(cropped_img)

        print(text, "\n-----\n")

        cropped_img.save(img_path, 'PNG')
        print("Saved", pdf_file)
    except Exception as e:
        print(str(e))
        print("Failed", pdf_file)
