## Functions

<div class="flex justify-center gap-10">

<div class="flex flex-col items-center">

```py
def f(x: int) -> int:
	return x + 1
```

$f(x) = x+1$

</div>

<div class="flex flex-col items-center">

```py
def g(x: int, y: int) -> int:
	return x + y
```

$g(x, y) = x+y$

</div>

<div class="flex flex-col items-center">

```py
def greet(name: str) -> str:
	return f"Hi, {name}!"
```

<p>Not always math!</p>

</div>

</div>

<v-click>
<div>

Functions map **inputs** to **outputs**.

</div>
</v-click>

<v-click>
<div>

Ideally:

</div>
</v-click>

<div class="flex justify-center gap-10">
<div>

<v-click>

- Your functions have **types**

</v-click>

<v-click>

````md magic-move
```py
def bad(x):
	return x
```

```py
def good(x: int) -> int:
	return x
```
````

</v-click>

</div>
<div>

<v-click>

- Your functions are **pure**

</v-click>

<v-click>

````md magic-move
```py
def bad(x: int) -> int:
	print("hello world")
	return x
```

```py
def good(x: int) -> int:
	return x
```
````

</v-click>
</div>

<div>

<v-click>

- Your functions do **one** thing

</v-click>

<v-click>

````md magic-move
```py
def bad(x: int) -> tuple[int, int, int]:
	return x, x+1, 2*x
```

```py
def good(x: int) -> int:
	return x

def add_one(x: int) -> int:
	return x+1

def double(x: int) -> int:
	return 2*x
```
````

</v-click>

</div>
</div>
