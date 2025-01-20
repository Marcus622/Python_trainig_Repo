
# einkaufsliste = []
# entscheidung = "y"

# while entscheidung == "y":
#     einkaufsliste.append(input("Was möchtest Du deiner Liste hinzufügen? "))
#     entscheidung = input("Möchtest Du deiner Liste noch etwas hinzufügen?  (y/n)")

# print(einkaufsliste)

# Endlosschleife mit break
# > statt Bedingungen am Anfang - nur while True
# > läuft endlos
# > Schlüsselwort break an späterer Stelle



#     for-Schleifen

todos = []
for _ in range(3): 
    
    newitem = input("Was möchtest du deiner Liste hinzufügen? ")
    todos.append(newitem)
    print("Meine Liste hat diese Elemente:")
    print(todos)


# todos formatieren

todos = ["Swiebel", "Nabane"]

    
newitem = input("Was möchtest du deiner Liste hinzufügen? ")
todos.append(newitem)
print("Meine Liste hat diese Elemente:")

for todo in todos: 
    print(f" - {todo}")



# for - Schleifen kombinieren

todos = ["Swiebel", "Nabane"]

for _ in range(1):
    newitem = input("Was möchtest du deiner Liste hinzufügen? ")
    todos.append(newitem)
    print("Meine Liste hat diese Elemente:")

    for todo in todos: 
        print(f" - {todo}")

# while Schleifen

# counter = 0

# while counter <= 5:
#     print(counter)
#     counter +=1


# einkaufsliste = []

# # Artikel hinzufügen
# # Aktion -> hinzufügen, entfernen, anzeigen, beenden

# while True:
#     aktion = input("Möchtest Du einen Artikel hinzufügen, entfernen, oder die Liste anzeigen? (hin / ent / anz / bee) ")

#     # hinzufügen
#     if aktion == "hin":
#         artikel = input("Welchen Artikel möchtest Du hinzufügen? ")
#         einkaufsliste.append(artikel)
#         print("Artikel wurde hinzugefügt")


#     # löschen
#     elif aktion == "ent":
#         artikel = input("Welchen Artikel möchtest Du entfernen? ")
#         if artikel in einkaufsliste:
#             einkaufsliste.remove(artikel)
#             print("Artikel gelöscht.")
#         else:
#             print("Artikel gibt es nicht.")

#     # anzeigen
#     elif aktion == "anz":
#         print("Deine Einkaufsliste:")
#         print(einkaufsliste)

#     # beenden
#     elif aktion == "bee":
#         print("Einkaufsliste beendet")
#         break

#     else:
#         print("Du musst das schon richtig eingeben.")