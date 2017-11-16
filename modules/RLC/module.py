import os
import sys
import importlib
from Tkinter import *
import ttk
import tkFont
class Module:
    #def __init__(self):

    def moduleName(self):
        return 'RLC'

    def moduleVersion(self):
        return '0.0.1'

    def hasTab(self):
        return True

    def genTab(self, cl, nbook):
        tab555 = Frame(nbook)
        Label(tab555, text=self.moduleName()).pack(side=LEFT)

        btn = Button(tab555, text="Placeholder", command=cl.quit)
        btn.pack(side=RIGHT)
        nbook.add(tab555, text=self.moduleName()) # add tab to Notebook

