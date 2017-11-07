import os
import sys
import importlib

class CircuitLib:


    def __init__(self):
	self.MODULES_DIR = 'modules'
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
        return mod
    
cl = CircuitLib()

