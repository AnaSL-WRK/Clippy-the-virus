from tkinter import *
from random import randint
import time
import os

root = Tk()
global sec
sec = 60
global timeout_start
timeout_start = time.time()





def gif():

    simp_path1 = 'assets/spin_clip.gif'
    abs_path1 = os.path.abspath(simp_path1)
    
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()


    frameCnt = 20
    frames = [PhotoImage(file=abs_path1, format='gif -index %i' % i) for i in range(frameCnt)]

    def update(ind):

        global temp
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        root.after(100, update, ind)
        
        
        
        if time.time() < timeout_start + sec:
            pass
        else:
            root.destroy()
 
       
  
            
    

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


def main():
    global temp
    gif()
    # Sleep for 5 seconds (or any desired duration)
    
 

if __name__ == "__main__":
    main()