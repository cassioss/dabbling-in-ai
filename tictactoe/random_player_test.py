import unittest
from random_player import *
from board import *

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
        empty_board = Board()
        empty_board.create_board_from_grid(empty_grid)
        rand_player = RandomPlayer(empty_board, "O")
        play = rand_player.strategy()
        assert 0 <= play <= 8

    def test_partially_filled_grid(self):
        partially_filled_board = Board()
        partially_filled_board.create_board_from_grid(partially_filled_grid)
        rand_player = RandomPlayer(partially_filled_board, "O")
        play = rand_player.strategy()
        assert 6 <= play <= 8


def main():
    unittest.main()


if __name__ == '__main__':
    main()
