#!/usr/bin/python2

import os
import sys
import importlib
from Tkinter import *
import ttk
import tkFont

class CircuitLib(ttk.Frame):
    @classmethod
    def main(clazz):
        #NoDefaultRoot()
        root = Tk()
        app = clazz(root)
        app.grid(sticky=NSEW)
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        root.resizable(True, True) # Row, Col
        root.mainloop()
  
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
        buttonFrame = ttk.Frame()
        buttonFrame.grid(row=0, column=1,sticky="SEW")
        
 
        self.exitBtn = self.packButton(buttonFrame, "Instructions", self.instructions)
        self.instBtn = self.packButton(buttonFrame, "About", self.about)
        self.modlBtn = self.packButton(buttonFrame, "Modules", self.modules)
        self.versBtn = self.packButton(buttonFrame, "Version", self.version)
        self.exitBtn = self.packButton(buttonFrame, "Exit", self.quit)
 
        self.notebook = ttk.Notebook()
        self.notebook.grid(row=0,column=0,sticky=NSEW)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
 
    def __init__(self, root):
        ttk.Frame.__init__(self, root)
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

if __name__ == '__main__':
    CircuitLib.main()
print "Program Exited"
