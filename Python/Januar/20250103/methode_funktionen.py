
# Funktion: Eine Funktion in Python ist ein Block von Code, der ausgeführt wird, wenn er aufgerufen wird. Funktionen können unabhängig von Klassen oder 
# Objekten existieren.

# Funktion, die zwei Zahlen addiert
def addiere(x, y):
    return x + y

# Funktion aufrufen
resultat = addiere(5, 3)
print(resultat)  # Ausgabe: 8




# Methode: Eine Methode ist eine Funktion, die an ein Objekt oder eine Instanz einer Klasse gebunden ist. Sie wird immer in Verbindung mit einem 
# Objekt oder einer Instanz aufgerufen.

class Auto:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell

    # Methode, die die Auto-Details anzeigt
    def anzeigen(self):
        return f"{self.marke} {self.modell}"

# Instanziierung eines Auto-Objekts
mein_auto = Auto("BMW", "X5")

# Methode aufrufen
print(mein_auto.anzeigen())  # Ausgabe: BMW X5


# Anwendungen und Unterschiede in der Praxis

# Funktionen:

# Funktionen sind ideal für allgemeine Operationen, die keine Beziehung zu einer bestimmten Instanz oder einem Objekt haben.
# Beispielanwendungen:
# Berechnungen (wie mathematische Operationen).
# Hilfsfunktionen zur Bearbeitung von Daten.
# Funktionen für die Dateiverarbeitung oder Netzwerkanfragen.

# Methoden:

# Methoden sind speziell dafür da, Operationen an den Daten eines Objekts oder einer Instanz durchzuführen.
# Beispielanwendungen:
# Objektverhalten (z. B. eine Methode, die den Zustand eines Objekts verändert oder Informationen über das Objekt bereitstellt).
# Interaktion mit Instanzdaten.

class Bankkonto:
    def __init__(self, inhaber, saldo=0):
        self.inhaber = inhaber
        self.saldo = saldo

    def einzahlen(self, betrag):
        self.saldo += betrag

    def abheben(self, betrag):
        if betrag <= self.saldo:
            self.saldo -= betrag
        else:
            print("Nicht genug Guthaben")

    def anzeigen(self):
        return f"Kontoinhaber: {self.inhaber}, Guthaben: {self.saldo}"

# Instanziierung des Bankkontos
mein_konto = Bankkonto("Max Mustermann", 1000)

# Methoden aufrufen
mein_konto.einzahlen(500)
mein_konto.abheben(200)
print(mein_konto.anzeigen())  # Ausgabe: Kontoinhaber: Max Mustermann, Guthaben: 1300


# Zusammenfassung:
# Funktionen: Werden unabhängig von Objekten verwendet und dienen allgemeinen Aufgaben.
# Methoden: Sind an Objekte oder Klassen gebunden und dienen dazu, das Verhalten und die Interaktionen mit diesen Objekten zu definieren.
# Der Hauptunterschied liegt also darin, dass Methoden immer in Bezug auf Objekte oder Instanzen aufgerufen werden, während Funktionen unabhängiger und 
# vielseitiger sind.



class Rechner:
    def addieren(self, a ,b):
        return a+b
    
mein_rechner = Rechner()
print(mein_rechner.addiere(2,3))