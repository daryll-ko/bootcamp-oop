from Animal_poly import Animal

animal = Animal("Wilson", "walrus")
animal2 = Animal("Kevin", "kangaroo")

animals = animal + animal2

for animal in animals:
    print(animal.greeting())
