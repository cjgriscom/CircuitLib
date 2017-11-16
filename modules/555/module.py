import os
import sys
import importlib
from Tkinter import *
import ttk
import tkFont
from PIL import ImageTk, Image
import tkMessageBox
import math

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
    
    def clear(self):
        self.setValue(self.HZ, "")
        self.setValue(self.DC, "")
        self.setValue(self.R1, "")
        self.setValue(self.R2, "")
        self.setValue(self.C1, "")
    
    def setValue(self, entry, value):
        entry.delete(0, END) #deletes the current value
        entry.insert(0, str(value)) #inserts new value assigned by 2nd parameter
    
    def getValue(self, entry, name):
        txt = entry.get()
        if txt.strip() == "":
            return 0, 0 # Exit code 0 means no value
        try:
            v = float(txt)
            return v, 1 # Exit code 1 means good value
        except ValueError:
            tkMessageBox.showinfo("Error", "Could not understand "+name+" value: " + txt + "")
            return 0, -1 # Exit code -1 means error
        
    
    def calculate(self):
        HZ, hasHZ = self.getValue(self.HZ, "Frequency")
        DC, hasDC = self.getValue(self.DC, "Duty Cycle")
        R1, hasR1 = self.getValue(self.R1, "R1")
        R2, hasR2 = self.getValue(self.R2, "R2")
        C1, hasC1 = self.getValue(self.C1, "C1")
        ERR = 0
        if hasHZ | hasDC | hasR1 | hasR2 | hasC1 >= 0: # Not negative
            numEntered = hasHZ + hasDC + hasR1 + hasR2 + hasC1
            if numEntered == 3 or numEntered == 4:
                ERR = 0
                if (DC < 0 or HZ < 0 or R1 < 0 or R2 < 0 or C1 < 0):
                    ERR = -1
                    tkMessageBox.showinfo("Error", "All values must be positive")
                elif (hasDC == 1 and DC < 50):
                    ERR = -1
                    tkMessageBox.showinfo("Error", "The duty cycle must be >= 50")
                elif (hasDC == 1 and DC > 99):
                    ERR = -1
                    tkMessageBox.showinfo("Error", "The duty cycle must be <= 99")
                elif (hasDC == 1 and hasR1 == 1 and (DC == 50) != (R1 == 0)):
                    ERR = -1
                    if R1 == 0:
                        tkMessageBox.showinfo("Error", "The duty cycle must be 50 when R1 equals 0")
                    else:
                        tkMessageBox.showinfo("Error", "R1 must be 0 when the duty cycle equals 50")
                elif (hasDC == 0 and hasHZ == 0): DC, HZ, ERR = self.solve_DC_HZ(R1, R2, C1)
                elif (hasDC == 0 and hasR1 == 0): DC, R1, ERR = self.solve_DC_R1(HZ, R2, C1)
                elif (hasDC == 0 and hasR2 == 0): DC, R2, ERR = self.solve_DC_R2(R1, HZ, C1)
                elif (hasDC == 0 and hasC1 == 0): DC, C1, ERR = self.solve_DC_C1(R1, R2, HZ)
                elif (hasHZ == 0 and hasR1 == 0): HZ, R1, ERR = self.solve_HZ_R1(DC, R2, C1)
                elif (hasHZ == 0 and hasR2 == 0): HZ, R2, ERR = self.solve_HZ_R2(R1, DC, C1)
                elif (hasHZ == 0 and hasC1 == 0): HZ, C1, ERR = self.solve_HZ_C1(R1, R2, DC)
                elif (hasC1 == 0 and hasR1 == 0): C1, R1, ERR = self.solve_C1_R1(DC, R2, HZ)
                elif (hasC1 == 0 and hasR2 == 0): C1, R2, ERR = self.solve_C1_R2(R1, DC, HZ)
                elif (hasR1 == 0 and hasR2 == 0): R1, R2, ERR = self.solve_R1_R2(DC, HZ, C1)
                elif (hasDC == 0): DC, HZ, ERR = self.solve_DC_HZ(R1, R2, C1)
                elif (hasC1 == 0): DC, C1, ERR = self.solve_DC_C1(R1, R2, HZ)
                elif (hasHZ == 0): DC, HZ, ERR = self.solve_DC_HZ(R1, R2, C1)
                else:
                    tkMessageBox.showinfo("Error", "The system is overconstrained. Remove a value and try again.")
                    ERR = -1
                
                if ERR == 0:
                    self.setValue(self.DC,DC)
                    self.setValue(self.HZ,HZ)
                    self.setValue(self.R1,R1)
                    self.setValue(self.R2,R2)
                    self.setValue(self.C1,C1)
            else:
                tkMessageBox.showinfo("Error", "Please enter 3 or 4 values at a time")
        
    
    def solve_DC_HZ(self, R1,R2,C1): #Complete
        HZ=1.44/((R1+2*R2)*C1)
        DC=(R1+R2)*100/(R1+2*R2)
        return DC, HZ, 0
    
    def solve_DC_R1(self, HZ,R2,C1): #Complete
        DC=100.-(625*C1*HZ*R2/9.)
        R1=(100.-2*DC)*R2/(DC-100.)
        return DC, R1, 0
    
    def solve_DC_R2(self, R1,HZ,C1): #Complete
        DC=50.+(625.*C1*HZ*R1)/(18.)
        R2=((1.44/HZ/C1)-R1)/2.
        return DC, R2, 0
    
    def solve_DC_C1(self, R1,R2,HZ): #Complete
        DC=(R1+R2)*100/(R1+2*R2)
        C1=1.44/(HZ*(R1+2*R2))
        return DC, C1, 0
    
    def solve_HZ_R1(self, DC,R2,C1): #Complete
        R1=(100.-2*DC)*R2/(DC-100.)
        HZ=1.44/((R1+2*R2)*C1)
        return HZ, R1, 0
    
    def solve_HZ_R2(self, R1,DC,C1): #Complete
        if R1 == 0:
            tkMessageBox.showinfo("Error", "With a 50% duty cycle, R2 and HZ are dependent; one or the other must be set.")
            return 0, 0, -1
        else:
            R2=(DC-100.)*R1/(2*(50.-DC))
            HZ=1.44/((R1+2*R2)*C1)
            return HZ, R2, 0
    
    def solve_HZ_C1(self, R1,R2,DC): # Unsolvable case
        tkMessageBox.showinfo("Error", "C1 depends on frequency; one or the other must be set.")
        return 0, 0, -1
    
    def solve_C1_R1(self, DC,R2,HZ): #Complete
        R1=(100.-2*DC)*R2/(DC-100.)
        C1=1.44/(HZ*(R1+2*R2))
        return C1, R1, 0
    
    def solve_C1_R2(self, R1,DC,HZ): #Complete
        if R1 == 0:
            tkMessageBox.showinfo("Error", "With a 50% duty cycle, C1 and R2 are dependent; one or the other must be set.")
            return 0, 0, -1
        else:
            R2=(DC-100.)*R1/(2*(50.-DC))
            C1=1.44/(HZ*(R1+2*R2))
            return C1, R2, 0
    
    def solve_R1_R2(self, DC,HZ,C1): #Complete
        R2=9.*(100-DC)/(625.*C1*HZ)
        R1=(100.-2*DC)*R2/(DC-100.)
        return R1, R2, 0
    
    
    
    def genTab(self, cl, nbook):
        
        tab555 = Frame(nbook)
        #Label(tab555, text="555").pack(side=LEFT)
        
        self.imgLabel = cl.util_getImageLabel(tab555, __file__, "astable555.png")
        self.imgLabel.pack(side=LEFT)

        buttonFrame = Frame(tab555)
        buttonFrame.pack(side=RIGHT)
        
        self.packLabel(buttonFrame, "Fill in 3 or 4 out of 5\nvalues and the rest\nwill be calculated.")
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
        self.packSpacer(buttonFrame)
        self.packButton(buttonFrame, "Clear", self.clear)
 
        
        nbook.add(tab555, text=self.moduleName()) # add tab to Notebook

