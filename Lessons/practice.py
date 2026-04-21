 def count(x: str) -> str:
        """Practice conditionals."""
        y: int = len(x)
        if y % 4 == 1:
            y = y * 2
        y = y - 6
        print(y)
        return(x[y])
        print(x[y])

    count(x="Hello")
