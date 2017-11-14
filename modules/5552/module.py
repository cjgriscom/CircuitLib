import os
import sys
import importlib
from Tkinter import *
import ttk
import tkFont
class Module:
    #def __init__(self):

    def moduleName(self):
        return '5552'

    def moduleVersion(self):
        return '0.0.1'

    def hasTab(self):
        return True

    def genTab(self, cl, nbook):
        tab555 = Frame(nbook, name='5552')
        Label(tab555, text="5552").pack(side=LEFT)

        btn = Button(tab555, text="Button5552", command=cl.quit)
        btn.pack(side=RIGHT)
        nbook.add(tab555, text="Tab5552") # add tab to Notebook

