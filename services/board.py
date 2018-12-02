class Board:

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.grid = [[False] * w for i in range(h)]

    def set_square(self, x, y, state):
        self.grid[y][x] = state

    def get_square(self, x, y):
        return self.grid[y][x]

    def get_square_neighbors(self, x, y):
        def _wrapped_point_(coordinate, limit):
            if coordinate < 0:
                return limit - abs(coordinate)
            if coordinate >= limit:
                return limit - coordinate
            return coordinate

        xl = _wrapped_point_(x-1, self.width)  # XL
        xm = _wrapped_point_(x+0, self.width)  # XM
        xr = _wrapped_point_(x+1, self.width)  # XR
        yt = _wrapped_point_(y-1, self.height)  # YT
        ym = _wrapped_point_(y+0, self.height)  # YM
        yb = _wrapped_point_(y+1, self.height)  # YB

        return [self.get_square(xl, yt),
                self.get_square(xm, yt),
                self.get_square(xr, yt),
                self.get_square(xl, ym),
                self.get_square(xr, ym),
                self.get_square(xl, yb),
                self.get_square(xm, yb),
                self.get_square(xr, yb)]

    def copy(self):
        new_board = Board(self.width, self.height)
        new_board.grid = list([i for i in self.grid])
        return new_board
