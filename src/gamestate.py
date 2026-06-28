import random
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

        # försöker starta på (17,5), om upptagen slumpar startpunkt till en ledig ruta
        x, y = 17, 5
        if not self.g.is_empty(x, y):
           while True:
              x = random.randint(1, self.g.width - 2)
              y = random.randint(1, self.g.height - 2)
              if self.g.is_empty(x, y):
                break

        self.player = Player(x, y)
        self.g.set_player(self.player)