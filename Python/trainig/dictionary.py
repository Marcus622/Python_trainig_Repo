# DICTIONARY (dict)

# > Schnellzugriff auf "Schlüssel-Wert-Paare"
# > Veränderbar
# > seit Python v3.7 geordnet
# > in geschweiften Klammern {} geschrieben

# leeres_dict = {}

einkaufsdict = {
    "artikelname": "Banane",
    "Preis": 2,
    "Ablaufdatum": 2024,
    "Farbe": ["gelb, braun",]
    
    }

for i in einkaufsdict:
    print(i)
    print(einkaufsdict[i])





einkaufsdict["Preis"] = 3
print(einkaufsdict.keys())
print(einkaufsdict.values())