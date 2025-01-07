

# gerichte = []
# for _ in range (3):
#     print("Hallo")

# counter = 0

# while  counter < 3:
#     print("Hallo von while")
#     counter = counter + 1

# gerichte = []

# for _ in range (3):
#     user_input = input("Gib dein Lieblingsgericht ein: ")
#     gerichte.append(user_input)
#     print(f"Meine aktuelle Liste: {gerichte}")

# for ge in gerichte:
#     print(f"Mein Lieblingsgericht: {ge}")


# weekdays = ["Montag", "Dienstag", "Mittwoch"]
# food = []
# for w in weekdays:
#     for _ in range(2):
#         food_input = input(f"Was möchtest du am {w} essen? ")
#         food.append(food_input)
# print(f"Der Essensplan für die gesamte Woche sieht wie folgt aus: {food}")



# # Aufgabe 1

# # Benutzer gibt den Text und Buchstaben ein.
# text = input("Gib einen Text ein: ")
# buchstabe = input("Gib den Buchstaben ein, den du zählen möchtest: ")


# # Sicherstellen, dass der Benutzer nur ein einzelnes Zeichen eingibt
# if len(buchstabe) !=1:
#     print("Gib nur einen Buchstaben ein.")


# else:
#     # Zähler für die Häufigkeit des Buchstabens
#     häufigkeit = 0

# # Schleife, die jeden Buchstaben im Text überprüft
#     for zeichen in text:
#         if zeichen == buchstabe:
#             häufigkeit +=1

#     print(f"Der Buchstabe {buchstabe} kommt {häufigkeit} mal im Text vor.")


#     # Aufgabe 2

# # Variablen für die Summe und die Anzahl er eingegebenen Zahlen.
#     summe = 0
#     anzahl = 5

# # Schleife, die den Benutzer fünf Zahlen eingeben lässt.
#     for i in range(anzahl):
#         zahl = float(input(f"Gib die {i+1}. Zahl ein. ")) # Eingabe der Zahlen.
#         summe += zahl # Die Zahl zur Summe hinzufügen.
    
#     # Berechnung des Durchschnitts.
#     durchschnitt = summe / anzahl

# # Ausgabe der Ergebnisse.
#     print(f"Die Summe der Zahlen ist {summe}")
#     print(f"Der Durchschnitt der Zahlen ist {durchschnitt}")



    # Aufgabe 3

    # Benutzer gibt die Anzahl der Zeilen ein
zeilen = int(input("Gib die Anzahl der Zeilen ein: "))

# Verschachtelte Schleife, um das Muster zu erzeugen
for i in range(1, zeilen + 1):  # Äußere Schleife für die Zeilen
    for j in range(i):  # Innere Schleife für die Sterne in jeder Zeile
        print("*", end="")  # Ein Stern wird ohne Zeilenumbruch ausgegeben
    print()  # Neue Zeile nach jedem Durchlauf der inneren Schleife

