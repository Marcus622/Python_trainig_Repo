# Erstelle eine Klasse, die ein Haustier beschreibt. 

class Animal:
    def __init__(self, name, species, age, favourite_food):
        
        self.name = name
        self.species = species
        self.age = age
        self.favourite_food = favourite_food
        self.energy_level = 100

# Beschreibung des Tieres.

    def get_description(self):
        return f" {self.name} is a {self.species} and {self.age} years old."
    
    def play_duration(self, duration):
        energy_lost = 5 * duration # Energieverlust 5 je  Minute.
        if self.energy_level < energy_lost:
            print(f"Achtung,{self.name} darf nicht zuviel Energie verbrauchen.")
        
        else:
            self.energy_level -= energy_lost
            print(f"{self.name} hat {duration} Minuten gespielt und hat jetzt noch einen Energielevel von {self.energy_level}.")


    def feed(self, food):
        if food == self.favourite_food:
            self.energy_level += 30
            print(f"{self.name} liebt {self.favourite_food} und hat jetzt ein Energielevel von {self.energy_level}.")

        else:
            self.energy_level += 10
            print(f"{self.name} hat {food} gegessen und jetzt einen E-Level von {self.energy_level}.")

        self.energy_level = min(self.energy_level, 100)
        
        if self.energy_level >= 80:
            print("Du darst keine Katze mehr verfüttern.")


pet1 = Animal(f"Brutus", "dog", 8, "Katzen")
pet2 = Animal(f"Joe", "monkey", 20, "bananas")
print(pet1.get_description())
pet1.play_duration(5)
pet1.feed("Katzen")
# print(f"Eine Katze später liegt sein Level bei {pet1.energy_level}.")
# pet1.feed("Katzen")

