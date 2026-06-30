def print_status(game_grid, state):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {state.score} points.")
    if state.last_revealed_item:
        print(state.last_revealed_item)
        state.last_revealed_item = None
    print(game_grid)