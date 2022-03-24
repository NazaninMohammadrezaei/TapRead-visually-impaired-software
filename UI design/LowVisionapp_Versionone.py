from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2 as cv
import pytesseract
import re
import pyttsx3

# Load the user interface
app = QtWidgets.QApplication([])
dlg = uic.loadUi("LowVisionapp_Versionone.ui")

# Present the picture
picture_path = 'C:/Users/chortkeh/desktop/TapRead/Sample_Image/booktext.jpg'
pixmap = QPixmap(picture_path)
dlg.label_3.setPixmap(pixmap)

# Set the spin box
dlg.spinBox.setValue(10)
dlg.spinBox.setMaximum(28)
dlg.spinBox.setMinimum(10)
dlg.spinBox.setSingleStep(2)

# Read tesseract.exe for Optical-Character-Recognition
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Extract text from an image and convert it to speech 
def Image_To_Speech():
    global text

    # Read the image
    img = cv.imread(picture_path)

    # Extract the embedded text from the image
    text = pytesseract.image_to_string(img)

    # Remove extra characters in the text
    result = re.sub("[^A-Za-z0-9]"," ",text)
    dlg.textEdit.setText(result)
    dlg.textEdit.setFont(QFont('Segoe UI', 10))

    # Convert text into speech
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(result)    
    engine.runAndWait()


# Change the font size when spin box was used
def Change_Font_Size():
    dlg.textEdit.setFont(QFont('Segoe UI',dlg.spinBox.value()))    
dlg.spinBox.valueChanged.connect(Change_Font_Size)


# when the user pushed "Read It!" button
dlg.pushButton_ReadIt.clicked.connect(Image_To_Speech)


dlg.show()
app.exec()
