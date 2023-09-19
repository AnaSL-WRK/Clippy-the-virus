from concurrent.futures import thread
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import time
from random import randint
import threading
import multiprocessing

root = tk.Tk()
frame = Frame(root)


#offset = 300 + 100*10
#root.geometry('150x50+'+str(offset)+'+'+str(offset))

        
class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    
    def load(self, im):
        
            root.geometry("300x300+" + str(randint(0, root.winfo_screenwidth() - 300)) + "+" + str(randint(0, root.winfo_screenmmheight() - 60)))
            
            if isinstance(im, str):
                im = Image.open(im)
            frames = []
            
            try:
                for i in count(1):
                    frames.append(ImageTk.PhotoImage(im.copy()))
                    im.seek(i)
            except EOFError:
                pass
            self.frames = cycle(frames)##
            
            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100
            
            if len(frames) == 1:
                self.config(image=next(self.frames))#
            else:
                self.next_frame()
            
    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))#
            self.after(self.delay, self.next_frame)
            
lbl = ImageLabel(root)
lbl.pack()
#demo :

        
        


threading.Thread(target=lbl.load("!CODE\spin_clip.gif")).start

print("helo")

threading.Thread(target=lbl.load("!CODE\spin_clip.gif")).start
#


   

#process = multiprocessing.Process(target=lbl.load("!CODE\spin_clip.gif"))
#process1 = multiprocessing.Process(target=lbl.load("!CODE\spin_clip.gif"))
#process.start()
#process1.start()

   
   
#threading.Thread(target=gif).start()
#threading.Thread(target=gif).start()

    
        
        
        
        
        
        

#root.wm_attributes('-alpha', 1)
#root.wm_attributes('-toolwindow', 0)
root.title("CLIPPY IS WATCHING YOU")  #in case
root.geometry('300x300')
#root.iconbitmap('!CODE\Eye.jpg')
root.attributes('-topmost', 1)
root.wm_attributes('-disabled', True)


root.wm_attributes("-transparentcolor", '#f4f4f4')

frame.master.overrideredirect(True)  # Set no border or title

root.mainloop()