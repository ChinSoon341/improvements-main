from PIL import Image
import os

def crop_and_save(input_path, output_folder, crop_region, output_file_name):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Open the image
    img = Image.open(input_path)

    # Crop the specified region
    left, upper, right, lower = crop_region
    cropped_img = img.crop((left, upper, right, lower))

    # Save the cropped image to the output folder with the specified file name
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
    # Specify the input image path
    input_image_path = r"C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\jpg\img_10.jpg"

    # Specify the output folder path
    output_folder = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\reorder'

    crop_regions = [
        (1, 2, 258, 51),
        (408, 160, 1193, 255),
        (438, 248, 1193, 341),
        (281, 520, 1601, 766),
        (952, 0, 1623, 779),
        (0, 785, 1640, 961),
        (76, 971, 805, 1036),
        (267, 1684, 1599, 1854),
        (283, 1868, 1605, 1966),
        (263, 2133, 613, 2216)
    ]

    output_file_names = [
        "01_lead_number.jpg",
        "02_company.jpg",
        "03_name.jpg",
        "04_counPhoneEmail.jpg",
        "05_nameCards.jpg",
        "06_category.jpg",
        "07_industry.jpg",
        "09_product.jpg",
        "10_media.jpg",
        "12_importantContact.jpg"
    ]

    for i, (crop_region, output_file_name) in enumerate(zip(crop_regions, output_file_names), 1):
        crop_and_save(input_image_path, output_folder, crop_region, output_file_name)

    # Case 1
    x_start1 = [287, 285, 289]
    y_start1 = [1092, 1288, 1516]
    x_end1 = [1601, 1601, 1584]
    y_end1 = [1241, 1464, 1704]
    output_image_path1 = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\reorder\08_interest.jpg'
    crop_and_stitch_sections(input_image_path, output_image_path1, x_start1, y_start1, x_end1, y_end1)

    # Case 2
    x_start2 = [814, 1028]
    y_start2 = [2004, 2115]
    x_end2 = [1601, 1599]
    y_end2 = [2101, 2256]
    output_image_path2 = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\reorder\11_preparedBy.jpg'
    crop_and_stitch_sections(input_image_path, output_image_path2, x_start2, y_start2, x_end2, y_end2)
