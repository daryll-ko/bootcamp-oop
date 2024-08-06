## Classes

<div class="w-fit mx-auto">

````md magic-move
```py
def greeting(name: str, kind: str) -> str:
	return f"Hey, {name} the {kind}!"

animal = {
	"name": "Perry",
	"kind": "platypus",
	"greeting": greeting("Perry", "platypus"),
}

print(animal["name"])
print(animal["kind"])
print(animal["greeting"])
print()

animal2 = {
	"name": "Wilson",
	"kind": "walrus",
	"greeting": greeting("Wilson", "walrus"),
}

print(animal2["name"])
print(animal2["kind"])
print(animal2["greeting"])
```

```py {all|-6|1,3,11,13-14|4,11|5-6|all}
from dataclasses import dataclass

@dataclass
class Animal:
	name: str
	kind: str

def greeting(name: str, kind: str) -> str:
	return f"Hey, {name} the {kind}!"

animal = Animal("Perry", "platypus")

print(animal.name)
print(animal.kind)
print(greeting(animal.name, animal.kind))
print()

animal2 = {
	"name": "Wilson",
	"kind": "walrus",
	"greeting": greeting("Wilson", "walrus"),
}

print(animal2["name"])
print(animal2["kind"])
print(animal2["greeting"])
```

```py
from dataclasses import dataclass

@dataclass
class Animal:
	name: str
	kind: str

def greeting(name: str, kind: str) -> str:
	return f"Hey, {name} the {kind}!"

animal = Animal("Perry", "platypus")

print(animal.name)
print(animal.kind)
print(greeting(animal.name, animal.kind))
print()

animal2 = Animal("Wilson", "walrus")

print(animal2.name)
print(animal2.kind)
print(greeting(animal2.name, animal2.kind))
```

```py {all|8-9,15,22}
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
```
````

</div>
