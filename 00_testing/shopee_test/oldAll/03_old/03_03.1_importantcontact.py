import subprocess
import os

def run_detection(image_path, weights_path, img_size, confidence_threshold, save_txt, exist_ok, output_result_path):
    # Replace the command with your desired one
    command = [
        'python', 'C:/Users/chinsoont.BECKHOFF/OneDrive - Singapore Polytechnic/improvements/03_ocr/v1.0/yolov5/yolov5-master/detect.py',
        '--weights', weights_path,
        '--img-size', str(img_size),
        '--conf', str(confidence_threshold),
        '--source', image_path,
        '--save-txt' if save_txt else '',
        '--exist-ok' if exist_ok else '',
        '--project', r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\runs\detect\exp\importantcontact'
    ]

    # Run the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Common parameters
img_size = 640
confidence_threshold = 0.7
save_txt = True
exist_ok = True

# Specify the folder location
folder_location = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\reorder'

# Dynamically get the number of folders
num_folders = len([name for name in os.listdir(folder_location) if os.path.isdir(os.path.join(folder_location, name))])

for output_folder_number in range(1, num_folders + 1):
    image_path_1 = rf'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\reorder\{output_folder_number}_output\12_importantContact_uncropped.jpg'
    weights_path_1 = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\runs\train\desktop_trained_model\weights\best.pt'
    output_result_path_1 = rf'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\runs\detect\exp\importantcontact'

    # Run detection
    run_detection(image_path_1, weights_path_1, img_size, confidence_threshold, save_txt, exist_ok, output_result_path_1)

    # Check the result
    result_file_path = os.path.join(output_result_path_1, 'labels', f'{os.path.basename(image_path_1)[:-4]}.txt')

    # Process the result
    if os.path.exists(result_file_path):
        with open(result_file_path, 'r') as result_file:
            content = result_file.read().strip()
        
        # Create a file based on the checkbox status
        output_status_file_path = rf'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\reorder\{output_folder_number}_output\checkbox_status.txt'
        with open(output_status_file_path, 'w') as status_file:
            if content:
                status_file.write('Yes')
            else:
                status_file.write('No')

        print(f"Checkbox status saved: {output_status_file_path}")
