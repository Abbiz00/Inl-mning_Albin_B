#from grid import Grid

class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, dx, dy, grid):
        new_x = self.pos_x + dx
        new_y = self.pos_y + dy

        if new_x < 0 or new_x >= grid.width:
            return False
        if new_y < 0 or new_y >= grid.height:
            return False

        cell = grid.get(new_x, new_y)
        return cell != grid.wall


