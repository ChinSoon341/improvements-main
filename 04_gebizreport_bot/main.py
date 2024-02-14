import subprocess
import os

def run_script(script_name):
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    print(f"Running {script_name}")
    subprocess.run(["python", script_path])

if __name__ == "__main__":
    run_script("04_01_geBIZwebS.py")
    run_script("04_02_excelCreationFlag")
    run_script("04_02.1_flagInvalid")
    run_script("04_02.2_flagMultiSup&main")
    

