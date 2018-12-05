from services.models import figures
import sys
print(sys.path)


def get_figure(name):
    return getattr(figures, name, lambda: "figure not available")


def set_figure(board, figure, x, y):
    [board.set_square(x+i, y + j, figure[j][i]) for j in range(len(figure))
     for i in range(len(figure[0]))]
