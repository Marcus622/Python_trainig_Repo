# Länge eines string herausfinden.
# FUNKTION > einfache Funktion zum Zählen der Bestandteile eines Objekts, z.B. der Buchstaben einer Zeichenkette.
# Strings werden mit + verkettet, Elemente verschiedener Datentypen mit Komma.

y = ("Dieser Satz ist recht lang. Wie lange ist er, wenn ich dies noch hinzufüge?")

print(len(y))


print("Der String mit der Variable y ist", len(y), "Zeichen lang.")

# Buchstaben in Strings verändern. Strings sind unveränderliche Datentypen.

x = "hallo"

x = "H" +x[1:]
print(x)

x = "Hallo"
print(x*10)
# Man Kann auch print("Hallo" * 10) verwenden.
print("Hallo" + "10") # print(Hallo + 10) > Fehler
# print("Hallo" + "10") > funktioniert, aber unveränderbar (falls Variable geändert werden soll,
# reagiert Ausgabebefehl darauf nicht) 
# > Deshalb umwandeln mit str()
print("Hallo" + str(10))

y = 100
print("Hallo" + str(y))

# Funktionen für strings
# z.upper() > Konvertiert in GROSSBUCHSTABEN
# z.lower() > Konvertiert in kleinbuchstaben

z = "Hallo Welt, ich lerne Python"

print(z.upper())

print(z.split())    # Mit z.split() werden Wörter getrennt, mit print(z.split(',')) wird am 
# Komma getrennt

z = 'Ich liebe Python Tutorials <3'

print(z.find('Python'))
print(z[z.find('Python'):])
