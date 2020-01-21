import time

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
    print 'left Down'
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'
'''

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1])
     
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

