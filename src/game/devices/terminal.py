def display(board):
    screen = ""
    for y in range(board.height):
        if not y == 0:
            screen += "\n"

        for x in range(board.width):
            screen += ("O" if board.get_square(x, y) else "-")

    print("\n" * 20)
    print(screen)
