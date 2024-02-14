from PIL import Image

def crop_name_section(input_image_path, output_image_path):
    # Open the image
    img = Image.open(input_image_path)

    interest_full_x_start = 70
    interest_full_y_start = 1050
    interest_full_x_end = 1650
    interest_full_y_end = 1700

    interest_full_section = img.crop((interest_full_x_start, interest_full_y_start, interest_full_x_end, interest_full_y_end))

    # Save the cropped image
    interest_full_section.save(output_image_path)

if __name__ == "__main__":
    input_path = r"C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr_raja\v0.2\dataset\trial\png_nodetection\full\img_14.jpg"
    output_path = r"C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr_raja\v0.2\dataset\trial\png_nodetection\full\individual\img_1_reorder_interest_full.jpg"

    crop_name_section(input_path, output_path)
