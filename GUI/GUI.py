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
	var=input.get()
	v3.set(str(count)+"  "+var)

v3 = StringVar()	
	
#文字Label
step1 = tk.Label(text="Step.1 TEXT", width=25)
input = tk.Entry(root, show=None)
count=0
e3 = tk.Entry(root, textvariable=v3, state='readonly')

#action define
button1=tk.Button(root, text="Press Me", command=click)

#assign location pack
input.pack()
step1.pack()
button1.pack()
e3.pack()

#assign location grid
# step1.grid(column=1,row=0)
# input.grid(column=2,row=1)
# button1.grid(column=3,row=2)
# e3.grid(column=4,row=3)

root.mainloop()

