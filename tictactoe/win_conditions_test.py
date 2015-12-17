import unittest
from win_conditions import *

horizontal_win = [
    ["O", "O", "O"],
    [None, "X", None],
    [None, "X", None]
]

vertical_win = [
    ["O", "X", "O"],
    [None, "X", None],
    [None, "X", None]
]

diagonal_win = [
    ["O", "X", "X"],
    [None, "O", None],
    [None, "X", "O"]
]

draw_grid = [
    ["O", "X", "O"],
    ["X", "O", "X"],
    ["X", "O", "X"]
]


class WinningTests(unittest.TestCase):
    def test_horizontal(self):
        assert win_horizontal_at(horizontal_win, 0)
        assert win_horizontal(horizontal_win)
        assert win(horizontal_win)
        assert not win_vertical(horizontal_win)
        assert not win_diagonal(horizontal_win)
        assert not draw(horizontal_win)

    def test_vertical(self):
        assert win_vertical_at(vertical_win, 1)
        assert win_vertical(vertical_win)
        assert win(vertical_win)
        assert not win_horizontal(vertical_win)
        assert not win_diagonal(vertical_win)
        assert not draw(vertical_win)

    def test_diagonal(self):
        assert win_main_diagonal(diagonal_win)
        assert win_diagonal(diagonal_win)
        assert win(diagonal_win)
        assert not win_horizontal(diagonal_win)
        assert not win_vertical(diagonal_win)
        assert not win_second_diagonal(diagonal_win)
        assert not draw(diagonal_win)

    def test_draw(self):
        print draw_grid[0]
        print draw_grid[0][0]
        assert draw(draw_grid)
        assert not win(draw_grid)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
