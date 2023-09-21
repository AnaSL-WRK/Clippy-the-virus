import importlib
import multiprocessing
import subprocess
import time
import os
        

def run_vbscript(vbscript_filename):
    try:
        subprocess.run(["cscript.exe", vbscript_filename], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {vbscript_filename}: {e}")
        
        
def run_script(script_name, arg1):
    try:
        module = importlib.import_module(script_name)
        # Assuming there's a function named 'main' in your script to run
        module.main(arg1)
        
    except ImportError:
        print(f"Failed to import {script_name}")





def main():
    scripts_to_run = ["gif", "change_desk"]

    processes = []

    
    
    for i in range(60):
        process = multiprocessing.Process(target=run_vbscript, args=("popup.vbs",))
        process.start() 
        i+=1 
    
    time.sleep(60)
    os.system("taskkill /f /im  cscript.exe")
    
    
    
    #time.sleep(5)
    for process in processes:
        process.join()
        
        
