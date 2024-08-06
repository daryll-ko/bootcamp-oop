## Inheritance

<v-click>

**Specifying** classes

</v-click>

<div class="mx-auto w-fit">
<v-click>

````md magic-move
```py
from dataclasses import dataclass

@dataclass
class Animal:
	name: str
	kind: str

	def greeting(self) -> str:
		return f"Hey, {self.name} the {self.kind}!"
```

```py
from dataclasses import dataclass

@dataclass
class Animal:
	name: str
	kind: str

	def greeting(self) -> str:
		return f"Hey, {self.name} the {self.kind}!"

@dataclass
class Mammal:
	name: str
	kind: str
	habitat: str

	def greeting(self) -> str:
		return f"Hey, {self.name} the {self.kind}!"

	def special_greeting(self) -> str:
		return f"Good day, {self.name} the {self.kind}!"
```

```py {all|12|all}
from dataclasses import dataclass

@dataclass
class Animal:
	name: str
	kind: str

	def greeting(self) -> str:
		return f"Hey, {self.name} the {self.kind}!"

@dataclass
class Mammal(Animal):
	habitat: str

	def special_greeting(self) -> str:
		return f"Good day, {self.name} the {self.kind} of {self.habitat}!"
```
````

</v-click>
</div>

<v-click>

All mammals are animals, but not all animals are mammals.

</v-click>
