from PIL import Image
import os

def crop_and_stitch_sections(input_image_path, output_image_path):
    # Open the image
    img = Image.open(input_image_path)

    # Define static coordinates for cropping each section (adjust as needed)
    company_x_start = 240
    company_y_start = 447
    company_x_end = 960
    company_y_end = 547

    name_x_start = 240
    name_y_start = 540
    name_x_end = 960
    name_y_end = 640 

    category_x_start = 90
    category_y_start = 1080
    category_x_end = 1600
    category_y_end = 1250  

    Industry_x_start = 80
    Industry_y_start = 1250
    Industry_x_end = 1600
    Industry_y_end = 1325  

    interest_x_start = 90
    interest_y_start = 1310
    interest_x_end = 1630
    interest_y_end = 1990

    # Crop each section
    company_section = img.crop((company_x_start, company_y_start, company_x_end, company_y_end))
    name_section = img.crop((name_x_start, name_y_start, name_x_end, name_y_end))
    category_section = img.crop((category_x_start, category_y_start, category_x_end, category_y_end))
    Industry_section = img.crop((Industry_x_start, Industry_y_start, Industry_x_end, Industry_y_end))
    interest_section = img.crop((interest_x_start, interest_y_start, interest_x_end, interest_y_end))

    # Determine the size of the output image
    output_width = max(company_section.width, name_section.width, category_section.width, Industry_section.width, interest_section.width)
    output_height = company_section.height + name_section.height + category_section.height + Industry_section.height + interest_section.height

    # Create a new image with a white background
    output_img = Image.new("RGB", (output_width, output_height), (255, 255, 255))

    # Paste each section onto the output image
    output_img.paste(company_section, (0, 0))
    output_img.paste(name_section, (0, company_section.height))
    output_img.paste(category_section, (0, company_section.height + name_section.height))
    output_img.paste(Industry_section, (0, company_section.height + name_section.height + category_section.height))
    output_img.paste(interest_section, (0, company_section.height + name_section.height + category_section.height + Industry_section.height))

    # Save the stitched image
    output_img.save(output_image_path)

def process_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{filename[:-4]}_restitched.jpg")
            crop_and_stitch_sections(input_path, output_path)

if __name__ == "__main__":
    input_folder = r"C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr_raja\v0.2\dataset\trial\png_nodetection\half"
    output_folder = r"C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr_raja\v0.2\dataset\trial\png_nodetection\half_restitched"

    process_images(input_folder, output_folder)
