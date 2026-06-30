
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
total_items_spawned = len(pickups)


def spawn_new_item(grid):
    """Skapar ett nytt slumpat item och placerar det på en ledig ruta på kartan."""
    global picked, total_items_spawned

    name = random.choice(all_items)
    value = 20 if name in fruits else 10
    new_item = Item(name, value=value)

    while True:
        x = random.randint(1, grid.width - 2)
        y = random.randint(1, grid.height - 2)
        if grid.is_empty(x, y):
            grid.set(x, y, new_item)
            break

    picked = new_item
    total_items_spawned += 1
    return new_item

def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = random.randint(1, grid.width - 2)
            y = random.randint(1, grid.height - 2)
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

