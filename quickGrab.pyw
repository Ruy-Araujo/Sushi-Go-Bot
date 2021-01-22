from PIL import ImageGrab
import os
import time

def screenGrab(x_pad,y_pad):
    box = (x_pad+1,y_pad+1,x_pad+637,y_pad+477)
    im = ImageGrab.grab(box)
    im.save('full_snap__' + str(int(time.time())) + '.png', format='PNG')
 
def main():
    screenGrab(354,167)
 
if __name__ == '__main__':
    main()

def clear():
    """
    Clear all captured images in code folder.
    """
    files = os.listdir()
    for file in files:
        if 'snap' in file:
            os.remove(file)
    print('Trash files are clear')

clear()