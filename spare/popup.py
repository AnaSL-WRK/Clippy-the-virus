from tkinter import *
from tkinter import messagebox
from time import sleep 


root = Tk()
root.withdraw()



def pop_always_on_top_and_pos(msg,i):  # This will be on top of any other window

    offset = 300 + i*10
    root.geometry('400x100+'+str(offset)+'+'+str(offset))
    root.resizable(False, False)
    root.attributes('-alpha', 0.5)
    
    if msg == "warning":
        messagebox.showwarning(title="CLIPPY IS WATCHING", message="TOO LATE")
        
    elif msg == "error":
        messagebox.showerror(title="CLIPPY IS WATCHING", message="ERROR", )

    elif msg == "cancel":
        messagebox.askokcancel(title="CANCEL?", message="CANCEL?")
        
    
 

pop_always_on_top_and_pos("warning",0)
pop_always_on_top_and_pos("error",10)
pop_always_on_top_and_pos("cancel",20)

while True:
   for i in range (100):
        pop_always_on_top_and_pos("error",10)
        pop_always_on_top_and_pos("warning",10)
        i+=1

     

  
    

