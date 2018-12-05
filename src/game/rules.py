# Any live cell with fewer than two live neighbors dies, as if by underpopulation.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


def infer_new_state(current_state, neighboring_squares):
    if current_state and sum(neighboring_squares) > 3:
        return False
    if not current_state and sum(neighboring_squares) == 3:
        return True
    if (current_state and sum(neighboring_squares) < 2):
        return False
    if current_state and (sum(neighboring_squares) == 2 or sum(neighboring_squares) == 3):
        return True

    return current_state
