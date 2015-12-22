import unittest
from random_player import *

# Basic tests for a random player.

empty_grid = [
    [],
    [],
    []
]

partially_filled_grid = [
    ["O", "X", "O"],
    ["X", "O", "X"],
    []
]

filled_grid = [
    ["O", "X", "O"],
    ["X", "O", "X"],
    ["X", "O", "X"]
]


class RandomPlayerTests(unittest.TestCase):
    def test_empty_grid(self):
        rand_player = RandomPlayer(empty_grid, "O")
        assert rand_player.strategy() in range(0, 9)

    def test_partially_filled_grid(self):
        rand_player = RandomPlayer(partially_filled_grid, "O")
        assert rand_player.strategy() in range(6, 9)

    def test_filled_grid(self):
        rand_player = RandomPlayer(filled_grid, "O")
        print rand_player.strategy() is None


def main():
    unittest.main()


if __name__ == '__main__':
    main()
