def print_status(stdscr, game_grid, state):
    """Visa spelvärlden och antal poäng."""
    stdscr.erase()
    y = 0
    stdscr.addstr(y, 0, "--------------------------------------"); y += 1
    stdscr.addstr(y, 0, f"You have {state.score} points."); y += 1
    if state.last_revealed_item:
        stdscr.addstr(y, 0, state.last_revealed_item); y += 1
        state.last_revealed_item = None
    stdscr.addstr(y, 0, str(game_grid))
    stdscr.refresh()