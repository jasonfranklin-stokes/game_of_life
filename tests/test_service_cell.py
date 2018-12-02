
import functions
import unittest


class TestIsCellAlive(unittest.TestCase):

    def test_live_cell_with_less_than_two_live_neighbours(self):
        # Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        result = functions.is_cell_alive(True, 0)
        self.assertEqual(result, False)

        result = functions.is_cell_alive(True, 1)
        self.assertEqual(result, False)

    def test_live_cell_with_two_or_three_neighbours(self):
        # Any live cell with two or three live neighbors lives on to the next generation.
        result = functions.is_cell_alive(True, 2)
        self.assertEqual(result, True)

        result = functions.is_cell_alive(True, 3)
        self.assertEqual(result, True)

    def test_dead_cell_with_three_neighbours(self):
        # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        result = functions.is_cell_alive(False, 3)
        self.assertEqual(result, True)

    def test_live_cell_with_more_than_three_live_neighbours(self):
        # Any live cell with more than three live neighbors dies, as if by overpopulation.
        result = functions.is_cell_alive(True, 4)
        self.assertEqual(result, False)

    def test_dead_cell_that_does_not_have_three_live_neighbours(self):
        # any dead cell that does not have exactly 3 live neigbours should stay dead
        result = functions.is_cell_alive(False, 0)
        self.assertEqual(result, False)

        result = functions.is_cell_alive(False, 1)
        self.assertEqual(result, False)

        result = functions.is_cell_alive(False, 2)
        self.assertEqual(result, False)

        result = functions.is_cell_alive(False, 4)
        self.assertEqual(result, False)


class TestLiveNeighboursCount(unittest.TestCase):

    def test_cellS_around_live(self):
        buffer = self.get_buffer(10, 10)
        buffer[3][2] = True  # YM XL
        buffer[3][4] = True  # YM XR
        buffer[4][2] = True  # YB XL
        buffer[4][3] = True  # YB XM
        buffer[4][4] = True  # YB XR
        buffer[2][2] = True  # YT XL
        buffer[2][3] = True  # YT XM
        buffer[2][4] = True  # YT XR

        result = functions.live_neighbours_count(buffer, 10, 10, 3, 3)
        self.assertEqual(result, 8)

    def get_buffer(self, width, height):
        return [[False] * width for i in range(height)]


if __name__ == '__main__':
    unittest.main()
