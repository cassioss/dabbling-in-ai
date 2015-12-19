import unittest
from board import Board

test_board_1 = Board()
test_board_2 = Board()


class WinningTests(unittest.TestCase):
    def test_play(self):
        assert test_board_1.can_play_at(0, 0)
        test_board_1.play_at(0, 0, "O")
        assert not test_board_1.can_play_at(0, 0)

    def test_restart(self):
        assert test_board_2.can_play_at(0, 0)
        test_board_2.play_at(0, 0, "X")
        assert not test_board_2.can_play_at(0, 0)
        test_board_2.restart()
        assert test_board_2.can_play_at(0, 0)

    def test_play_conversion(self):
        assert test_board_1.play_to_pos(0) == test_board_1.grid[0][0]
        assert test_board_1.play_to_pos(2) == test_board_1.grid[0][2]
        assert test_board_1.play_to_pos(4) == test_board_1.grid[1][1]
        assert test_board_1.play_to_pos(5) == test_board_1.grid[1][2]
        assert test_board_1.play_to_pos(7) == test_board_1.grid[2][1]


def main():
    unittest.main()


if __name__ == '__main__':
    main()
