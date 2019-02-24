from Classes import *
from tkinter import *
import numpy as np
import cv2

class LangtonAnt(Glitch):

    def StartGlitch(self, lineSkip=2):
        if Core.currentGlitch.any(): 
            tempImage = Core.currentGlitch
            glitchImage = tempImage
            super().RegisterGlitch(glitchImage)

    def DoGlitch(self, glitchImage):
        pass

    def InitInterface(self):
        self.interfaceWindow = Tk()
        self.interfaceWindow.title(__name__)
        glitchButton = Button(self.interfaceWindow, text="Glitch !", command=self.StartGlitch)
        glitchButton.pack()
