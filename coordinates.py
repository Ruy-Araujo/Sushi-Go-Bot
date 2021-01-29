
class Cord:
   
# Atributes coordinates

    # Food Stok 
    foodCord = {
        "shrimp" :  (40, 330),
        "rice" :    (85, 330),
        "nori" :    (40, 380),
        "roe" :     (85, 380),
        "salmon" :  (40, 440),
        "unagi" :   (85, 440),
        "sundari" : (195, 385) 
    }
    
    foodId = {
        8587 : "onigiri",
        7442 : "californiaRoll",
        3930 : "gunkanMaki"
    }

    plates = {
        "table1" : (92, 200),
        "table2" : (181,204),
        "table3" : (280,200),
        "table4" : (395,200),
        "table5" : (492,200),
        "table6" : (594,200)
    }
    
    orders = {
        "table1" : False,
        "table2" : False,
        "table3" : False,
        "table4" : False,
        "table5" : False,
        "table6" : False
    }

    phoneMenu = {
        "menuPhone" : (545, 355),
        "menuToppings" : {
            "toppingsButton" : (545, 270),
            "exit" :    (595,335),
            "shrimp" :  (495,220),
            "unagi" :   (575,215),
            "nori" :    (495,275),
            "roe" : (575,275),
            "salmon" :  (495,335)
        },
        "menuRice": {
            "riceButton": (545,295),
            "exit" : (580,335),
            "rice" : (545,280)
        },
        "menuSake": {
            "sakeButton" : (545, 315), 
            "exit" : (580,335),   
            "sake" : (545,275)
        },
        "menuDelivery" : {
            "normal" : (495,295),
            "express" : (575,295)
        }
    }

    foodAvailability = {
        "shrimp" :  (218, 246, 254),
        "unagi" :   (218, 246, 254),
        "nori" :    (218, 246, 254),
        "roe" : (218, 246, 254),
        "salmon" :  (218, 246, 254),
        "rice" :    (236, 166, 171),
        "sake" :    (255, 205, 156)
    }

    foodAvailabilityLocation = {
        "shrimp" :  (522,217),
        "unagi" :   (604,221),
        "nori" :    (520,276),
        "roe" : (593,277),
        "salmon" :  (518,332),
        "rice" :    (567,280),
        "sake" :    (562,273)
    }

    stok = {
        "money" :   0,
        "shrimp" :  5,
        "rice" :    10,
        "nori" :    10,
        "roe" :     10,
        "salmon" :  5,
        "unagi" :   5,
        "sake" :    2   
    }   

    clientOrder = {
        "table1" : (24,58),
        "table2" : (125,58),
        "table3" : (226,58),
        "table4" : (327,58),
        "table5" : (428,58),
        "table6" : (529,58)
    }

