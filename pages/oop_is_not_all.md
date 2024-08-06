## OOP is not all

<div class="grid grid-cols-3 gap-10">

<v-clicks>

<div class="flex flex-col items-center justify-center">

```py
def maximum(l: list[int]) -> int:
	assert len(l) > 0
	result = l[0]
	for x in l:
		if x > result:
			result = x
	return result
```

```hs
maximum :: [Int] -> Int
maximum [] = error "empty list has no maximum"
maximum [x] = x
maximum (x:xs)
	| x > maxTail = x
	| otherwise = maxTail
	where maxTail = maximum xs
```

<p class="text-center py-0">

**Functional programming**

(Almost) everything is pure!

</p>
</div>

<div class="flex flex-col items-center justify-center">

```py
not_final(success).
not_fatal(failure).

courage_to_continue_counts() :-
	not_final(success),
	not_fatal(failure).

courage_to_countinue_counts()?
```

<p class="text-center py-0">

**Logic programming**

Make your own rules!

</p>
</div>

<div>

```asm
recurse:
	move	$a0, $s4
	move	$a1, $t8
	jal	set_positions

	or	$s6, $s6, $t1

	move	$a0, $s4
	move	$a1, $s5
	move	$a2, $s6
	move	$a3, $s7
	jal	backtrack
	or	$s1, $s1, $v0
	bgt	$s1, $0, finish

	...
```

<p class="text-center py-0">

**_sigh_**

Good luck in CS 21...

</p>

</div>

</v-clicks>

</div>
