# TIC TAC TOE


# > Zeile auswählen
# > Spalte auswählen
# > Marker setzen
#   > Check: Feld leer?
# > Sieg? Unentschieden?
# > Spielbrett nochmal anzeigen.

# 1. Spielbrett erstellen

def erstelle_brett():
    brett = []
    
    for i in range(3):
        zeile = [" "," "," "]
        brett.append(zeile)
    return(brett)

# 2. Spielbrett ausgeben

def drucke_brett(brett):
    for zeile in brett:
        print("|".join(zeile))
        print("------")

def spiele_tic_tac_toe():
    brett = erstelle_brett()
    aktueller_spieler = "X"

    while True:
        drucke_brett(brett)

