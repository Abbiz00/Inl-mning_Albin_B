from idlelib.debugger_r import start_remote_debugger

from src.grid import Grid
from src.player import Player
from src import pickups


# TODO: flytta denna till en annan fil
class GameState:
    """Samla spelets variabler i en klass."""
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


# TODO: flytta denna till en annan fil
def print_status(game_grid, state):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {state.score} points.")
    print(game_grid)


def start(state):
    command = "a"
    count_steps = 0
    # loopa tills användaren trycker Q eller X.

    while not command.casefold() in ["q", "x"]:


        print_status(state.g, state)


        command = input("Use WASD to move, i för innehåll Q/X to quit. ")
        command = command.casefold()[:1]
        maybe_item = None # reset

        # skriver ut inventarier
        if command == "i":
            print("Inventarier:" +", ".join(state.inventory))
            continue

        if command == "d" and state.player.can_move(1, 0, state.g):  # move right
            # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
            maybe_item = state.g.get(state.player.pos_x + 1, state.player.pos_y)
            state.player.move(1, 0)

        elif command == "a" and state.player.can_move(-1, 0, state.g):  # move left
            # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
            maybe_item = state.g.get(state.player.pos_x - 1, state.player.pos_y)
            state.player.move(-1, 0)

        elif command == "s" and state.player.can_move(0, 1, state.g):  # move down
            # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
            maybe_item = state.g.get(state.player.pos_x, state.player.pos_y +1)
            state.player.move(0, 1)

        elif command == "w" and state.player.can_move(0, -1, state.g):  # move up
            # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
            maybe_item = state.g.get(state.player.pos_x, state.player.pos_y -1)
            state.player.move(0, -1)



        if isinstance(maybe_item, pickups.Item):
            # we found something
            state.score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

            #Lägger till elementen i en ny lista och sparar den i state.inventory
            state.inventory.append(maybe_item.name)
            #print(f"pickuplista: {state.inventory}") # skriver ut listan som test

        # remove one point every step if score is above zero
        if state.score > 0: state.score -= 1

    # Hit kommer vi när while-loopen slutar
    print("Thank you for playing!")


# __name__ skapas av Python och sätts till "__main__" om man startar game.py
# direkt. Detta är för att undvika att start-funktionen körs om man importerar
# saker från game.py i en annan fil, till exempel vid testning.
if __name__ == "__main__":
    game_state = GameState()
    start(game_state)
