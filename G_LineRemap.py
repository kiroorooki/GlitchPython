from Classes import *
import numpy as np
import cv2
import random

class LineRemap(Glitch):

    glitchLineSkipSlider = None
    lineRemapType = 0

    def FullRemap(self):
        tempImage = Core.currentGlitch
        glitchmage = tempImage
        height, width, channels = tempImage.shape
        linesID = []
        for i in range(self.glitchCoordinates[2], self.glitchCoordinates[3]):
            linesID.append(i)
        for i in range(self.glitchCoordinates[2], self.glitchCoordinates[3]):
                lineID = random.randint(0, len(linesID) - 1)
                for j in range(self.glitchCoordinates[0], self.glitchCoordinates[1]):
                    glitchmage[i][j] = tempImage[lineID][j]
                linesID.pop(lineID)
        return glitchmage


    def TopBot(self):
        tempImage = Core.currentGlitch
        glitchmage = tempImage
        height, width, channels = tempImage.shape
        for i in range(self.glitchCoordinates[2], self.glitchCoordinates[3]):
            for j in range(self.glitchCoordinates[0], self.glitchCoordinates[1]):
                if ((i % int(self.glitchLineSkipSlider.get())) == 0):
                    glitchmage[i][j] = tempImage[height -1 - i][j]
        return glitchmage

    def InitInterface(self):
        super().InitInterface()
        self.interfaceWindow.title(__name__)
        glitchButton = Button(self.interfaceWindow, text="Glitch !", command=self.StartGlitch)
        glitchButton.pack()
        self.glitchLineSkipSlider = Spinbox(self.interfaceWindow, from_=1, to_=Core.currentGlitch.shape[0])
        self.glitchLineSkipSlider.pack()
        self.lineRemapType = IntVar()
        self.lineRemapType = 0
        Radiobutton(self.interfaceWindow, text="fullRemap", variable=self.lineRemapType, value=0).pack()
        Radiobutton(self.interfaceWindow, text="TopBot", variable=self.lineRemapType, value=1).pack()

    def StartGlitch(self):
        if Core.currentGlitch.any():
            super().StartGlitch()
            if self.lineRemapType == 0: glitchmage = self.FullRemap()
            elif self.lineRemapType == 1: glitchmage = self.TopBot()
            super().RegisterGlitch(glitchmage)
