"""Class Writing Practice."""


class GameCollection:

    inventory: list[str]
    wishlist: list[str]
    budget: float

    def __init__(self, curr_inventory: list[str], wish: list[str], start_budget: float):
        self.inventory = curr_inventory
        self.wishlist = wish
        self.budget = start_budget

    # __init__ initializes the attributes

    def purchase(self, name: str, cost: float):
        if cost < self.budget:
            self.budget -= cost
            self.inventory.append(name)
        for _ in self.wishlist:
            if name == self.wishlist[_]:
                self.wishlist.pop(_)
        else:
            print("Sorry! Not enough money!")

    def __add__(self, new_game: str) -> GameCollection:
        new_wishlist: list[str] = []
        for item in self.wishlist:
            new_wishlist.append(item)
        # copies a new list
        new_wishlist.append(new_game)
        # x = .append() will return none

        z = self.inventory
        y = self.budget
        return GameCollection(z, new_wishlist, y)


my_games: GameCollection = GameCollection(
    curr_inventory=["Sims"], wish=["Witcher"], start_budget=50.75
)

my_games.purchase("Stardew", 40.25)
my_games.purchase("Witcher", 60.00)
