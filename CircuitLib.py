#!/usr/bin/python2

import os
import sys
import importlib
from Tkinter import *
import ttk
import tkFont

class CircuitLib(Frame):

   def createWidgets(self):
       self.buttonFrame = Frame()
       self.buttonFrame.grid(row=0, column=1)

       fred = self.draw.create_oval(0,0,20,20,fill="green",tags="selected")
       
       self.notebook = ttk.Notebook()
       self.notebook.grid(row=0,column=0)
       master_foo = Frame(self.notebook, name='master-foo')
       Label(master_foo, text="this is foo").pack(side=LEFT)
       # Button to quit app on right
       btn = Button(master_foo, text="foo", command=self.quit)
       btn.pack(side=RIGHT)
       self.notebook.add(master_foo, text="foo") # add tab to Notebook

   def __init__(self):
       Frame.__init__(self)
       self.MODULES_DIR = 'modules'
       self.loadModules()
       self.grid()
       self.createWidgets()

   def loadModules(self):
       tree = os.listdir(self.MODULES_DIR)

       for i in tree:
           if not os.path.isdir(os.path.join(self.MODULES_DIR,i)): continue
           print "Checking", i
           mod = self.instantiateModule(i)
           print "Instantiated", mod.moduleName(), ("v" + mod.moduleVersion())
           print "HasTab? ", mod.hasTab()
       
   def instantiateModule(self, name): 
       MyClass = getattr(importlib.import_module("modules."+name+".module"), "Module")
       mod = MyClass() #Instantiate
       return mod
    
cl = CircuitLib()
cl.mainloop()

