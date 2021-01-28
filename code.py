from PIL import ImageGrab
from coordinates import *
import os
import time
from pynput.mouse import Button, Controller
from quickGrab import *

# --------- Points -----------
"""
Set x_pad y_pad whit your game screem zero point, it's in left-up coner.
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
        Cord.stok['rice'] -= 2
        Cord.stok['nori'] -= 1

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
        Cord.stok['rice'] -= 1
        Cord.stok['nori'] -= 1
        Cord.stok['roe'] -= 1

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
        Cord.stok['rice'] -= 1
        Cord.stok['nori'] -= 1
        Cord.stok['roe'] -= 2
      
    time.sleep(.1)
    rollSundari()
    print(f'make {food}') # debug

def clearTables():
    tables = Cord.tables
    for table in tables:
        mousePos(tables[table])
        time.sleep(.3)
        leftClick()
    print('tables are clear')
    
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
        time.sleep(.1)
    else:                   
        print(f'{item} is not avaliable')
        if item in ("shrimp","unagi","nori","roe","salmon"):
            mousePos(cords["menuToppings"]["exit"])
            leftClick()
            time.sleep(.1)
        else:
            mousePos(cords["menuRice"]["exit"])
            leftClick()
            time.sleep(.1)

def checkStok():
    for food in Cord.stok:
        print(f"{food} has {Cord.stok[food]} left")
        if Cord.stok[food] <= 3:
            if food == "money":
                pass
            elif food == "sake":
                pass
            else:
                buy(food)    
                print(f'Buy {food}')

"""
def buyRice():
    cords = Cord.phoneMenu
    mousePos(cords["menuPhone"])
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
    
    
    mousePos(cords["menuDelivery"]["normal"])
    leftClick()
    time.sleep(.1)  
"""

#startGame()
#time.sleep(1)

"""
for _ in range(3):
    checkStok()
    makeFood('onigiri')
    time.sleep(1)
    checkStok()
    makeFood('californiaRoll')
    time.sleep(1)
    checkStok()
    makeFood('gunkanMaki')
    time.sleep(1)
    clearTables()
"""

"""
print(status('shrimp'))
print(status('unagi'))
print(status('nori'))
print(status('roe'))
print(status('salmon'))
print(status('rice'))
print(status('sake'))
"""

"""
sg = screenGrab(x_pad,y_pad)
print(sg.getpixel(getCords()))
"""

#getCords()

#clearTables()

#buy("rice")

def getCliente():
    for table in Cord.clients:
        for item in Cord.clients[table]:
            if item == "foodLocal":
                print(f"{table} - {Cord.clients[table][item]}")
                getPixel((Cord.clients[table][item]))
                main()

#getCords()
"""clear()
getCliente()"""

def main():
    #startGame()
    #time.sleep(1)
    for table in Cord.clients:
        for food in Cord.clients[table]: 
           verify = getPixel((Cord.clients[table][food]))
           if verify == food:
               print(f'is it {food}')

main()