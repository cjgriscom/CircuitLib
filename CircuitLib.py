#!/usr/bin/python2

import os
import sys
import importlib
from Tkinter import *
import ttk
import tkFont

class CircuitLib(Frame):
    def packButton(self, buttonFrame, txt, cmd):
        
        btn = Button(buttonFrame, text=txt, command=cmd)
        btn.grid(row=self.BUTTONCOL, column=0,sticky=NSEW)
        self.BUTTONCOL += 1
        return btn
   
    def instructions(self):
        print "TODO"
 
    def about(self):
        print "TODO"
 
    def modules(self):
        print "TODO"
 
    def version(self):
        print "TODO"
 
    def createWidgets(self):
        self.BUTTONCOL = 0
        buttonFrame = Frame()
        buttonFrame.grid(row=0, column=1,sticky=NSEW)
        
 
        self.exitBtn = self.packButton(buttonFrame, "Instructions", self.instructions)
        self.instBtn = self.packButton(buttonFrame, "About", self.about)
        self.modlBtn = self.packButton(buttonFrame, "Modules", self.modules)
        self.versBtn = self.packButton(buttonFrame, "Version", self.version)
        self.exitBtn = self.packButton(buttonFrame, "Exit", self.quit)
 
        self.notebook = ttk.Notebook()
        self.notebook.grid(row=0,column=0,sticky=NSEW)
 
    def __init__(self):
        Frame.__init__(self)
        self.MODULES_DIR = 'modules'
        self.grid(sticky=NSEW)
        self.createWidgets()
        self.loadModules()
 
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
        if mod.hasTab():
            mod.genTab(self, self.notebook)
        return mod
    
cl = CircuitLib()
cl.mainloop()

