# Definiere eine Funktion namens "square", die eine Zahl annimmt und hoch zwei zurückgibt.
# Funktionsdefinition:

def square_root(zahl):
    return pow(zahl, 0.5)

# Funktion ohne Argumente:
def square_root_no_argument():
    zahl = user_input
    return pow(zahl, 0.5)

# Funktion mit zwei Argumenten:

def add(zahl1,zahl2):
    return zahl1 + zahl2



# Funktionsaufruf 
user_input = float(input("Gib mir eine Zahl: "))
result = square_root(user_input)

print(result)
print(square_root_no_argument)

# Wir schreiben eine Funktion, die den user nach dem Alter fragt und dieses auf der Konsole ausgibt.

def altersabfrage():
    age_string = input("Wie alt bist du: ")
    age = int(age_string)
    print(f"Du bist also {age} Jahre alt.")

altersabfrage()

# Schreibe eine Funktion, die den Benutzer nach seinem Namen fragt und diesen auf der Konsole ausgibt.

def namensabfrage():
    name = input("Gib deinen Namen an: ")
    print(f"Du bist also {name} ")

namensabfrage()

# Schreibe eine Funktion, die den Benutzer nach seinem Namen fragt und mit return zurückgibt.

def namensabfrage2():
    name = input("Gib deinen Namen an: ")
    return (f"Du bist also {name}.")

print(namensabfrage())
print(namensabfrage2())