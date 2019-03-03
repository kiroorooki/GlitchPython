from tkinter import *
class Glitch:

    interfaceWindow = None
    imageToGlitch = None
    glitchCoordinatesSpinBoxes = []

    def __init__(self):
        print("Glitch Created")
        self.InitInterface()

    def __del__(self):
        print("Glitch Deleted")

    def UpdateCoordinates(self, key):
        Core.DrawSelectionZone(
          int(self.glitchCoordinatesSpinBoxes[0].get()), 
          int(self.glitchCoordinatesSpinBoxes[1].get()), 
          int(self.glitchCoordinatesSpinBoxes[2].get()), 
          int(self.glitchCoordinatesSpinBoxes[3].get()))

    def InitInterface(self):
        self.interfaceWindow = Tk()
        self.glitchCoordinatesSpinBoxes.append(Spinbox(self.interfaceWindow, from_=0, to_=Core.currentGlitch.shape[0]))
        self.glitchCoordinatesSpinBoxes.append(Spinbox(self.interfaceWindow, from_=0, to_=Core.currentGlitch.shape[0]))
        self.glitchCoordinatesSpinBoxes.append(Spinbox(self.interfaceWindow, from_=0, to_=Core.currentGlitch.shape[1]))
        self.glitchCoordinatesSpinBoxes.append(Spinbox(self.interfaceWindow, from_=0, to_=Core.currentGlitch.shape[1]))
        for i in range(len(self.glitchCoordinatesSpinBoxes)):
          self.glitchCoordinatesSpinBoxes[i].bind("<Key>", self.UpdateCoordinates)
          self.glitchCoordinatesSpinBoxes[i].pack()

    def StartGlitch(self):
        pass

    def RegisterGlitch(self, glitchImage):
        Core.DrawImageOnGlitchWindow(glitchImage)
        Core.CreateCurrentGlitchWindow()
        Core.ShowCurrentGlitchThumbnail(glitchImage)
        Core.AddGlitchHistory(glitchImage)
    
import Core as Core