## Encapsulation

What we've been doing so far!

<div class="mx-auto w-fit">

````md magic-move
```py
name = "Wilson"
kind = "walrus"
greeting = "Hey, Wilson the walrus!"

print(name)
print(kind)
print(greeting)
```

```py
animal = {
	"name": "Wilson",
	"kind": "walrus",
	"greeting": "Hey, Wilson the walrus!",
}

print(animal["name"])
print(animal["kind"])
print(animal["greeting"])
```

```py
def greeting(name: str, kind: str) -> str:
	return f"Hey, {name} the {kind}!"

animal = {
	"name": "Wilson",
	"kind": "walrus",
	"greeting": greeting("Wilson", "walrus"),
}

print(animal["name"])
print(animal["kind"])
print(animal["greeting"])
```

```py {all|5-6,8}
from dataclasses import dataclass

@dataclass
class Animal:
	name: str
	kind: str

	def greeting(self) -> str:
		return f"Hey, {self.name} the {self.kind}!"

animal = Animal("Wilson", "walrus")

print(animal.name)
print(animal.kind)
print(animal.greeting())
```
````

</div>

<v-click>

**Encapsulating** or **grouping** relevant data and functions together

</v-click>
