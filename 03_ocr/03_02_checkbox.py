import cv2,os,subprocess
from PIL import Image
import os

def run_detection(image_path, weights_path, img_size, confidence_threshold, save_txt, exist_ok):
    # Replace the command with your desired one
    command = [
        'python', r'C:\Users\ADAM7\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\detect.py',
        '--weights', weights_path,
        '--img-size', str(img_size),
        '--conf', str(confidence_threshold),
        '--source', image_path,
        '--save-txt' if save_txt else '',
        '--exist-ok' if exist_ok else ''
    ]

    # Run the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def crop_image(image_path, yolo_file_path, x_axis_addition, y_axis_addition, output_path):
    # Read the YOLO format file
    with open(yolo_file_path, 'r') as file:
        lines = file.readlines()

    # Extract coordinates from the YOLO format
    for line in lines:
        data = line.split()
        if len(data) == 5:  # YOLO format should have 5 values (class, x_center, y_center, width, height)
            x_center, y_center, width, height = map(float, data[1:])
            
            # Calculate coordinates with additions
            x = int((x_center * cv2.imread(image_path).shape[1]) + x_axis_addition)
            y = int((y_center * cv2.imread(image_path).shape[0]) + y_axis_addition)

            # Perform the cropping
            cropped_image = cv2.imread(image_path)

            # Define the cropping boundaries based on the original image size
            x1 = max(0, x - int(width * cv2.imread(image_path).shape[1] / 2) - x_axis_addition)
            y1 = max(0, y - int(height * cv2.imread(image_path).shape[0] / 2) - y_axis_addition)
            x2 = min(cv2.imread(image_path).shape[1], x + int(width * cv2.imread(image_path).shape[1] / 2) + x_axis_addition)
            y2 = min(cv2.imread(image_path).shape[0], y + int(height * cv2.imread(image_path).shape[0] / 2) + y_axis_addition)

            # Crop the image based on the calculated coordinates
            cropped_image = cropped_image[y1:y2, x1:x2]

            # Save the cropped image at the specified output path
            cv2.imwrite(output_path, cropped_image)

if __name__ == "__main__":
    # Common parameters
    img_size = 640
    confidence_threshold = 0.7
    save_txt = True
    exist_ok = True
    x_axis_addition = 233
    y_axis_addition = 12

    # Specify the folder location
    folder_location = r'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output'

    # Dynamically get the number of folders
    num_folders = len([name for name in os.listdir(folder_location) if os.path.isdir(os.path.join(folder_location, name))])


    for output_folder_number in range(1, num_folders + 1):
        image_path_1 = rf'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output\{output_folder_number}_output\06_category_uncropped.jpg'
        weights_path_1 = r'C:\Users\ADAM7\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\runs\train\checkbox_detection_3000epoch_model\weights\best.pt'
        yolo_file_path_1 = rf'C:\Users\ADAM7\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\runs\detect\exp\labels\06_category_uncropped.txt'
        output_path_1 = rf'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output\{output_folder_number}_output\06_category.jpg'

        image_path_2 = rf'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output\{output_folder_number}_output\09_product_uncropped.jpg'
        weights_path_2 = r'C:\Users\ADAM7\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\runs\train\checkbox_detection_3000epoch_model\weights\best.pt'
        yolo_file_path_2 = rf'C:\Users\ADAM7\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\runs\detect\exp\labels\09_product_uncropped.txt'
        output_path_2 = rf'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output\{output_folder_number}_output\09_product.jpg'

        run_detection(image_path_1, weights_path_1, img_size, confidence_threshold, save_txt, exist_ok)
        crop_image(image_path_1, yolo_file_path_1, x_axis_addition, y_axis_addition, output_path_1)

        run_detection(image_path_2, weights_path_2, img_size, confidence_threshold, save_txt, exist_ok)
        crop_image(image_path_2, yolo_file_path_2, x_axis_addition, y_axis_addition, output_path_2)

#masking
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
    output_path_1 = rf'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output\{output_folder_number}_output'
    output_path_2 = rf'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\output\{output_folder_number}_output'

    # Resize and fill with a black background for '06_category.jpg'
    resize_and_fill_with_background(input_path_1, output_path_1, '06_category.jpg')

    # Resize and fill with a black background for '09_product.jpg'
    resize_and_fill_with_background(input_path_2, output_path_2, '09_product.jpg')