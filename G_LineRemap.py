from Classes import *
import numpy as np
import cv2
import random

class LineRemap(Glitch):

    glitchLineSkipSlider = None

    def FullRemap(self):
        tempImage = Core.currentGlitch
        glitchmage = tempImage
        #np.random.shuffle(tempImage)
        height, width, channels = tempImage.shape
        linesID = []
        for i in range(height):
          linesID.append(i)
        for i in range(height):
              lineID = random.randint(0, len(linesID) - 1)
              glitchmage[i] = tempImage[lineID]
              linesID.pop(lineID)
        return glitchmage


    def TopBot(self):
      tempImage = Core.currentGlitch
      glitchmage = tempImage
      height, width, channels = tempImage.shape
      for i in range(height):
          if ((i % int(self.glitchLineSkipSlider.get())) == 0): glitchmage[i] = tempImage[height -1 - i]
      return glitchmage

    def InitInterface(self):
        super().InitInterface()
        self.interfaceWindow.title(__name__)
        glitchButton = Button(self.interfaceWindow, text="Glitch !", command=self.StartGlitch)
        glitchButton.pack()
        self.glitchLineSkipSlider = Spinbox(self.interfaceWindow, from_=1, to_=Core.currentGlitch.shape[0])
        self.glitchLineSkipSlider.pack()

    def StartGlitch(self):
        if Core.currentGlitch.any(): 
            glitchmage = self.FullRemap()
            super().RegisterGlitch(glitchmage)
