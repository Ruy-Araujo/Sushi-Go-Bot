
class Cord:
   
# Atributes coordinates

    # Food Stok 
    food = {
        "shrimp" :  (40, 330),
        "rice" :    (85, 330),
        "nori" :    (40, 380),
        "roe" :     (85, 380),
        "salmon" :  (40, 440),
        "unagi" :   (85, 440),
        "sundari" : (195, 385) 
    }
    
    # Plate Locations
    tables = {
        "table_1" : (92, 200),
        "table_2" : (181,204),
        "table_3" : (280,200),
        "table_4" : (395,200),
        "table_5" : (492,200),
        "table_6" : (594,200)
    }
    
    # Phone Locations
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

    clients = {
        "table1" : {
            "foodLocal" : (54,70),
            "onigiri" : (107, 107, 79),
            "californiaRoll" : (187, 190, 178),
            "gunkanMaki" : (67, 62, 27)
        },
         "table2" : {
            "foodLocal" : (154,70),
            "onigiri" : (108, 108, 81),
            "californiaRoll" : (187, 190, 178),
            "gunkanMaki" : (67, 62, 27)
        },
         "table3" : {
            "foodLocal" : (256,70),
            "onigiri" : (107, 107, 79),
            "californiaRoll" : (187, 190, 178),
            "gunkanMaki" : (67, 62, 27)
        },
         "table4" : {
            "foodLocal" : (358,70), 
            "onigiri" : (67, 62, 27),
            "californiaRoll" : (193, 195, 184),
            "gunkanMaki" : (67, 62, 27)
        },
         "table5" : {
            "foodLocal" : (457,70),
            "onigiri" : (108, 108, 81),
            "californiaRoll" : (187, 190, 178),
            "gunkanMaki" : (67, 62, 27)
        },
         "table6" : {
            "foodLocal" : (560,70),
            "onigiri" : (67, 62, 27),
            "californiaRoll" : (0),
            "gunkanMaki" : (67, 62, 27)
        }
    }

# Methods


    
"""


        

"""