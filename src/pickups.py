
import random
class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

fruits = {"apple", "strawberry", "cherry", "watermelon"}
veggies_meat = ["carrot", "radish", "cucumber", "meatball"]

all_items = list(fruits) + veggies_meat
pickups = [Item(name, value=20 if name in fruits else 10) for name in all_items]

# Random frukt
fruit_items = [item for item in pickups if item.name in fruits]
picked = random.choice(pickups)
revealed = []


def reveal_picked(grid):
    global picked

    candidates = []
    for y in range(grid.height):
        for x in range(grid.width):
            cell = grid.get(x, y)
            if isinstance(cell, Item):
                candidates.append(cell)

    candidates = [item for item in candidates if item not in revealed]

    if candidates:
        picked = random.choice(candidates)
        picked.symbol = "?"
        revealed.append(picked)

    elif revealed:
        revealed.clear()
        reveal_picked(grid)

    else:
        picked = None

def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = random.randint(1, grid.width - 2)
            y = random.randint(1, grid.height - 2)
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

