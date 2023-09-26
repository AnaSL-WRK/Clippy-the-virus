import multiprocessing
import subprocess
import time
import os
        

def run_vbscript(vbscript_filename):
    try:
        subprocess.run(["cscript.exe", vbscript_filename], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {vbscript_filename}: {e}")
        
    




def main():

    processes = []

    
    
    for i in range(50):
        process = multiprocessing.Process(target=run_vbscript, args=("scripts/popup.vbs",))
        process.start()
        i+=1 
    
    time.sleep(60)
    os.system("taskkill /f /im  cscript.exe")
    
    
    
    #time.sleep(5)
    for process in processes:
        process.join()
        
        
