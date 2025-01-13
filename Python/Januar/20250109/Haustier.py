# Klassendefinition

class Pet:
    def __init__(self, name, species, age, favourite_food):
        self.name = name
        self.species = species
        self.age = age
        self.favourite_food = favourite_food
        self.energy_level = 100


    def get_description(self):
        description = f"Unser Vieh heisst {self.name}, ist ein {self.species} und {self.age} Jahre alt."
        return description
        

    def play(self, duration):
        energy_lost = duration * 5
        if self.energy_level < energy_lost:
            print("Das Vieh ist zu müde um so lange zu spielen.")

        if self.energy_level >= energy_lost:
            self.energy_level = self.energy_level - energy_lost
            print("Das Energielevel liegt bei: ",self.energy_level)

            return





pet_object1 = Pet("Waldi", "Hund", 5, "Futter")
pet_object2 = Pet("wolfi", "Vogel", 7 ,"Mais")

pet_object1.play(5)

# print(pet_object1.get_description())
# print(pet_object2.get_description())