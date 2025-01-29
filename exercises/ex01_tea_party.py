"""Plan a cozy tea party!"""

__author__: str = "730824693"


def main_planner(guests: int) -> None:
    """Bring all the functions together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost: "
        + "$"
        + str(
            cost(
                tea_count=(tea_bags(people=guests)), treat_count=(treats(people=guests))
            )
        )
    )


def tea_bags(people: int) -> int:
    """Number of tea bags based on number of guests."""
    return people * 2


def treats(people: int) -> int:
    """Number of treats based on number of teas."""
    return int(tea_bags(people) * 1.5)
    tea_bags(people=1)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea bags and treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
