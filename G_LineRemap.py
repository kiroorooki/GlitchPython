from Classes import *
from tkinter import *
import numpy as np
import cv2

class LineRemap(Glitch):

    glitchLineSkipSlider = None

    def StartGlitch(self):
        if Core.currentGlitch.any(): 
            tempImage = Core.currentGlitch
            glitchmage = tempImage
            height, width, channels = tempImage.shape
            print("totoletoto", self.glitchLineSkipSlider.get())
            for i in range(height):
                if ((i % int(self.glitchLineSkipSlider.get())) == 0): glitchmage[i] = tempImage[height -1 - i]
            super().RegisterGlitch(glitchmage)

    def InitInterface(self):
        self.interfaceWindow = Tk()
        self.interfaceWindow.title(__name__)
        glitchButton = Button(self.interfaceWindow, text="Glitch !", command=self.StartGlitch)
        glitchButton.pack()
        self.glitchLineSkipSlider = Spinbox(self.interfaceWindow, from_=1, to_=Core.currentGlitch.shape[0])
        self.glitchLineSkipSlider.pack()


