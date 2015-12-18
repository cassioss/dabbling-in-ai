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


def main():
    unittest.main()


if __name__ == '__main__':
    main()
