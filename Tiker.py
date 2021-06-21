# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:03:47 2021

@author: ansanchez
"""
from tkinter import *

root = Tk()

# root.title("Ojetes a babor")


# frame = Frame(root,width=480, height=320)

# frame.pack()

# label = Label(frame, text="A tope")
# label.place(x=100,y=100)




label=Label(root, text="Nombre")
label.grid(row=0, column=0, sticky='w')

entry=Entry(root)
entry.grid(row=0, column=1)

label2=Label(root, text="Apellidos")
label2.grid(row=1, column=0)

entry2=Entry(root)
entry2.grid(row=1, column=1, sticky='w')

root.mainloop()