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
class Mammal(Animal):
    habitat: str

    def special_greeting(self) -> str:
        return f"Good day, {self.name} the {self.kind} of {self.habitat}!"
