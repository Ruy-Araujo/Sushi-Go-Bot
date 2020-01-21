from PIL import ImageGrab
import os
import time

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
    box = (x_pad+1,y_pad+1,x_pad+637,y_pad+477)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()
