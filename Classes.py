class Glitch:

    interfaceWindow = None
    imageToGlitch = None

    def __init__(self):
        print("Glitch Created")
        self.InitInterface()

    def __del__(self):
        print("Glitch Deleted")

    def InitInterface(self):
        pass

    def StartGlitch(self):
        pass

    def RegisterGlitch(self, glitchImage):
        Core.DrawImageOnGlitchWindow(glitchImage)
        Core.CreateCurrentGlitchWindow()
        Core.ShowCurrentGlitchThumbnail(glitchImage)
        Core.AddGlitchHistory(glitchImage)
    
import Core as Core