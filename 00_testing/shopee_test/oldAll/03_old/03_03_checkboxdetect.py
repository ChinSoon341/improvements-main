import subprocess
import cv2

def run_detection(image_path, weights_path, img_size, confidence_threshold, save_txt, exist_ok):
    # Replace the command with your desired one
    command = [
        'python', r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\detect.py',
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
    image_path = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\reorder\1_output\06_category_uncropped.jpg'
    weights_path = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\runs\train\desktop_trained_model\weights\best.pt'
    img_size = 640
    confidence_threshold = 0.7
    save_txt = True
    exist_ok = True
    x_axis_addition = 233
    y_axis_addition = 12
    yolo_file_path = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\runs\detect\exp\labels\06_category_uncropped.txt'
    output_path = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\reorder\1_output\06_category.jpg'

    run_detection(image_path, weights_path, img_size, confidence_threshold, save_txt, exist_ok)
    crop_image(image_path, yolo_file_path, x_axis_addition, y_axis_addition, output_path)
