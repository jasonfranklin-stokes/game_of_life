import rules
from devices import terminal
from services.board import Board
from services import figure
import time


def game_loop(board):

    def set_square(f_board, b_board, x, y):
        new_state = rules.infer_new_state(f_board.get_square(
            x, y), f_board.get_square_neighbors(x, y))

        b_board.set_square(x, y, new_state)

    while True:
        display_board = board.copy()
        board = Board(display_board.width, display_board.height)

        terminal.display(display_board)

        time.sleep(0.1)

        [set_square(display_board, board, x, y)
            for y in range(display_board.height) for x in range(display_board.width)]


width = 40
height = 20

board = Board(width, height)
figure.set_figure(board, figure.get_figure("tumbler"), 15, 7)

game_loop(board)
