# Schreibe und erkläre eine Funktion celsius_to_fahrenheit(c) sowie fahrenheit_to_celsius(f)
#  die  die Temperatur in die jeweils andere einheit umrechnet.

def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) +32
    return fahrenheit

celsius_temp = 15
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)

print(f"{celsius_temp} Grad Celsius entsprechen {fahrenheit_temp} Grad Fahrenheit.")

def fahrenheit_to_celsius(f):
    celsius = (f-32) *5/9
    return celsius

fahrenheit_temp = 77
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)

print(f"{fahrenheit_temp} Grad Fahrenheit entsprechen {celsius_temp} Grad Celsius.")
