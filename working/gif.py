from tkinter import *
from random import randint
from time import sleep

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()



 
frameCnt = 20
frames = [PhotoImage(file='../assets/spin_clip.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
    

root.title("CLIPPY IS WATCHING YOU")  #in case
root.geometry("300x300+" + str(randint(0, width)) + "+" + str(randint(0, height)))
#root.iconbitmap('!CODE\Eye.jpg')
root.attributes('-topmost', 1)
root.wm_attributes('-disabled', True)


root.wm_attributes("-transparentcolor", '#f4f4f4')

root.mainloop()
#threading.Thread(target=gif()).start

