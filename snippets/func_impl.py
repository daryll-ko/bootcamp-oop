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
