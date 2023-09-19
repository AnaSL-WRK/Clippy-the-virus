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
        
        
        
def run_script(script_name):
    try:
        module = importlib.import_module(script_name)
        # Assuming there's a function named 'main' in your script to run
        #module.main()
    except ImportError:
        print(f"Failed to import {script_name}")

if __name__ == "__main__":
    scripts_to_run = ["gif", "change_desk"]

    processes = []
   #for i in range(5):
   #    process = multiprocessing.Process(target=run_script, args=("gif",))
   #    processes.append(process)
   #    time.sleep(0.5)
   #    process.start()
        
    #for script_name in scripts_to_run:
    #    process = multiprocessing.Process(target=run_script, args=(script_name,))
    #    processes.append(process)
    #    process.start()
    
    
    process = multiprocessing.Process(target=run_script, args=("change_desk",))
    processes.append(process)
    process.start()
    
    #time.sleep(5)

    process = multiprocessing.Process(target=run_vbscript, args=("sound.vbs",))
    processes.append(process)
    process.start()
    
    
    for process in processes:
        process.join()