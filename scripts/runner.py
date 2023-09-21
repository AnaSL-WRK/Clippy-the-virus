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


    #minimize all windows
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press(Key.home)
    keyboard.release(Key.home)
    keyboard.release(Key.cmd)
               
            
    #freeze mouse
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start()
    
    
    
    #gifs
    for i in range(7):
        process = multiprocessing.Process(target=run_script, args=("gif",))
        processes.append(process)
        time.sleep(0.5)
        process.start()
        

    #warnings
    process = multiprocessing.Process(target=run_script, args=("warningRunner",))
    processes.append(process)
    process.start()
    
    

    #red
    process = multiprocessing.Process(target=run_script, args=("change_desk", 1))
    processes.append(process)
    process.start()
    

    #start sound and wallpaper changes
    process = multiprocessing.Process(target=run_vbscript, args=("sound.vbs",))
    processes.append(process)
    process.start()
    
    process = multiprocessing.Process(target=run_powershell_script, args=("accentColor.ps1",))
    processes.append(process)
    process.start()
    
    time.sleep(3)
    
    process = multiprocessing.Process(target=run_script, args=("change_desk", 2))
    processes.append(process)
    process.start()
    
    time.sleep(8.5)
    
    process = multiprocessing.Process(target=run_script, args=("change_desk", 3))
    processes.append(process)
    process.start()
    
    time.sleep(8.5)

    process = multiprocessing.Process(target=run_script, args=("change_desk", 4))
    processes.append(process)
    process.start()
    
    time.sleep(8)#9
    
    process = multiprocessing.Process(target=run_script, args=("change_desk", 5))
    processes.append(process)
    process.start()
    
    time.sleep(8)
    
    process = multiprocessing.Process(target=run_script, args=("change_desk", 6))
    processes.append(process)
    process.start()
   
    time.sleep(25)
    
    mouse_listener.stop()
    
    process = multiprocessing.Process(target=run_vbscript, args=("trash.vbs",))
    processes.append(process)
    process.start()
    
    
    time.sleep(5)
    
    for process in processes:
        process.join()
   
    #os.system("shutdown /r /t 1")   
