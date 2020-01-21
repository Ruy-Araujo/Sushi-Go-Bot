from PIL import ImageGrab
import os
import time
import win32api, win32con


# ----- Points ------

x_pad = 364
y_pad = 136

""" 
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.

x_pad = 156
y_pad = 345
Play area =  x_pad+1, y_pad+1, 796, 825
"""

def screenGrab():
    box = (x_pad,y_pad,x_pad+638,y_pad+478)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 

def main():
    pass

if __name__ == '__main__':
    main()

 
# --------- Mause Comands -------------

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ("Click.")          #completely optional. But nice for debugging purposes.


'''
The next two are the exact same thing, but now each step is split into its own function. These will be used when we need to hold down the mouse for a length of time (for dragging, shooting, etc..).

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left release')
'''

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     
def get_cords():
    x,y = win32api.GetCursorPos()		# Get the cursor position on Win32api
    x = x - x_pad
    y = y - y_pad
    print (x,y)

# ------- Capture Tools ----------

def capture():
    for i in range(6):
        time.sleep(1.5)
        get_cords()
        

# ----------- Start Game ----------------

def startGame():
    #location of start button
    mousePos((310, 202))
    leftClick()
    time.sleep(.1)
     
    #location of skip donwload app
    mousePos((309, 386))
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

# ----------- Food Stok -------------

class Cord:
     
    f_shrimp = (40,330)
    f_rice = (85 330)
    f_nori = (40 380)
    f_roe = (85 380)
    f_salmon = (40 440)
    f_unagi = (85 440)

# --------- Plate Locations ---------

"""
 92 210
194 210
292 210
400 210
493 210
594 210
"""



