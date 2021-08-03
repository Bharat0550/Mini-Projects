# Python code to display an digital clock using Twitter library

from tkinter import *
from tkinter.ttk import *

from time import strftime
root = Tk()
root.title("clock")
def time():
    string = strftime('%H:%M:%S %p')
    Label.config(text=string)
    Label.after(1000, time)

Label = Label(root, font=("ds-digital" , 80), background = "black" , foreground = "cyan")
Label.pack(anchor= 'center')
time()

mainloop()

#it display a digital clock of black and cyan color



  
