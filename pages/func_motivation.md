## Looking _within_ data

<div class="flex justify-center gap-10">
<div>

````md magic-move
```py {all|1-5,12-16|2-4,13-15|4,15}
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
````

</div>
<v-click>
<div>
More possible factorization!
</div>
</v-click>
</div>
