
def finde_groesste_zahl(liste): # Diese Funktion nimmt eine Liste von Zahlen und findet die größte Zahl in dieser Liste.
    # Prüfen, ob die Liste leer ist
    if len(liste) == 0: # len zählt die Zeichen in der Liste. Ist keines vorhanden, gibt return none aus
        return None
    
    # Setze die erste Zahl als größte Zahl
    groesste_zahl = liste[0] # Hier wird die erste Zahl als groesste_zahl angenommen.
    
    # Durchlaufe die Liste und vergleiche jede Zahl
    for zahl in liste:          # Mit der for Schleife wird eine Wiederholungsprüfung eingeleitet, welche in der Liste
                                # die erste Zahl mit der nächsten vergleicht. Ist die Zahl in diesem Falle kleiner, 
                                # wird sie übersprungen und der Vergleich findet mit der nächsten statt. 
        if zahl > groesste_zahl:# Ist eine Zahl grösser, wird sie als groesste_zahl ersetzt und der Vergleich wird fortgesetzt.
            groesste_zahl = zahl
    
    # Rückgabe der größten Zahl
    return groesste_zahl        # Ist die Schleife durchgelaufen, wird die grösste Zahl an die Funktion zurückgegeben.

# Funktion zur Berechnung der Summe und Anzahl der ungeraden Zahlen im Bereich
def berechne_ungerade_zwischen(zahl1, zahl2): # Diese Funktion soll die ungeraden Zahlen im Bereich der eingegebenen addieren.
    # Initialisiere Summe und Zähler
    summe = 0 # Hier wird die erste Zahl als Beginn festgelegt.
    anzahl = 0
    
    # Schleife durch den Bereich von zahl1 bis zahl2
    for zahl in range(zahl1, zahl2 + 1): # Das + 1 bei zahl2 sorgt dafür, dass zahl2 selbst in die Schleife 
        # einbezogen wird, da range normalerweise den Endwert ausschließt.
        # Überprüfe, ob die Zahl ungerade ist
        if zahl % 2 != 0: # Der Modulo-Operator % gibt den Restwert einer Division zurück. zahl% 2 teilt die Zahl 
            # durch 2 und gibt den Restwert zurück. Ist er ungleich 0 (!= 0) befeutet es, dass die Zahl nicht 
            # gleichmässig durch 2 teilbar und daher ungerade ist.
            summe += zahl
            anzahl += 1
    
    # Rückgabe der Summe und der Anzahl der ungeraden Zahlen
    return summe, anzahl

# Eingabe der beiden Zahlen
zahl1 = int(input("Gib die erste Zahl ein: ")) # Aufforderung zur Zahleneingabe und konvertierung in eine Ganzzahl.
zahl2 = int(input("Gib die zweite Zahl ein: ")) # Eingaben werden in Variablen zahl1 und zahl2 gespeichert.

# Berechnung der Summe und Anzahl der ungeraden Zahlen im Bereich
summe, anzahl = berechne_ungerade_zwischen(zahl1, zahl2)

# Ausgabe der Ergebnisse
print(f"Die Summe der ungeraden Zahlen im Bereich von {zahl1} bis {zahl2} ist: {summe}")
print(f"Die Anzahl der ungeraden Zahlen im Bereich von {zahl1} bis {zahl2} ist: {anzahl}")

# Beispiel-Liste und Aufruf der Funktion zur Bestimmung der größten Zahl
liste = [15, 33, 2, 85, 90, 13 ,55, 78]  # Liste, welche die Zahlen definiert, die von der Schleife durchlaufen wird.
groesste = finde_groesste_zahl(liste)
print("Die größte Zahl in der Liste ist:", groesste) # Gibt die größte Zahl aus.
