#!/usr/bin/python2

import os
import sys
import importlib
from Tkinter import *
import tkFont

class CircuitLib(Frame):
   def mouseDown(self, event):
       self.lastX = event.x
       self.lastY = event.y

   def mouseMove(self, event):
       self.draw.move(CURRENT, event.x - self.lastX, event.y - self.lastY)
       self.lastX = event.x
       self.lastY = event.y
        
   def mouseEnter(self, event):
       self.draw.itemconfig(CURRENT, fill="red")


   def mouseLeave(self, event):
       self.draw.itemconfig(CURRENT, fill="blue")

   def createWidgets(self):
       times24 = tkFont.Font(family="times", size="24")
       times36 = tkFont.Font(family="times", size="36")
       self.draw = Canvas(self, width="300", height="200")
       self.draw.grid(row=0)
       self.draw.create_rectangle(1,1,300,200)

       self.QUIT = Button(self, text="Quit", foreground="red", bd=10,
                          font=times24, command=self.quit)
       self.QUIT.grid(row=1, sticky=N+S+E+W)

       fred = self.draw.create_oval(0,0,20,20,fill="green",tags="selected")

       self.draw.tag_bind(fred, "<Any-Enter>", self.mouseEnter)
       self.draw.tag_bind(fred, "<Any-Leave>", self.mouseLeave)

       Widget.bind(self.draw, "<1>", self.mouseDown)
       Widget.bind(self.draw, "<B1-Motion>", self.mouseMove)
       


   def __init__(self):
       Frame.__init__(self)
       self.MODULES_DIR = 'modules'
       self.loadModules()
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
cl.mainLoop()

