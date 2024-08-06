## Abstraction

<v-click>

Using **black boxes** or **oracles**

</v-click>

<div class="flex justify-center items-center gap-10">
<v-clicks>
<div>

```py
animal = Animal("Wilson", "walrus")

zoo = Zoo("DCS Zoo", [])
zoo.add_animal(animal)

print(zoo)
```

</div>
<div>

```
  ____
 |_  /___  ___
  / // _ \/ _ \
 /___\___/\___/


------------------------------
|     Wilson the walrus      |
------------------------------
```

</div>
</v-clicks>
</div>

<v-click>

**Abstracting** implementation details away from users

</v-click>
