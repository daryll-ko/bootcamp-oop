## Using functions

<div class="flex justify-center gap-10">
<div>

````md magic-move
```py {all|4,15}
animal = {
	"name": "Perry",
	"kind": "platypus",
	"greeting": "Hey, Perry the platypus!",
}

print(animal["name"])
print(animal["kind"])
print(animal["greeting"])
print()

animal2 = {
	"name": "Wilson",
	"kind": "walrus",
	"greeting": "Hey, Wilson the walrus!",
}

print(animal2["name"])
print(animal2["kind"])
print(animal2["greeting"])
```

```py {1-2|1-2,7,18}
def greeting(name: str, kind: str) -> str:
	return f"Hey, {name} the {kind}!"

animal = {
	"name": "Perry",
	"kind": "platypus",
	"greeting": "Hey, Perry the platypus!",
}

print(animal["name"])
print(animal["kind"])
print(animal["greeting"])
print()

animal2 = {
	"name": "Wilson",
	"kind": "walrus",
	"greeting": "Hey, Wilson the walrus!",
}

print(animal2["name"])
print(animal2["kind"])
print(animal2["greeting"])
```

```py {1-2,7,18}
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
````

</div>
<v-click>
<div class="flex flex-col justify-center">

Almost there!

</div>
</v-click>
</div>
