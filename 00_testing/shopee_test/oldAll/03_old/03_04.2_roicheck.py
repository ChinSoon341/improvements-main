import cv2

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

# Example usage
image_pth = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\reorder\1_output\06_category_uncropped.jpg'
yolo_file_path = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\runs\detect\exp\labels\06_category_uncropped.txt'
x_axis_addition = 153
y_axis_addition = 12
output_path = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\reorder\1_output\06_category.jpg'

crop_image(image_pth, yolo_file_path, x_axis_addition, y_axis_addition, output_path)
