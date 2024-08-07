from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    kind: str

    def greeting(self) -> str:
        return f"Hey, {self.name} the {self.kind}!"

    def __add__(self, other: Animal) -> list[Animal]:
        return [self, other]
