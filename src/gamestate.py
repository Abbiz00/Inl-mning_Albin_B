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
        pickups.randomize(self.g)

        # Start på (17,5), flytta ett steg i taget om blockerad
        x, y = 17, 5
        for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            if self.g.is_empty(x + dx, y + dy):
                x, y = x + dx, y + dy
                break

        self.player = Player(x, y)
        self.g.set_player(self.player)