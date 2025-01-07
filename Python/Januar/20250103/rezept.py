

# 1.1 Implementiere folgendes UML Klassendiagramm:
# Zutat
# name: str 
# kalorien_pro_100g: int
# zubereitungszeit: int

class Zutat:
    def __init__(self, name, kalorien, zubereitungszeit):
        # Initialisiert die Zutat mit den gegebenen Eigenschaften
        self.name = name
        self.kalorien_pro_100g = int(kalorien)  # Kalorien pro 100g
        self.zubereitungszeit = int(zubereitungszeit)  # Zubereitungszeit in Minuten

    def __str__(self):
        # Gibt eine lesbare Darstellung der Zutat zurück
        return f"Zutat: {self.name}, Kalorien pro 100g: {self.kalorien_pro_100g}, Zubereitungszeit: {self.zubereitungszeit} Minuten."


class Rezept:
    def __init__(self, name, beschreibung):
        # Initialisiert das Rezept mit Namen, Beschreibung und einer leeren Zutatenliste
        self.name = name
        self.beschreibung = beschreibung
        self.zutatenliste = {}

    def zutat_hinzufügen(self, zutat, menge):
        """
        Fügt eine Zutat und die entsprechende Menge zum Rezept hinzu.
        Menge sollte als String übergeben werden (z. B. "200g", "1 Prise").
        """
        self.zutatenliste[zutat] = menge

    def kalorien(self):
        """
        Berechnet die Gesamtkalorien des Rezepts, indem die Kalorien aller Zutaten
        unter Berücksichtigung ihrer Menge zusammengezählt werden.
        """
        gesamt_kalorien = 0
        for zutat, menge in self.zutatenliste.items():
            # Kalorien pro Zutat pro 100g werden zur Gesamtzahl addiert
            gesamt_kalorien += zutat.kalorien_pro_100g
        print(f"Gesamtkalorien im Rezept: {gesamt_kalorien} kcal")

    def zubereitungszeit(self):
        """
        Berechnet die Gesamtzubereitungszeit des Rezepts, indem die Zubereitungszeiten
        aller Zutaten zusammengezählt werden.
        """
        gesamt_zeit = 0
        for zutat in self.zutatenliste:
            gesamt_zeit += zutat.zubereitungszeit
        print(f"Gesamtzubereitungszeit im Rezept: {gesamt_zeit} Minuten")


# Beispiel: Erstellen von Zutaten
zutat1 = Zutat("Mehl", 364, 5)
zutat2 = Zutat("Eier", 155, 2)
zutat3 = Zutat("Milch", 42, 3)

# Erstellen eines Rezepts
rezept = Rezept("Pfannkuchen", "Super lecker und einfach zuzubereiten!")

# Zutaten zum Rezept hinzufügen
rezept.zutat_hinzufügen(zutat1, "200g")
rezept.zutat_hinzufügen(zutat2, "2 Stück")
rezept.zutat_hinzufügen(zutat3, "300ml")

# Ausgabe der Beschreibung des Rezepts
print(rezept.beschreibung)

# Berechnung der Kalorien und Zubereitungszeit
rezept.kalorien()
rezept.zubereitungszeit()
