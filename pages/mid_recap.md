## So far, we have:

<div class="flex justify-center gap-10">
<div>
<v-clicks>

- raw variables and duplication
- factorizing what we duplicate
- dictionaries
- functions
- classes

</v-clicks>
</div>

<div>
<v-click>

```py
from dataclasses import dataclass

@dataclass
class Animal:
	name: str
	kind: str

	def greeting(self) -> str:
		return f"Hey, {self.name} the {self.kind}!"
```

</v-click>
</div>
</div>

<div class="mx-auto w-fit flex flex-col justify-center">
<v-click>
<p>

We used `class` to **group data and functions** together!

</p>
</v-click>

<v-click>
<p>

We have **objects**, and we **interact** with these objects.

</p>
</v-click>
</div>
