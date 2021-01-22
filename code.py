from PIL import ImageGrab
from coordinates import *
import os
import time
#import win32api, win32con
from pynput.mouse import Button, Controller


# --------- Points -----------
"""
Set x_pad y_pad whit your game screem zero point, it's in left-up coner.
Run screenGrab() and look if image is correctly adjusted. 
"""
x_pad = 354     
y_pad = 167

# --------- Mause Comands -------------

def leftClick():
    Controller().press(Button.left)
    Controller().release(Button.left)
    print ("Click.")          #optional, for debugging purposes.

def mousePos(cord):
    Controller().position = ((x_pad + cord[0], y_pad + cord[1]))
     
# ------- Capture Tools ----------

def getCords():
    x,y = Controller().position         # Get the cursor position on Linux
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def capture():
    for i in range(6):
        time.sleep(1.5)
        getCords()
        
# ----------- Start Game ----------------

def startGame():
    #location of start button
    mousePos((310, 202))
    leftClick()
    time.sleep(.1)
     
    #location of skip donwload app
    mousePos((309, 389))
    leftClick()
    time.sleep(.1)
     
    #location of skip button
    mousePos((580, 450))
    leftClick()
    time.sleep(.1)
     
    #location of continue button
    mousePos((310, 372))
    leftClick()
    time.sleep(.1)

# --------- Recipes ---------

cord = Cord()

def rollSundari():
    mousePos(cord.sundari)
    leftClick()
    time.sleep(.8)

def onigiri():
    """
    Recipe: 2 rice 1 nori.
    """
    mousePos(cord.f_rice)
    leftClick()
    time.sleep(.1)
    mousePos(cord.f_rice)
    leftClick()
    time.sleep(.1)
    mousePos(cord.f_nori)
    leftClick()
    time.sleep(.1)
    rollSundari()
     
def californiaRoll():
    """
    Recipe: 1 rice 1 nori 1 roe.
    """
    mousePos(cord.f_rice)
    leftClick()
    time.sleep(.1)
    mousePos(cord.f_nori)
    leftClick()
    time.sleep(.1)
    mousePos(cord.f_roe)
    leftClick()
    time.sleep(.1)
    rollSundari()
     
def gunkanMaki():
    """
    Recipe: 1 rice 1 nori 2 roe.
    """
    mousePos(cord.f_rice)
    leftClick()
    time.sleep(.1)
    mousePos(cord.f_nori)
    leftClick()
    time.sleep(.1)
    mousePos(cord.f_roe)
    leftClick()
    time.sleep(.1)
    mousePos(cord.f_roe)
    leftClick()
    time.sleep(.1)
    rollSundari()



