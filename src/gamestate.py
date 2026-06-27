from src import pickups
from src.grid import Grid
from src.player import Player

class GameState:

    def __init__(self):
        self.score = 0
        self.inventory = []

        # Bygg griden och väggarna innan spelaren placeras
        self.g = Grid()
        self.g.make_walls()
        self.g.make_extra_walls()
        self.g.make_trap()
        pickups.randomize(self.g)

        # Start på (17,5), loopen letar tills den hittar en ledig ruta
        x, y = 17, 5
        if not self.g.is_empty(x, y):
            for check_y in range(1, self.g.height - 1):
                for check_x in range(1, self.g.width - 1):
                    if self.g.is_empty(check_x, check_y):
                        x, y = check_x, check_y
                        break
                else:
                    continue
                break

        self.player = Player(x, y)
        self.g.set_player(self.player)