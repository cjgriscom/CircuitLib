import os
import sys
import importlib
from Tkinter import *
import ttk
import tkFont
from PIL import ImageTk, Image
class Module:
    BUTTONCOL = 0
    #def __init__(self):

    def moduleName(self):
        return 'Astable 555'

    def moduleVersion(self):
        return '0.0.1'

    def hasTab(self):
        return True
    
    
    def packSpacer(self, buttonFrame):
        self.packLabel(buttonFrame, "")
      
    def packLabel(self, buttonFrame, txt):
        
        label = Label(buttonFrame, text=txt)
        label.grid(row=self.BUTTONCOL, column=0,sticky=NSEW)
        self.BUTTONCOL += 1
        return label
      
    def packField(self, buttonFrame):
        
        field = Entry(buttonFrame)
        field.grid(row=self.BUTTONCOL, column=0,sticky=NSEW)
        self.BUTTONCOL += 1
        return field
      
    def packButton(self, buttonFrame, txt, cmd):
        
        btn = Button(buttonFrame, text=txt, command=cmd)
        btn.grid(row=self.BUTTONCOL, column=0,sticky=NSEW)
        self.BUTTONCOL += 1
        return btn
    
    def calculate(self):
        nop
        
        

    def genTab(self, cl, nbook):
        
        tab555 = Frame(nbook)
        #Label(tab555, text="555").pack(side=LEFT)
        
        self.imgLabel = cl.util_getImageLabel(tab555, __file__, "astable555.png")
        self.imgLabel.pack(side=LEFT)

        buttonFrame = Frame(tab555)
        buttonFrame.pack(side=RIGHT)
        
        self.packLabel(buttonFrame, "Fill in 3 out of 5\nvalues and the rest\nwill be calculated.")
        self.packSpacer(buttonFrame)
        
        self.packLabel(buttonFrame, "Frequency (Hz)")
        self.HZ = self.packField(buttonFrame)
        self.packSpacer(buttonFrame)
        self.packLabel(buttonFrame, "Duty Cycle (%)")
        self.DC = self.packField(buttonFrame)
        self.packSpacer(buttonFrame)
        self.packLabel(buttonFrame, "R1 (ohm)")
        self.R1 = self.packField(buttonFrame)
        self.packSpacer(buttonFrame)
        self.packLabel(buttonFrame, "R2 (ohm)")
        self.R2 = self.packField(buttonFrame)
        self.packSpacer(buttonFrame)
        self.packLabel(buttonFrame, "C1 (farad)")
        self.C1 = self.packField(buttonFrame)
        self.packSpacer(buttonFrame)
        self.packButton(buttonFrame, "Calculate", self.calculate)
 
        
        nbook.add(tab555, text=self.moduleName()) # add tab to Notebook

