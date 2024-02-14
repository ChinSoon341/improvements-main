from pdf2image import convert_from_path
import os

def convert_pdf_to_images(pdf_path, saving_folder):
    try:
        pages = convert_from_path(pdf_path)
        
        if not os.path.exists(saving_folder):
            os.makedirs(saving_folder)
        
        for page_number, page in enumerate(pages, 1):
            img_name = f'img_{page_number}.jpg'
            img_path = os.path.join(saving_folder, img_name)
            page.save(img_path, "JPEG")
            print(f'Page {page_number} saved as {img_path}')
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_path = r'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\Day 1 (1st half).pdf'
    saving_folder = r'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\example'

    convert_pdf_to_images(pdf_path, saving_folder)
