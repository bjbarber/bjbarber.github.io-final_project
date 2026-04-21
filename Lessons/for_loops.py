"""Loop practice"""

letters: list[str] = ["w", "x", "y", "z"]

idx: int = 0
while idx < len(letters):
    print(letters[idx])
    idx += 1

for elem in letters:
    print(elem)
    # creates variable called elem; elem will iterate over every element in the list
    # can name this variable whatever you want

pet_names: list[str] = ["Max", "Beasley"]


def celebrate(pet_names: list[str]) -> None:
    for elem in pet_names:
        print(f"Good boy, {elem} !")


# says good boy to every pet in the list

names: list[str] = ["Alyssa", "Izzi", "Benjamin"]

for index in range(0, len(names)):
    element: str = names[index]
    print(f"{index}: {element}")

# prints the element and the index.
# start at 0 so it can count to 3. If started at 1, it would count only twice.

def celebrate(pet_names: list[str]) -> None:
    for index in range(0, len(pet_names:))
        elem: str = names[index]
        print(f"Good boy, {elem} !")

# you can call the same function with dictionaries

def get_orders(orders: dict[str, int]) -> None:
    for key in orders:
        num_orders: int = orders[key]
        #gives us the number of flavors at the key.
        print(f"{key} has {num_orders}.")