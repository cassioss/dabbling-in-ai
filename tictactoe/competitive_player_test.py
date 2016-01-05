import unittest
from competitive_player import *
from board import *


# Basic tests for a competitive player.

class CompetitivePlayerTests(unittest.TestCase):
    empty_board = Board()
    generic_id = 1
    generic_symbol = 'O'
    com_player = CompetitivePlayer(generic_id, empty_board, generic_symbol)

    def test_complete_win(self):
        assert self.com_player.complete_win[(0, 4)] == 8
        assert self.com_player.complete_win[(2, 4)] == 6
        assert self.com_player.complete_win[(0, 1)] == 2
        assert self.com_player.complete_win[(3, 4)] == 5
        assert self.com_player.complete_win[(6, 7)] == 8
        assert self.com_player.complete_win[(0, 3)] == 6
        assert self.com_player.complete_win[(1, 4)] == 7
        assert self.com_player.complete_win[(2, 5)] == 8

    def test_can_complete_game(self):
        assert self.com_player.can_complete_game(0, 1)
        assert self.com_player.can_complete_game(3, 4)
        assert self.com_player.can_complete_game(3, 4)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
