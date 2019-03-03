from tkinter import Tk, filedialog, ttk, messagebox
import numpy as np
import cv2 
from PIL import Image as Img
from PIL import ImageTk

#images
currentImage = None
currentGlitch = None
currentGlitchType = None
currentImageTk = None
currentGlitchTk = None
previousGlitchTk = None
#Image canvas
currentImageCanvas = None
currentGlitchCanvas = None
previousGlitchCanvas = None
#variables
thumbnailSize = 300
glitchHistory = []
glitchHistorylistBox = None
glitchCoordinateRectangles = []

mainWindow = None
glitchWindowName = 'glitchWindow'

def Initialization():
    global mainWindow
    global currentGlitchType
    mainWindow = Tk()
    mainWindow.title("Glitch")
    InitInterface()
    mainWindow.mainloop()

def OpenImage():
    image = cv2.imread(filedialog.askopenfilename(), 1)
    global currentImage, currentGlitch
    if image is not None:
        currentImage = image
        currentGlitch = image
        global mainWindow
        ShowCurrentImageThumbnail(image)

def InitBarMenu(window):
    menuBar = Menu(window)
    filemenu = Menu(menuBar, tearoff=0)
    filemenu.add_command(label="Open", command=OpenImage)
    filemenu.add_command(label="Save", command=SaveSelectedGlitches)
    filemenu.add_separator()
    menuBar.add_cascade(label="File", menu=filemenu)
    window.config(menu=menuBar)

def CreateCurrentGlitchWindow():
    cv2.namedWindow(glitchWindowName, cv2.WINDOW_NORMAL)

def DrawImageOnGlitchWindow(image):
    cv2.imshow(glitchWindowName, image)

