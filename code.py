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
x_pad = 314     
y_pad = 170

# --------- Mause Comands -------------

def leftClick():
    if os.name == 'posix':
        posix_leftClick()
    elif os.name == 'nt':
        nt_leftClick()

def posix_leftClick():
    Controller().press(Button.left)
    Controller().release(Button.left)
    print ("Click.")          #optional, for debugging purposes.  

def nt_leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ("Click.")          #optional, for debugging purposes.  

def mousePos(cord):
    if os.name == 'posix':
        posix_mousePos(cord)
    elif os.name == 'nt':
        nt_mousePos(cord)

def posix_mousePos(cord):
    Controller().position = ((x_pad + cord[0], y_pad + cord[1]))

def nt_mousePos(Cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     
# ------- Capture Tools ----------

def getCords():
    if os.name == 'posix':
        posix_getCords()
    elif os.name == 'nt':
        nt_getCords()
        
def posix_getCords():
    x,y = Controller().position         # Get the cursor position on Linux
    x = x - x_pad
    y = y - y_pad
    print(x,y)


def nt_getCords():
    x,y = win32api.GetCursorPos()		# Get the cursor position on Win32api
    x = x - x_pad
    y = y - y_pad
    print (x,y)

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



