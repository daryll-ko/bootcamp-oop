from Zoo import Animal, Zoo
from Mammal import Mammal

animal = Animal("Wilson", "walrus")

zoo = Zoo("DCS Zoo", [])
zoo.add_animal(animal)

# print(zoo)

animal2 = Mammal("Kevin", "kangaroo", "DCS")
zoo.add_animal(animal2)

print(zoo)

print(animal2.special_greeting())
