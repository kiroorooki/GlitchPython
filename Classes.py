from tkinter import *
class Glitch:

    interfaceWindow = None
    imageToGlitch = None
    glitchCoordinatesSpinBoxes = []
    #coords : x0 x1 y0 y1
    glitchCoordinates = [0,0,0,0]
    useGlitchCoordinates = IntVar()

    def __init__(self):
        print("Glitch Created")
        self.InitInterface()

    def __del__(self):
        print("Glitch Deleted")

    def UpdateCoordinates(self, key=None):
        if self.useGlitchCoordinates == 0:
            tempCoordinates = [0,0,0,0]
            for i in range(4):
                tempCoordinates[i] = int(self.glitchCoordinatesSpinBoxes[i].get())
                if i < 2 and Core.currentImage.shape[1] < tempCoordinates[i]:
                    tempCoordinates[i] = Core.currentImage.shape[1]
                elif i > 1 and Core.currentImage.shape[0] < tempCoordinates[i]:
                    tempCoordinates[i] = Core.currentImage.shape[0]
            
            if tempCoordinates[1] <= tempCoordinates[0]:
                tempCoordinates[0] = tempCoordinates[1] - 1
            if tempCoordinates[3] <= tempCoordinates[2]:
                tempCoordinates[2] = tempCoordinates[3] - 1
        else: tempCoordinates = [0, Core.currentImage.shape[1], 0 , Core.currentImage.shape[0]]

        self.glitchCoordinates = tempCoordinates
        Core.DrawSelectionZone(
        self.glitchCoordinates[0], 
        self.glitchCoordinates[1], 
        self.glitchCoordinates[2], 
        self.glitchCoordinates[3])

    def InitInterface(self):
        self.interfaceWindow = Tk()
        Radiobutton(self.interfaceWindow, text="Full glitch", variable=self.useGlitchCoordinates, value=1).pack()
        Radiobutton(self.interfaceWindow, text="PartialGlitch", variable=self.useGlitchCoordinates, value=0).pack()
        self.glitchCoordinatesSpinBoxes.append(Spinbox(self.interfaceWindow, from_=0, to_=Core.currentImage.shape[0]))
        self.glitchCoordinatesSpinBoxes.append(Spinbox(self.interfaceWindow, from_=0, to_=Core.currentImage.shape[0]))
        self.glitchCoordinatesSpinBoxes.append(Spinbox(self.interfaceWindow, from_=0, to_=Core.currentImage.shape[1]))
        self.glitchCoordinatesSpinBoxes.append(Spinbox(self.interfaceWindow, from_=0, to_=Core.currentImage.shape[1]))
        for i in range(len(self.glitchCoordinatesSpinBoxes)):
          self.glitchCoordinatesSpinBoxes[i].bind("<Key>", self.UpdateCoordinates)
          self.glitchCoordinatesSpinBoxes[i].bind("<Button>", self.UpdateCoordinates)
          self.glitchCoordinatesSpinBoxes[i].pack()

    def StartGlitch(self):
        Core.ClearSelectionZone()

    def RegisterGlitch(self, glitchImage):
        Core.DrawImageOnGlitchWindow(glitchImage)
        Core.CreateCurrentGlitchWindow()
        Core.ShowCurrentGlitchThumbnail(glitchImage)
        Core.AddGlitchHistory(glitchImage)
    
import Core as Core