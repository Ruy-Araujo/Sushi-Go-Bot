from PIL import ImageGrab,ImageOps
from pynput.mouse import Button, Controller
import os,time
from numpy import *
from coordinates import *
# --------- Points -----------
"""
Set x_pad y_pad whit your game screem zero point, run getCords() in left-up coner.
Run screenGrab() and look if image is correctly adjusted. 
"""
x_pad = 363      
y_pad = 206

# Mause Comands

def leftClick():
    Controller().press(Button.left)
    Controller().release(Button.left)
    #print ("Click.")          #optional, for debugging purposes.

def mousePos(cord):
    Controller().position = ((x_pad + cord[0], y_pad + cord[1]))
     
# ---- Capture Tools 

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
    return (x,y)

def capture():
    for i in range(6):
        time.sleep(1.5)
        getCords()

def status(item):
    """
    Return if item is avalieble or not 
    
    Itens list:
    - shrimp
    - unagi
    - nori
    - roe
    - salmon
    - rice
    - sake 
    """
    sg = screenGrab(x_pad,y_pad)
    cords, avaib = Cord.foodAvailabilityLocation, Cord.foodAvailability
    pixel = sg.getpixel(cords[item])
    if pixel == avaib[item]:
        print(f"{item} is avalible to buy")
        return True
    else:
        print(f"{item} is NOT avalible to buy")
        return False

def getPixel(tuple):
    sg = screenGrab(x_pad,y_pad)
    print(sg.getpixel(tuple))
    return sg.getpixel(tuple)

def getSeat(table):
    """Return cliet order ID"""
    leftCorn = list(Cord.clientOrder[table])
    leftCorn[0] += x_pad
    leftCorn[1] += y_pad
    box = (leftCorn[0],leftCorn[1],leftCorn[0]+58,leftCorn[1]+15)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #im.show()    # Debug
    #print(f"Id of order in {table} is: {a}")
    return a

# ---- Start Game 

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

# ---- Cooking

def makeFood(food):
    """
    Recipes onigiri, californiaRoll, gunkaMaki
    """
    def rollSundari():
        mousePos(Cord.foodCord['sundari'])
        leftClick()
        time.sleep(.8)

    if food == 'onigiri':
        """
        Recipe: 2 rice 1 nori.
        """
        mousePos(Cord.foodCord['rice'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.foodCord['rice'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.foodCord['nori'])
        leftClick()
        Cord.stok['rice'] -= 2
        Cord.stok['nori'] -= 1

    elif food == 'californiaRoll':
        """
        Recipe: 1 rice 1 nori 1 roe.
        """
        mousePos(Cord.foodCord['rice'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.foodCord['nori'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.foodCord['roe'])
        leftClick() 
        Cord.stok['rice'] -= 1
        Cord.stok['nori'] -= 1
        Cord.stok['roe'] -= 1

    elif food == 'gunkanMaki':
        """
        Recipe: 1 rice 1 nori 2 roe.
        """
        mousePos(Cord.foodCord['rice'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.foodCord['nori'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.foodCord['roe'])
        leftClick()
        time.sleep(.1)
        mousePos(Cord.foodCord['roe'])
        leftClick()
        Cord.stok['rice'] -= 1
        Cord.stok['nori'] -= 1
        Cord.stok['roe'] -= 2
      
    time.sleep(.1)
    rollSundari()
    time.sleep(1)
    print(f'make {food}') # debug

def clearTable(table):
    plate = Cord.plates[table]
    mousePos(plate)
    time.sleep(.1)
    leftClick()
    print(f'{table} are clear')
    
def buy(item):
    """
    Buy itens.
    Itens list:
    - shrimp
    - unagi
    - nori
    - roe
    - salmon
    - rice
    - sake
    """
    cords = Cord.phoneMenu
    mousePos(cords["menuPhone"])
    leftClick()
    time.sleep(.1)
    if item in ("shrimp","unagi","nori","roe","salmon"):
        mousePos(cords["menuToppings"]["toppingsButton"])
        leftClick()
        time.sleep(.3)
    elif item == "rice":
        mousePos(cords["menuRice"]["riceButton"])
        leftClick()
        time.sleep(.3)
    elif item == "sake":
        mousePos(cords["menuSake"]["sakeButton"])
        leftClick()
        time.sleep(.3)
    if status(item):
        if item in ("shrimp","unagi","nori","roe","salmon"):
            mousePos(cords["menuToppings"][item])
            leftClick()
            time.sleep(.1)
            if item in ("shrimp","unagi"):
                Cord.stok[item] += 5
                Cord.stok["money"] -= 350  
            if item == "nori":
                Cord.stok["nori"] += 10
                Cord.stok["money"] -= 100
            if item == "roe":
                Cord.stok["roe"] += 10
                Cord.stok["money"] -= 200
            if item == "salmon":
                Cord.stok["salmon"] += 5
                Cord.stok["money"] -= 300
        elif item == "rice":
            mousePos(cords["menuRice"]["rice"])
            leftClick()
            time.sleep(.1) 
            Cord.stok["rice"] += 10
            Cord.stok["money"] -= 100
        elif item == "sake":
            mousePos(cords["menuSake"]["sake"])
            leftClick()
            time.sleep(.1) 
            Cord.stok["salmon"] += 2
            Cord.stok["money"] -= 100
        mousePos(cords["menuDelivery"]["normal"])
        leftClick()
        time.sleep(1)
        return True
    else:                   
        print(f'{item} is not avaliable to buy')
        if item in ("shrimp","unagi","nori","roe","salmon"):
            mousePos(cords["menuToppings"]["exit"])
            leftClick()
            time.sleep(.1)
        else:
            mousePos(cords["menuRice"]["exit"])
            leftClick()
            time.sleep(.1)
        return False

def checkStok():
    for food in Cord.stok:
        print(f"{food} has {Cord.stok[food]} left")
        if Cord.stok[food] <= 4:
            if food == "money":
                pass
            elif food == "sake":
                pass
            else:
                buy(food)  
                print(f'Buy {food}')
                
def main():
    startGame()
    time.sleep(1)
    while True:
        for table in Cord.clientOrder:
            order = getSeat(table)
            if order in (8587,7442,3930):
                if not Cord.orders[table]:         
                    checkStok()
                    makeFood(Cord.foodId[order])
                    Cord.orders[table] = True
            else:
                print (f"{table} unoccupied")
                clearTable(table)
                Cord.orders[table] = False
        time.sleep(1)

main()