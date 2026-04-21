"""Quiz 3 Review"""


# Short Answer 5
class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def flip(self) -> None:
        temp: float = self.x
        self.x = self.y
        self.y = temp

    def shift_y(self, dy: float) -> None:
        self.y += dy

    def diff(self) -> float:
        return self.x - self.y


# 5.1

my_point: Point = Point(3.7, 2.3)

# 5.2

my_point.x = 2.0

# 5.3

my_point.shift_y(1.0)

# 5.4

x: float = my_point.diff()

# Function + Method-Writing with Instances of a Class

# 1


class Course:
    """Models the idea of a UNC course."""

    name: str
    level: int
    prerequisites: list[str]

    # 2

    def is_valid_course(self, course: str) -> bool:
        if self.level >= 400 and course in self.prerequisites:
            return True
        else:
            return False

    # don't forget to include self as a parameter.


def find_courses(courses: list[Course], prerequisite: str) -> list[str]:
    found_courses: list[str] = []

    for x in courses:
        if prerequisite in x.prerequisites and x.level >= 400:
            found_courses.append(x.name)

    return found_courses

    # x.prerequisites refers to the course at x index in the list. Same with x.name


# Class-writing


class Car:
    """Represents a basic model of a car."""

    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(self, make: str, model: str, year: int, color: str, mileage: float):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def update(self, miles: float) -> None:
        self.mileage += miles
        # you need to add the parameter name, not the type! (Day 1 stuff)
        # evaluate to none, for good practice.

    def display_info(self) -> None:
        """Prints attributes."""
        print(self.make)
        print(self.model)
        print(self.year)
        print(self.color)
        print(self.mileage)


def calculate_depreciation(obj: Car, depreciation_rate: float) -> float:
    return obj.mileage * depreciation_rate
    # Classes are types, so obj: Car means Car is the type! This is correct.


# Class Writing + Magic Methods


class HotCocoa:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(
        self, has_whip: bool, flavor: str, marshmallow_count: int, sweetness: int
    ):
        self.has_whip = has_whip
        self.flavor = flavor
        self.marshmallow_count = marshmallow_count
        self.sweetness = sweetness

    def mallow_adder(self, mallows: int) -> None:
        self.marshmallow_count += mallows
        self.sweetness += 2 * mallows

        # don't forget self as a parameter.

    def __str__(self) -> str:
        if self.has_whip == True:
            return f"A {self.flavor} cocoa with whip, {self.marshmallow_count} marshmallows, and level {self.sweetness} sweetness."
        else:
            return f"A {self.flavor} cocoa without whip, {self.marshmallow_count} marshmallows, and level {self.sweetness} sweetness."


def order_cost(order: list[HotCocoa]) -> float:
    with_whip: int = 0
    without_whip: int = 0

    for _ in order:
        if order.has_whip == True:
            with_whip += 1
        else:
            without_whip += 1

    return with_whip * 2.50 + without_whip * 2.00

    # you can also adjust the cost and not use the variables with/w/o whip.


# Instantiation Practice with HotCocao

my_order: HotCocoa = HotCocoa(
    has_whip=False, flavor="vanilla", marshmallow_count=5, sweetness=2
)

my_order.has_whip = True
# Booleans must have first letter capitalized (T/F)

my_order.mallow_adder(2)

viktoryas_order: HotCocoa = HotCocoa(
    has_whip=True, flavor="peppermint", marshmallow_count=10, sweetness=2
)

orders: list[HotCocoa] = list[my_order, viktoryas_order]
order_cost(orders)

print(my_order)
# prints out the details of the order, because of the __str__ magic method.

# Timespent


class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minutes: int):
        self.name = name
        self.purpose = purpose
        self.minutes = minutes
        # stay consistent with types

    def add_time(self, added_minutes: int) -> None:
        self.minutes += added_minutes
        # don't forget to include self!

    def __add__(self, added_minutes: int) -> TimeSpent:
        new_minutes = self.minutes + added_minutes

        return TimeSpent(self.name, self.purpose, new_minutes)
        # check this one.

    def reset(self) -> str:
        old_minutes = self.minutes
        self.minutes = 0
        return old_minutes
        # check this one too.

    def __str__(self) -> str:
        return f"{self.name} has spend {self.minutes} on {self.purpose}."
        # return the string, don't print it. Print() automaticaly calls __str__.


def most_by_purpose(collect: list[TimeSpent], purpose: str) -> str:
    most_time: TimeSpent = collect[0]
    # | None = None because thats what the object equals, not [].
    # it means the variable can be a timespent or none.

    for x in collect:
        if x.purpose == purpose:
            if (
                x.minutes > most_time.minutes and most_time.purpose == purpose
            ):  # not correct
                most_time = x  # x is an object in the list.
            else:
                most_time = x

    return most_time.name

    # better off just having two variables for time and name.


# Code Writing

class Node:

# 1
def recursive_range(start: int, end: int) -> Node | None:
    if start == end:
        return None
        # base case where we don't include the end number.
    elif start < end:
        return Node(start, recursive_range(start + 1, end))
    else:
        return Node(start, recursive_range(start - 1, end))
    
# 2

def append(self, new_val: int) -> None:
    if self.next is None:
        self.next = Node(new_val, None) # last node object has None, soo this makes final Node.
    else:
        self.next.append(new_val) # adds new_val to the next object in linked list.

    # recursive methods needs a recursive case and a base case.
