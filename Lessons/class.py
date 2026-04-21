"""For practice writing classes"""

# prompt is on class writing slide of CL15

class ShoppingGuide:

    groceries: list[str]
    budget: float
    store: str

    def __init__(self, groceries: list[str], budget: float, store: str)
        self.groceries = groceries
        self.budget = budget
        self.store = store
        # you don't have to name parameters the same as attributes, as long as they're equal.
        # I wonder whether self is attached to the parameter or the attribute... ???
    def __str__(self) -> str:
        info: str = f"Go to {self.store} and buy {self.groceries} with {self.budget}"

    def __add_(self, more_money: float) -> ShoppingGuide:
        other_guide: ShoppingGuide = ShoppingGuide(self.groceries, self.budget + more_money, self.store)
        return other_guide

my_plan: ShoppingGuide = ShoppingGuide(["apples", "kiwi"], 5.55, "food lion")
AJs_plan: ShoppingGuide = my_plan + 2.12
print(AJs_plan)