"""Review for Quiz 2"""

# Dictionaries and For loops
# 1
stats: list[int] = [7, 8, 9]
index: int = 0
total: int = 100
while index < len(stats):
    total -= stats[index]
    index += 1
# 1.1
for x in stats:
    total -= x
# 1.2
for x in range(0, 3):
    total -= stats[x]

# 2
classes: set[str] = {"110", "210", "311"}
classes.remove("210")
classes.add("445")


# 5
my_dict: dict[int, str] = {}

# 5.1
my_dict["8"] = "eight"
my_dict["0"] = "zero"
my_dict["3"] = "three"
my_dict["-1"] = "negative 1"

# 5.2
my_dict.pop("3")

# 5.3
cat: str = my_dict["0"]


# 5.4
def key_num() -> None:
    print(len(my_dict))


# 5.5
def value_num() -> None:
    print(len(my_dict))


# 5.6
my_dict["8"] = "zero"


# 5.7
name["returned_amount"] = sum_dict_keys(my_dict)

result_dict = {"returned_amount": sum_dict_keys(my_dict)}

# 8
my_dictionary: dict[str, float] = {}

# 9
msg: dict[str, int] = {"Hello": 1, "Yall": 2}

msg["yall"]

# 10
msg["yall"] += 3

# 11
ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}

ids.pop(100)

# 12
len(ids)

# 13
inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}

inventory["markers"] = 15

# 14
prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}

prices["milk"] = 2.50

# 15
scores: dict[str, int] = dict()

for key in scores:
    print(key)

# 16
fruit_count: dict[str, int] = {}

for key in fruit_count:
    print(f"{key}: {fruit_count[key]}")

# Unit Tests

# 4
"""Use case for function"""


def test_fill_list_length() -> None:
    assert len(fill_list[4, 19]) == 18


def test_fill_list_contains() -> None:
    for idx in fill_list[4, 19]:
        assert fill_list[4] == 4


"""Edge case for function"""

"""--------------------------------------------------------------------------------------------"""
# Function Writing Practice


# Lists
def odd_and_even(a: list[int]) -> list[int]:
    odd_even: list[int] = []
    index: int = 0
    while index < len(a):
        if index % 2 == 0 and a(index) % 2 == 1:
            odd_even.append(a[index])
        index += 1
    return odd_even
