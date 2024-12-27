

# Aufgaben für den Nachmittag: Python-Code in Arbeitsschritte beschreiben

# **Abgabe**: Text ()

## Aufgabe 1: Einfache Entscheidungen mit `if`-Statements (25 Punkte)

#**Ziel:** Verstehen, wie Entscheidungen im Code in Arbeitsschritte übersetzt werden können.

# Code-Beispiel:


zahl = int(input("Gib eine Zahl ein: ")) # Diese Funktion zeigt dem Benutzer durch 'input', dass er eine Zahl eingeben muss. Durch die "" erfolgt eine Formatierung als String (Zeichenkette).
# Um mit der Zahl arbeiten zu können, muss der String in eine Ganzzahl (Integer) umgewandelt werden. Dies geschieht durch den Aufruf von int(), das den String in eine Zahl umwandelt.
# Gibt der Benutzer keine gültige Zahl ein, wird ein Fehler ausgelöst. Die umgewandelte Zahl wird in der Variablen Zahl gespeichert, die nun die vom Benutzer eingegebene Zahl enthält.


if zahl > 10:                               # Hier beginnt die Bedingung. Es wird überprüft, ob die eingelesene Zahl größer als 10 ist. Falls dies wahr ist, d.h. die Zahl ist wirklich größer 
    # als 10, wird der nachfolgende Block als Code ausgeführt,
    print("Die Zahl ist größer als 10.")  # Wenn die Bedingung "zahl > 10" wahr ist, wird diese Zeile ausgeführt und der Text "Die Zahl ist größer als 10." ausgegeben.

else:                                       # Die else-Anweisung wird verwendet, um einen Block von Code auszuführen, wenn die Bedingung der if-Anweisung falsch (False) ist.
#                                             Ist die Zahl also 10 oder kleiner, wird dieser Code aktiviert.

    print("Die Zahl ist 10 oder kleiner.")  # Diese Zeile wird ausgeführt, wenn die Zahl 10 oder kleiner ist. Sie gibt den Text "Die Zahl ist 10 oder kleiner." aus.





## Aufgabe 2: Listen verstehen und mit Python erstellen 

# **Ziel:** Verstehen, wie Datenstrukturen wie Listen verwendet werden können.

# Dieses Programm arbeitet mit einer Liste und gibt die erste und die letzte Zahl aus dieser Liste aus.


zahlen = [1, 2, 3, 4, 5]                     # Als erstes wird eine Liste mit den Werten 1, 2, 3, 4, 5 erstellt und der Variablen zahlen zugewiesen. In Python sind Listen geordnete Sammlungen 
#                                               von Werten, die über Indexe zugänglich sind und in eckigen Klammern definiert werden. Die Indizierung beginnt bei Null, d.h. zahlen[0] gibt das 
#                                               erste Element der Liste zurück (hier 1).
print("Die erste Zahl ist:", zahlen[0])
print("Die letzte Zahl ist:", zahlen[-1])     # der Befel print gibt den Text zusammen mit dem Wert zahlen[-1] aus. Durch die negative 1 kann man in Python auf das letzte Element zugreifen. Mit
#                                               -2 auf das vorletzte, usw.

#- Schreibe die Arbeitsschritte auf.

#**Zusatzaufgabe:** Erstelle selbst eine Liste mit Wochentagen und schreibe die Arbeitsschritte auf.


## Aufgabe 3: Entscheidungslogik erweitern (25 Punkte)

# **Ziel:** Die Funktionsweise von mehreren Bedingungen in Python verstehen und in Arbeitsschritte übertragen.

# Code-Beispiel:


zahl = int(input("Gib eine Zahl ein: "))  # Als erstes fordere ich den Benutzer durch input() auf, eine Zahl einzugeben. Da input() die Eingabe immer als String zurückgibt, wandel ich die 
#                                           Eingabe durch int() in eine ganze Zahl um (Integer). Dies wird durch int(input()) erreicht. Das Ergebnis wird der Variablen zahl zugewiesen.
if zahl > 0:                              # if zahl > prüft, ob die Zahl größer ist als 0
    print("Die Zahl ist positiv.")        # Wenn die Bedingung wahr ist (d.h. die Zahl ist positiv), wird der Code innehalb des if-Blocks ausgeführt. In diesem Fall wird "Die Zahl ist positiv"
#                                           ausgegeben.
elif zahl < 0:                            # elif (kurz für"else if") wird verwendet, wenn die erste if-Bedingung falsch ist und eine alternative Bedingung überprüft werden soll.
#                                           zahl < 0 prüft, ob die Zahl kleiner ist als 0. 
    print("Die Zahl ist negativ.")        # Ist die Bedingung wahr, wird der Code innerhalb dieses Blocks ausgeführt und die Zahl ist negativ.
else:                                     # else wird verwendet, wenn keine der vorherigen Bedingungen (also if und elif) zutrifft.
    print("Die Zahl ist null.")           # Wenn die Zahl weder größer als 0 noch kleiner als 0 ist, muss sie gleich 0 sein. In diesem Fall wird der Code im else-Block ausgeführt und 
#                                           "Die Zahl ist null." ausgegeben.




## Aufgabe 4: Funktionen verstehen (20 Punkte)

# **Ziel:** Lernen, wie Funktionen in Python definiert werden und was in jedem Arbeitsschritt passiert.

# Code-Beispiel:


def ist_gerade(zahl):                       # Diese Funktion überprüft, ob eine Zahl gerade ist. def ist das Schlüsselwort in Python, um eine Funktion zu definieren. 
#                                             ist_gerade ist der Name der Funktion. Funktionen in Python werden benannt, um später im Code darauf zuzugreifen. Der Name "ist_gerade"
#                                             deutet darauf hin, dass die Funktion überprüft, ob eine Zahl gerade ist. (zahl) ist der Parameter der Funktion. Wenn du die Funktion aufrufst, 
#                                             kannst du eine Zahl an die Funktion übergeben, die dann in der Variable zahl gespeichert wird. Der Parameter zahl ist also der Eingabewert, 
#                                             der überprüft werden soll.
    if zahl % 2 == 0:
        return True
    else:
        return False

zahl = int(input("Gib eine Zahl ein: "))
if ist_gerade(zahl):
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")


# -Schreibe die Arbeitsschritte auf.



## Aufgabe 5: Benutzerinteraktion (10 Punkte)

# **Ziel:** Die Struktur eines Programms mit Benutzereingaben und Ausgaben analysieren.

# Code-Beispiel:


name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))
print(f"Hallo {name}, in 10 Jahren wirst du {alter + 10} Jahre alt sein!")


# - Schreibe die Arbeitsschritte auf.
