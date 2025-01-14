from random import randint
zahl = randint(1, 100)

print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")

while True:
    versuch = int(input("Rate meine Zahl: "))

    if versuch == zahl:
        print("Super, du hast die Zahl erraten.")
        break

    elif versuch < zahl:
        print("Die Zahl ist zu klein.")

    else:
        print("Die Zahl ist zu groß.")