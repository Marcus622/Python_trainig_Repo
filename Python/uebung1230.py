# a = 5
# b = 15
# c = 17

# print(a < b or b > c) or not (c != b and b < a) 
# print(a > b or a <= b)
# print(a != b and a > b)
# print(not(a == b))

# km_meilen = 0.621371
# km = float(input("Gib die Km ein, die du umrechnen möchtest: "))
# meilen = km_meilen * km
# print(f"{km} Km sind {meilen} Meilen.")





# In diesem Programm soll der Nutzer ein Datum eingeben und es soll wiedergegeben werden, ob an diesem Tag Unterricht
# oder frei ist.
# Als erstes formuliere ich die Eingabeaufforderung



import datetime     # Diese Zeile importiert die datetime-Bibliothek um mit Datums-und Zeitinformationen zu arbeiten.
                    # Sie ermöglicht es, das aktuelle Datum abzurufen, Zeiträume zu erfassen u.v.m.

date = datetime.datetime.now    # gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.
print(date)                     # gibt das aktuelle Datum und die Uhrzeit auf der Konsole aus.


date_today = input("Gib das gewünschte Datum im Format jjjj. mm. tt ein: ") # Hier wird der Benutzer aufgefordert, das 
# Datum einzugeben, welches er überprüfen möchte. Diese Eingabe wird als string in der Variable date_today gespeichert.

# jetzt muss ich die freien Tage definieren, die nach der Eingabe des Datums verglichen werden.

WinterHolidaysStart24 = "2024.12.23"
WinterHolidaysEnd24 = "2025.01.02"
EasterHolidaysStart25 = "2025.04.17"
EasterHolidaysEnd25 = "2025.04.22"
SummerHolidaysStart25 = "2025.08.08"
SummerHolidaysEnd25 = "2025.08.20"
WinterHolidaysStart25 = "2025.12.23"
WinterHolidaysEnd25 = "2026.02.01"
first_may = "2025.05.01"
christi_verpissimus = "2025.05.29"
pfimo = "2025.06.09"
day_of_dawn = "2025.10.03"
martin_luther_day = "2025.10.31"


