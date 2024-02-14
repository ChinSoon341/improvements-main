from PIL import Image, ImageDraw
import os

def crop_and_save_with_background(input_path, output_folder, crop_region, output_file_name, add_background=False):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Open the image
    img = Image.open(input_path)

    # Crop the specified region
    left, upper, right, lower = crop_region
    cropped_img = img.crop((left, upper, right, lower))

    if add_background:
        # Create an A7-sized black background
        background = Image.new("RGB", (880, 308), (0, 0, 0))

        # Paste the cropped image onto the black background
        background.paste(cropped_img, (0, 0))
        cropped_img = background

    # Save the image to the output folder with the specified file name
    output_path = os.path.join(output_folder, output_file_name)
    cropped_img.save(output_path)

def crop_and_stitch_sections(input_image_path, output_image_path, x_start, y_start, x_end, y_end):
    # Open the image
    img = Image.open(input_image_path)

    # Initialize variables for output dimensions
    output_width = max(x_end)
    output_height = sum([end - start for start, end in zip(y_start, y_end)])

    # Create a new image with a white background
    output_img = Image.new("RGB", (output_width, output_height), (255, 255, 255))

    # Paste each section onto the output image
    y_offset = 0
    for start_x, start_y, end_x, end_y in zip(x_start, y_start, x_end, y_end):
        section = img.crop((start_x, start_y, end_x, end_y))
        output_img.paste(section, (0, y_offset))
        y_offset += section.height

    # Save the stitched image
    output_img.save(output_image_path)

if __name__ == "__main__":
    # Specify the input folder path
    input_folder = r'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\forms'

    # Specify the output parent folder path
    output_parent_folder = r'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output'

    # Specify crop regions and output file names
    crop_regions = [
        (276, 212, 1193, 260),
        (438, 248, 1193, 341),
        (281, 520, 1601, 766),
        (952, 0, 1623, 779),
        (0, 785, 1640, 961),
        (258,969, 814,1033), 
        (267, 1684, 1599, 1854),
        (283, 1868, 1605, 1966),
        (263, 2133, 613, 2216)
    ]

    output_file_names = [
        "02_company.jpg",
        "03_name.jpg",
        "04_counPhoneEmail.jpg",
        "05_nameCards.jpg",
        "06_category_uncropped.jpg",
        "07_industry.jpg",
        "09_product_uncropped.jpg",
        "10_media.jpg",
        "12_importantContact_uncropped.jpg"
    ]

    # Loop through all images in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_image_path = os.path.join(input_folder, file_name)

            # Create a unique output folder for each image
            image_number = file_name.split('_')[-1].split('.')[0]
            output_folder = os.path.join(output_parent_folder, f'{image_number}_output')
            
            for i, (crop_region, output_file_name) in enumerate(zip(crop_regions, output_file_names), 1):
                add_background = output_file_name in [ "02_company.jpg"]
                crop_and_save_with_background(input_image_path, output_folder, crop_region, output_file_name, add_background)

            # Case-specific cropping and stitching (you may add more cases as needed)
            x_start1 = [287, 285, 289]
            y_start1 = [1092, 1288, 1516]
            x_end1 = [1601, 1601, 1584]
            y_end1 = [1241, 1464, 1704]
            output_image_path1 = os.path.join(output_folder, '08_interest.jpg')
            crop_and_stitch_sections(input_image_path, output_image_path1, x_start1, y_start1, x_end1, y_end1)


