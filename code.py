from PIL import ImageGrab
from coordinates import *
import os
import time
from pynput.mouse import Button, Controller

# --------- Points -----------
"""
Set x_pad y_pad whit your game screem zero point, it's in left-up coner.
Run screenGrab() and look if image is correctly adjusted. 
"""
x_pad = 315     
y_pad = 170

# Mause Comands

def leftClick():
    Controller().press(Button.left)
    Controller().release(Button.left)
    print ("Click.")          #optional, for debugging purposes.

def mousePos(cord):
    Controller().position = ((x_pad + cord[0], y_pad + cord[1]))
     
# Capture Tools 

def screenGrab(x_pad,y_pad):
    box = (x_pad+1,y_pad+1,x_pad+637,y_pad+477)
    im = ImageGrab.grab(box)
    #im.save('full_snap__' + str(int(time.time())) + '.png', format='PNG')
    return im

def clear():
    """
    Clear all captured images in code folder.
    """
    files = os.listdir()
    for file in files:
        if 'snap' in file:
            os.remove(file)
    print('Trash files are clear')

def getCords():
    x,y = Controller().position         # Get the cursor position on Linux
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def capture():
    for i in range(6):
        time.sleep(1.5)
        getCords()

def getStatus(item):
    sg = screenGrab(x_pad,y_pad)
    cords, avaib = Cord.phoneMenu, Cord.foodAvailability
    if item in ('shrimp','unagi','nori','fishEgg','salmon'):
        pixel = sg.getpixel(cords["menuToppings"][item])
        if pixel == avaib[item]:
            return True
        else:
            return False
    elif item == 'rice':
        pixel = sg.getpixel(cords["menuRice"][item])
        if pixel == avaib[item]:
            return True
        else:
            return False
    elif item == 'sake':
        pixel = sg.getpixel(cords["menuSake"][item])
        if pixel == avaib[item]:
            return True
        else:
            return False
    
# Start Game 

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

# Cooking

def makeFood(food):

    def rollSundari():
        mousePos(Cord.food['sundari'])
        leftClick()
        time.sleep(.8)

    if food == 'onigiri':
        """
        Recipe: 2 rice 1 nori.
        """
        mousePos(Cord.food['rice'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.food['rice'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.food['nori'])
        leftClick()
        
    elif food == 'californiaRoll':
        """
        Recipe: 1 rice 1 nori 1 roe.
        """
        mousePos(Cord.food['rice'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.food['nori'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.food['roe'])
        leftClick() 

    elif food == 'gunkanMaki':
        """
        Recipe: 1 rice 1 nori 2 roe.
        """
        mousePos(Cord.food['rice'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.food['nori'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.food['roe'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.food['roe'])
        leftClick()
      
    time.sleep(.1)
    rollSundari()


cord = Cord()

def clearTables():
    tables = cord.tablesCords()
    for table in tables:
        mousePos(tables[table])
        leftClick()
    time.sleep(.5)
    
def buyToppings(item):
    cords = Cord.phoneMenu
    mousePos(cords["menuPhone"])
    leftClick()
    time.sleep(.1)
    mousePos(cords["menuToppings"]["toppingsButton"])
    leftClick()
    time.sleep(.1)
    mousePos(cords["menuToppings"][item])
    leftClick()
    time.sleep(.1)
    mousePos(cords["menuDelivery"]["normal"])
    leftClick()
    time.sleep(.1)

def buyRice():
    cords = Cord.phoneMenu
    mousePos(cords["menuPhone"])
    leftClick()
    time.sleep(.1)
    mousePos(cords["menuRice"]["riceButton"])
    leftClick()
    time.sleep(.1)
    mousePos(cords["menuRice"]["rice"])
    leftClick()
    time.sleep(.1) 
    mousePos(cords["menuDelivery"]["normal"])
    leftClick()
    time.sleep(.1)  

def buySake():
    cords = Cord.phoneMenu
    mousePos(cords["menuPhone"])
    leftClick()
    time.sleep(.1)
    mousePos(cords["menuSake"]["sakeButton"])
    leftClick()
    time.sleep(.1)
    mousePos(cords["menuSake"]["sake"])
    leftClick()
    time.sleep(.1) 
    mousePos(cords["menuDelivery"]["normal"])
    leftClick()
    time.sleep(.1)  





#startGame()
#time.sleep(1)
"""for _ in range(3):
    makeFood('onigiri')
    makeFood('californiaRoll')
    makeFood('gunkanMaki')"""

print(getStatus('shrimp'))
print(getStatus('unagi'))
print(getStatus('nori'))
print(getStatus('fishEgg'))
print(getStatus('salmon'))
print(getStatus('rice'))
print(getStatus('sake'))

