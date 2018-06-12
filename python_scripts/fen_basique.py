# -*- coding: latin-1 -*-
"""
Created on Thu Jan 12 21:35:59 2012

@author: mat
"""

from tkinter import *

fen1 = Tk()
tex1 = Label(fen1, text="bonjour tout le monde", fg="red")
tex1.pack()
bou1 = Button(fen1, text="quitter", command=fen1.destroy)
bou1.pack()
fen1.mainloop()
