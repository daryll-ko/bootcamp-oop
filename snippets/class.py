from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    kind: str

    def greeting(self) -> str:
        return f"Hey, {self.name} the {self.kind}!"


animal = Animal("Perry", "platypus")

print(animal.name)
print(animal.kind)
print(animal.greeting())
print()

animal2 = Animal("Wilson", "walrus")

print(animal2.name)
print(animal2.kind)
print(animal2.greeting())
