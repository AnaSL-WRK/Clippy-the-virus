from tkinter import *
from random import randint
import time
import threading

root = Tk()
def gif():
    timeout = 5   # [seconds]
    
    #timeout_start = time.time()
    #while time.time() < timeout_start + timeout:
    start_time = time.time()
    seconds = 4
    
    while True:   
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        while elapsed_time < seconds:
            width = root.winfo_screenwidth()
            height = root.winfo_screenheight()
            
            frameCnt = 20
            frames = [PhotoImage(file='../assets/spin_clip.gif', format='gif -index %i' % i) for i in range(frameCnt)]

            def update(ind):
                frame = frames[ind]
                ind += 1
                if ind == frameCnt:
                    ind = 0
                label.configure(image=frame)
                root.after(100, update, ind)

            label = Label(root)
            label.pack()

            label.master.overrideredirect(True)
            root.after(0, update, 0)
                
            root.title("CLIPPY IS WATCHING YOU")
            root.geometry("300x300+" + str(randint(0, width)) + "+" + str(randint(0, height)))
            root.attributes('-topmost', 1)
            root.wm_attributes('-disabled', True)
            root.wm_attributes("-transparentcolor", '#f4f4f4')
            root.mainloop()
        break
    root.destroy()

def main():
    
    gif()
    # Sleep for 5 seconds (or any desired duration)
    
    # Close the tkinter window when done
    root.quit()

if __name__ == "__main__":
    main()