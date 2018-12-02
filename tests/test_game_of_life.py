import game_of_life
import unittest


import functions
import unittest


class TestIsCellAlive(unittest.TestCase):

    def test_is_cell_alive(self):
        result = functions.is_cell_alive(False, 0)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
