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

if __name__ == "__main__":
    # Specify the input image path
    input_image_path = r"C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\jpg\img_14.jpg"

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

    (267,1684,1599,1854),
    (283,1868,1605,1966),
    (263,2133,613,2216)
]
    output_file_names = [
    "01_lead_number.jpg",
    "02_company.jpg",
    "03_name.jpg",
    "04_counPhoneEmail.jpg",
    "05_nameCards.jpg",
    "06_category.jpg",
    "07_industry.jpg",
    #03_02.1_reorderInterest.py cover 8 (interest- 3 fields)
    "09_product.jpg",
    "10_media.jpg",
    #03_02.1_reorderInterest.py cover 11 (preparedBy - 2 fields)
    "12_importantContact.jpg"
]

for i, (crop_region, output_file_name) in enumerate(zip(crop_regions, output_file_names), 1):
    crop_and_save(input_image_path, output_folder, crop_region, output_file_name)