def ConvertImageFromOCVToTkinter(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Img.fromarray(img)
    return img

def OnGlitchSelect(evt):
    global currentGlitchType, currentGlitch
    if currentGlitch is not None :
        if currentGlitchType != None : 
            if currentGlitchType.interfaceWindow != None : currentGlitchType.interfaceWindow.destroy()
            del currentGlitchType
        w = evt.widget
        currentGlitchType = glitchlist[w.get()]()

def OnHistorySelect(evt):
    w = evt.widget
    if len(w.curselection()) > 0 :
      index = int(w.curselection()[0])
      ShowCurrentGlitchThumbnail(glitchHistory[index])

def InitInterface():
    global mainWindow, currentImageCanvas, currentGlitchCanvas, previousGlitchCanvas, glitchHistorylistBox
    InitBarMenu(mainWindow)
    leftFrame = Frame(mainWindow, bg='blue', width=300, height=900)
    leftFrame.grid(row=0, column=0)
    rightFrame = Frame(mainWindow, bg='red', width=thumbnailSize, height=900)
    rightFrame.grid(row=0, column=1)
    currentImageCanvas = Canvas(rightFrame, bg='black', width=thumbnailSize, height=thumbnailSize)
    currentImageCanvas.grid(row=0, column=0)
    currentGlitchCanvas = Canvas(rightFrame, bg='green', width=thumbnailSize, height=thumbnailSize)
    currentGlitchCanvas.grid(row=1, column=0)
    previousGlitchCanvas = Canvas(rightFrame, bg='white', width=thumbnailSize, height=thumbnailSize)
    previousGlitchCanvas.grid(row=2, column=0)
    glitchComboBox = ttk.Combobox(leftFrame, values = list(glitchlist.keys()))
    glitchComboBox.grid(row=0, column=0)
    glitchComboBox.bind("<<ComboboxSelected>>", OnGlitchSelect)
    glitchHistorylistBox = Listbox(leftFrame, height=30, width=35)
    glitchHistorylistBox.bind('<<ListboxSelect>>', OnHistorySelect)
    glitchHistorylistBox.grid(row=1, column=0)
    resetButton = Button(leftFrame, text="Reset Glitch image", command=ResetGlitchImage)
    resetButton.grid(row=2, column=0)
    saveButton = Button(leftFrame, text="Reset History",command=ResetHistory)
    saveButton.grid(row=3, column=0)
    saveButton1 = Button(leftFrame, text="Save Selected", command=SaveSelectedGlitches)
    saveButton1.grid(row=4, column=0)
    saveButton2 = Button(leftFrame, text="Save All")
    saveButton2.grid(row=5, column=0)

def ResetGlitchImage():
    global currentGlitch, currentGlitchCanvas, currentImage
    del currentGlitch
    if currentImage.Any() : currentGlitch = currentImage
    currentGlitchCanvas.delete("all")
    ShowCurrentGlitchThumbnail(currentImage)

def ResetHistory():
    global glitchHistorylistBox, glitchHistory
    msgBox = messagebox.askokcancel('Clear history',"You're about to clear the entire history !", icon = 'warning')
    if msgBox == 'ok':
       glitchHistory.clear()
       glitchHistorylistBox.delete(0,'end')
       


def SaveSelectedGlitches():
    global glitchHistorylistBox, glitchHistory
    glitchArray = []
    if len(glitchHistorylistBox.curselection()) > 0 : 
        for img in glitchHistorylistBox.curselection():
            glitchArray.append(glitchHistory[img])
        SaveGlitches(glitchArray)

def SaveGlitches(glitchArray):
    global glitchHistory
    if len(glitchArray) > 0 : 
        i = 0
        filepath = filedialog.asksaveasfilename()
        for img in glitchArray:
            filepath = filepath + "_" + str(i) + ".png"
            SaveFile(filepath, img)
            i += 1

def SaveAllGlitches():
    global glitchHistory
    SaveGlitches(glitchHistory)

def SaveFile(filepath, fileToSave):
  if fileToSave != None :
        cv2.imwrite(filepath , fileToSave)


def ShowCurrentImageThumbnail(img):
    global currentImageTk, currentImageCanvas
    currentImageTk = ConvertImageFromOCVToTkinter(img)
    currentImageTk.thumbnail([thumbnailSize, thumbnailSize])
    imgSize = [currentImageTk.width, currentImageTk.height]
    offset = [(thumbnailSize - imgSize[0]) / 2, (thumbnailSize - imgSize[1]) / 2,0]
    currentImageTk = ImageTk.PhotoImage(image=currentImageTk)
    currentImageCanvas.create_image(offset[0], offset[1], anchor=NW, image=currentImageTk, tag="image")

def ShowCurrentGlitchThumbnail(img):
    global currentGlitchTk, currentGlitchCanvas
    currentGlitchTk = ConvertImageFromOCVToTkinter(img)
    currentGlitchTk.thumbnail([thumbnailSize, thumbnailSize])
    imgSize = [currentGlitchTk.width, currentGlitchTk.height]
    offset = [(thumbnailSize - imgSize[0]) / 2, (thumbnailSize - imgSize[1]) / 2,0]
    currentGlitchTk = ImageTk.PhotoImage(image=currentGlitchTk)
    currentGlitchCanvas.create_image(offset[0], offset[1], anchor=NW, image=currentGlitchTk, tag="image")

def ShowPreviousGlitchThumbnail(img):
    global previousGlitchTk, previousGlitchCanvas
    previousGlitchTk = ConvertImageFromOCVToTkinter(img)
    previousGlitchTk.thumbnail([thumbnailSize, thumbnailSize])
    imgSize = [previousGlitchTk.width, previousGlitchTk.height]
    offset = [(thumbnailSize - imgSize[0]) / 2, (thumbnailSize - imgSize[1]) / 2,0]
    previousGlitchTk = ImageTk.PhotoImage(image=previousGlitchTk)
    previousGlitchCanvas.create_image(offset[0], offset[1], anchor=NW, image=previousGlitchTk, tag="image")

def AddGlitchHistory(img):
    global glitchHistory, glitchHistorylistBox, currentGlitchType
    glitchHistory.append(img)
    glitchHistorylistBox.insert(len(glitchHistory), (str(len(glitchHistory)), "_", type(currentGlitchType).__name__))
    glitchHistorylistBox.select_clear(0, len(glitchHistory) - 1)
    glitchHistorylistBox.select_set(len(glitchHistory) - 1)
    if len(glitchHistory) >= 2 : ShowPreviousGlitchThumbnail(glitchHistory[len(glitchHistory) - 2])

def DrawSelectionZone(x0, x1, y0, y1):
    global glitchCoordinateRectangles, currentImageCanvas, currentGlitchCanvas, currentImage, currentGlitch
    currentImageThumb = currentImageCanvas.find_withtag("image")
    thumbCoordinates = currentImageCanvas.bbox(currentImageThumb)
    x0 *= (thumbCoordinates[2] - thumbCoordinates[0]) / currentImage.shape[1]
    y0 *= (thumbCoordinates[3] - thumbCoordinates[1]) / currentImage.shape[0]
    x1 *= (thumbCoordinates[2] - thumbCoordinates[0]) / currentImage.shape[1]
    y1 *= (thumbCoordinates[3] - thumbCoordinates[1]) / currentImage.shape[0]
    x0 += thumbCoordinates[0]
    y0 += thumbCoordinates[1]
    x1 += thumbCoordinates[0]
    y1 += thumbCoordinates[1]
    if len(glitchCoordinateRectangles) > 0:
        ClearSelectionZone()
    glitchCoordinateRectangles.append(currentImageCanvas.create_rectangle(x0, y0, x1, y1, width=1, outline='green'))
    glitchCoordinateRectangles.append(currentGlitchCanvas.create_rectangle(x0, y0, x1, y1, width=1, outline='green'))

def ClearSelectionZone():
    global glitchCoordinateRectangles
    if len(glitchCoordinateRectangles) > 0:
            currentImageCanvas.delete(glitchCoordinateRectangles[0])
            currentGlitchCanvas.delete(glitchCoordinateRectangles[1])
            glitchCoordinateRectangles.clear()

from Classes import *
from ClassSelector import *