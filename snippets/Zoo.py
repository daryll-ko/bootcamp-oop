from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    kind: str

    def greeting(self) -> str:
        return f"Hey, {self.name} the {self.kind}!"

    def wrap(self) -> str:
        length = 30
        pad = (length - 2) - (len(self.name) + len(self.kind) + 5)
        return f"""
{'-'*length}
|{' '*(pad//2)}{self.name} the {self.kind}{' '*((pad+1)//2)}|
{'-'*length}"""


@dataclass
class Zoo:
    name: str
    animals: list[Animal]

    def __repr__(self) -> str:
        return f"""\
  ____         
 |_  /___  ___ 
  / // _ \\/ _ \\
 /___\\___/\\___/

{'\n'.join([*map(lambda animal: animal.wrap(), self.animals)])}"""

    def add_animal(self, animal: Animal) -> None:
        self.animals.append(animal)

    def reverse(self) -> None:
        self.animals.reverse()


animal = Animal("Wilson", "walrus")

zoo = Zoo("DCS Zoo", [])
zoo.add_animal(animal)

print(zoo)

animal2 = Animal("Kevin", "kangaroo")
zoo.add_animal(animal2)
