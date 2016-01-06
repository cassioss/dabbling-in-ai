import unittest
from competitive_player import *
from board import *

partially_filled_grid = [
    [None, None, None],
    [None, None, 'X'],
    [None, None, None]
]


# Basic tests for a competitive player.

class CompetitivePlayerTests(unittest.TestCase):
    partially_filled_board = Board()
    partially_filled_board.create_board_from_grid(partially_filled_grid)
    generic_id = 1
    generic_symbol = 'O'
    com_player = CompetitivePlayer(generic_id, partially_filled_board, generic_symbol)

    def test_complete_win(self):
        assert self.com_player.completes_game_in(0, 4) == 8
        assert self.com_player.completes_game_in(2, 4) == 6
        assert self.com_player.completes_game_in(0, 1) == 2
        assert self.com_player.completes_game_in(3, 4) == 5
        assert self.com_player.completes_game_in(6, 7) == 8
        assert self.com_player.completes_game_in(0, 3) == 6
        assert self.com_player.completes_game_in(1, 4) == 7
        assert self.com_player.completes_game_in(2, 5) == 8

    def test_can_complete_game(self):
        assert self.com_player.can_complete_game(0, 1)
        assert self.com_player.can_complete_game(6, 7)
        assert not self.com_player.can_complete_game(3, 4)
        assert not self.com_player.can_complete_game(3, 7)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
