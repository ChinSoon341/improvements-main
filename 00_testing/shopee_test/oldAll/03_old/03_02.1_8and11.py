from PIL import Image
import os

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
    input_image_path = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\jpg\img_14.jpg'

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
