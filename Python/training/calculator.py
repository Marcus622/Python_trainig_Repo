# Aufgabe 3: Taschenrechner 

# Als erstes vier Funktionen: add(x,y), subtract(x,y), mult(x,y) und div(x,y)
    
    
# Addition
def add(x, y):
    return x + y

# Subtraktion
def subtract(x, y):
    return x - y

# Multiplikation
def mult(x, y):
    return x * y

# Division
def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Fehler: Division durch Null ist nicht erlaubt."

# Beispielaufrufe:
x = 10
y = 5

print(f"{x} + {y} = {add(x, y)}")
print(f"{x} - {y} = {subtract(x, y)}")
print(f"{x} * {y} = {mult(x, y)}")
print(f"{x} / {y} = {div(x, y)}")


# Rechenfunktionen
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Fehler: Division durch Null ist nicht erlaubt."

# Calculator Funktion
def calculator():
    # Benutzer fragt nach der gewünschten Operation
    operation = input("Welche Operation möchtest du durchführen? (addieren, subtrahieren, multiplizieren, dividieren): ").lower()
    
    # Benutzer nach den zwei Zahlen fragen
    x = float(input("Gib die erste Zahl ein: "))
    y = float(input("Gib die zweite Zahl ein: "))
    
    # Die entsprechende Funktion je nach Operation aufrufen und das Ergebnis ausgeben
    if operation == "+":
        result = add(x, y)
        print(f"Das Ergebnis von {x} + {y} ist {result}.")
    elif operation == "-":
        result = subtract(x, y)
        print(f"Das Ergebnis von {x} - {y} ist {result}.")
    elif operation == "*":
        result = mult(x, y)
        print(f"Das Ergebnis von {x} * {y} ist {result}.")
    elif operation == "/":
        result = div(x, y)
        print(f"Das Ergebnis von {x} / {y} ist {result}.")
    else:
        print("Ungültige Operation. Bitte wähle eine der folgenden: addieren, subtrahieren, multiplizieren, dividieren.")

# Calculator aufrufen
calculator()
