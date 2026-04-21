"""Programming a cozy tea a party; plug in guests figure out logistics"""

_author_: str = "730640030"


def main_planner(guests: int) -> None:
    """Entrypoint of program"""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


"""It took me awhile to figure out printing the cost function, but I realized the tea_bags(guests and treats(guests) really just give us integers to plug in"""


def tea_bags(people: int) -> int:
    """tells us how many teabags we need based on # of people"""
    return 2 * people


"""At first I thought I needed to print this so I actually wrote the code to print it with my own prompt, I realized that did not make sense with the next two steps and deleted it"""


def treats(people: int) -> int:
    """how many treats we need based on # of people"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """computes cost of tea bags and treats combined"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))

"""This is what allows us to run the program and prompt the user to input the number of guests"""
