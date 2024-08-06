## Dictionaries

<div class="flex justify-center gap-10">
<div>

````md magic-move
```py{all|1-8}
name = "Perry"
kind = "platypus"
greeting = "Hey, Perry the platypus!"

print(name)
print(kind)
print(greeting)
print()

name = "Wilson"
kind = "walrus"
greeting = "Hey, Wilson the walrus!"

print(name)
print(kind)
print(greeting)
```

```py{1-10|12-}
animal = {
	"name": "Perry",
	"kind": "platypus",
	"greeting": "Hey, Perry the platypus!",
}

print(animal["name"])
print(animal["kind"])
print(animal["greeting"])
print()

name = "Wilson"
kind = "walrus"
greeting = "Hey, Wilson the walrus!"

print(name)
print(kind)
print(greeting)
```

```py{12-|all}
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

<div>
<v-click>
<div>
<p>Output:</p>

```
Perry
platypus
Hey, Perry the Platypus!

Wilson
walrus
Hey, Wilson the Walrus!
```

</div>
</v-click>

<v-click>
<p>
"Factorizing" code
</p>
</v-click>

<v-switch>

<template #1>

<div class="flex flex-col items-center">

$ax + bx + cx$

`animal = { name2 kind2 greeting2 }`

</div>

</template>
<template #2>

<div class="flex flex-col items-center">

$(a + b + c)x$

`animal2 = { name kind greeting }`

</div>

</template>
</v-switch>

</div>
</div>
