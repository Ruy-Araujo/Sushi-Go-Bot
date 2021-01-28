from PIL import ImageGrab,ImageOps
import os
import time
from numpy import *

x_pad = 363
y_pad = 206

def screenGrab(x_pad,y_pad):
    box = (x_pad+1,y_pad+1,x_pad+637,y_pad+477)
    im = ImageGrab.grab(box)
    im.save('full_snap__' + str(int(time.time())) + '.png', format='PNG')

def main():
    screenGrab()
    
"""if __name__ == '__main__':
    main()"""

def clear():
    """
    Clear all captured images in code folder.
    """
    files = os.listdir()
    for file in files:
        if 'snap' in file:
            os.remove(file)
    print('Trash files are clear')

def grab():
    box = (x_pad + 1,y_pad+1,x_pad+640,y_pad+480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    return a
"""
  a = array(im.getcolors())
    a = a.sum()
    print (a)
    return a
"""

clear()
screenGrab(x_pad,y_pad)
