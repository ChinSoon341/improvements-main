from PIL import Image
import os

def resize_and_fill_with_background(input_path, output_folder, output_file_name, target_size=(500.1, 500.1), fill_color=(0, 0, 0)):
    # Convert output_folder_number to a string
    output_folder_str = str(output_folder)

    # Ensure the output folder exists
    os.makedirs(output_folder_str, exist_ok=True)

    # Check if the input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file not found - {input_path}")
        return

    # Open the image
    img = Image.open(input_path)

    # Set a default DPI value or handle it as needed
    default_dpi = 72  # You can adjust this value if needed

    # Resize the image to the target size and fill the remaining space with a black background
    resized_img = Image.new("RGB", (int(target_size[0] * default_dpi / 25.4), int(target_size[1] * default_dpi / 25.4)), fill_color)
    resized_img.paste(img, ((resized_img.width - img.width) // 2, (resized_img.height - img.height) // 2))

    # Save the resized image to the output folder with the specified file name
    output_path = os.path.join(output_folder_str, output_file_name)
    resized_img.save(output_path)
    print(f"Saved: {output_path}")

# Specify the folder location
folder_location = r'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output'

# Dynamically get the number of folders
num_folders = len([name for name in os.listdir(folder_location) if os.path.isdir(os.path.join(folder_location, name))])

for output_folder_number in range(1, num_folders + 1):
    input_path_1 = rf'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output\{output_folder_number}_output\06_category.jpg'
    input_path_2 = rf'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output\{output_folder_number}_output\09_product.jpg'

    # Output paths for resized images
    output_path_1 = rf'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output\{output_folder_number}_output\06_category_resized.jpg'
    output_path_2 = rf'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output\{output_folder_number}_output\09_product_resized.jpg'

    # Resize and fill with a black background for '06_category.jpg'
    resize_and_fill_with_background(input_path_1, output_path_1, '06_category_resized.jpg')

    # Resize and fill with a black background for '09_product.jpg'
    resize_and_fill_with_background(input_path_2, output_path_2, '09_product_resized.jpg')
