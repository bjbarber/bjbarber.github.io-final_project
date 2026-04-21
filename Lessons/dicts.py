"""For practicing dictionary use"""

# dictionaries are lists which match a key to a value, as opposed to matching an index to a value in a list.

# constructing an empty dict: name: dict[<key type>, <value type>]
name: dict[str, float] = dict()  # or {}

# constructing a populated dict:
temps: dict[str, float] = {"Florida": 72.5, "Raleigh": 56.0}

# adding elements: <dict name>[<key] = <value>
temps["DC"] = 52.1

# removing elements
temps.pop("Florida")

# access a value:
temps["DC"]

# modify a value (valyes can be duplcates)
temps["DC"] = 53.1 """new value"""

# check if key in dictionary; will evaluate to a boolean
"DC" in temps