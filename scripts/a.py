import importlib
import multiprocessing
import subprocess
import time
import os
import pynput
import pygetwindow as gw
from pynput.keyboard import Key, Controller



def run_vbscript(vbscript_filename):
    try:
        subprocess.run(["cscript.exe", vbscript_filename], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {vbscript_filename}: {e}")
        
        
def run_powershell_script(powershell_script_filename):
    try:
        subprocess.run(["powershell.exe", "-File", powershell_script_filename], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {powershell_script_filename}: {e}")        
        
        
def run_script(script_name, arg1=None):
    try:
        module = importlib.import_module(script_name)
        # Assuming there's a function named 'main' in your script to run
        if arg1 == None:
            module.main()
            
        module.main(arg1)
        
    except ImportError:
        print(f"Failed to import {script_name}")





if __name__ == "__main__":
    scripts_to_run = ["gif", "change_desk"]
    processes = []
        
    
    
    #gifs
    for i in range(7):
        process = multiprocessing.Process(target=run_script, args=("gif",))
        processes.append(process)
        time.sleep(0.5)
        process.start()
        