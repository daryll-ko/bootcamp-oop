## Basic idea

<div class="flex justify-center gap-10">
<div>

```py {all|1-3|5-7|all}
name = "Perry"
kind = "platypus"
greeting = "Hey, Perry the platypus!"

print(name)
print(kind)
print(greeting)
```

</div>

<div>
<v-click>
<div>
Output:

```
Perry
platypus
Perry the platypus
```

</div>
</v-click>

<v-click>
What if we want another animal?
</v-click>
</div>
</div>

---

## Two animals

<div class="flex justify-center gap-10">
<div>

````md magic-move
```py
name = "Perry"
kind = "platypus"
greeting = "Hey, Perry the platypus!"

print(name)
print(kind)
print(greeting)
```

```py {all|1-7|10-16|all}
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

Can we get `Perry` back?

</v-click>
</div>

</div>

---

## Two animals, but _persistent_

<div class="flex justify-center gap-10">
<div>

````md magic-move
```py
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

```py
name = "Perry"
kind = "platypus"
greeting = "Hey, Perry the platypus!"

print(name)
print(kind)
print(greeting)
print()

name2 = "Wilson"
kind2 = "walrus"
greeting2 = "Hey, Wilson the walrus!"

print(name2)
print(kind2)
print(greeting2)
```

```py
name = "Perry"
kind = "platypus"
greeting = "Hey, Perry the platypus!"

print(name)
print(kind)
print(greeting)
print()

name2 = "Wilson"
kind2 = "walrus"
greeting2 = "Hey, Wilson the walrus!"

print(name2)
print(kind2)
print(greeting2)
print()

print(name)
print(kind)
print(greeting)
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

Perry
platypus
Hey, Perry the Platypus!
```

</div>
</v-click>

</div>
</div>
