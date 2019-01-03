import os
import tkinter as tk
from tkinter import *

root=tk.Tk()
#root.resizable(0,0)
#root.geometry('255x255')
root.title("Rick_Python_GUI")

def click():
	global count
	count=count + 1
	step1.configure(text="Yes "+str(count))

#文字Label
step1 = tk.Label(text="Step.1 TEXT", width=25)
input = tk.Entry(root, show="Hello")
count=0

#action define
button1=tk.Button(root, text="Press Me", command=click)

#assign location pack
# input.pack()
# step1.pack()
# button1.pack()

#assign location grid
# step1.grid(column=1,row=0)
# input.grid(column=2,row=1)
# button1.grid(column=3,row=2)

root.mainloop()

