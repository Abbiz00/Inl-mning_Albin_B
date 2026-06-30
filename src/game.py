from idlelib.debugger_r import start_remote_debugger
import curses
import random
from src.grid import Grid
from src.player import Player
from src import pickups
from src.gamestate import GameState
from src.print_s import print_status


MOVE_MAP = {
    "d": (1, 0),   # höger
    "a": (-1, 0),  # vänster
    "s": (0, 1),   # ner
    "w": (0, -1),  # upp
}


def try_move(command, state):
    """Försöker flytta spelaren baserat på kommando. Returnerar föremålet på målrutan, eller None."""
    if command not in MOVE_MAP:
        return None

    dx, dy = MOVE_MAP[command]

    if not state.player.can_move(dx, dy, state.g):
        return None

    maybe_item = state.g.get(state.player.pos_x + dx, state.player.pos_y + dy)
    state.player.move(dx, dy)
    return maybe_item


def start(stdscr, state):
    command = "a"

    while not command.casefold() in ["q", "x"]:
        print_status(stdscr, state.g, state)
        command = stdscr.getkey()
        command = command.casefold()[:1]

        # visar Inventarier
        if command == "i":
            print("Inventory: " + ", ".join(state.inventory))
            continue

        if command == "t":
            count = state.g.disarm_traps()
            if count > 0:
              print(f"Du desarmerade {count} fälla!")
            else:
              print("Det finns inga fällor att desarmera.")
            continue


        maybe_item = try_move(command, state)

        if isinstance(maybe_item, pickups.Item):
            state.score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            state.g.clear(state.player.pos_x, state.player.pos_y)
            state.inventory.append(maybe_item.name)
            state.grace_steps +=5

            # desarmerar alla fällor på spelplanen

        # Fälla minskar poängen med 10, om poäng mindre än 10 noll poäng
        elif maybe_item == "T":
            state.score -= 10

            if state.score < 0:
               state.score = 0
            print("You stepped on a trap")

        # minskar poängen med ett för varje steg
        if maybe_item is not None and state.grace_steps > 0:
            state.grace_steps -= 1
        elif maybe_item is not None and state.score > 0:
            state.score -= 1

        #Räknar steg
        if maybe_item is not None:
            state.steps +=1

        # kontrollerar om man gått 25 steg och anropar funktion för att skapa ny item
        #print(pickups.all_fruits)
        #print (state.steps)
        if state.steps % 25 == 0 and state.steps > 0 and state.steps != state.last_revealed_at:
            new_item = pickups.spawn_new_item(state.g)
            state.last_revealed_at = state.steps
            #test
            state.last_revealed_item = f"Ett nytt föremål har dykt upp: {new_item.name} (värde: {new_item.value})"

        # Exit
        if maybe_item == "E" and len(state.inventory) == pickups.total_items_spawned:
            print("Thank you for playing!")
            break


# __name__ skapas av Python och sätts till "__main__" om man startar game.py
# direkt. Detta är för att undvika att start-funktionen körs om man importerar
# saker från game.py i en annan fil, till exempel vid testning.
if __name__ == "__main__":
    game_state = GameState()
    curses.wrapper(lambda stdscr: start(stdscr, game_state))
