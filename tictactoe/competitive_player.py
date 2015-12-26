from player import Player
from random import choice
from board import Board


class CompetitivePlayer(Player):
    def __init__(self, board, symbol):
        Player.__init__(self, board, symbol)

    def strategy(self):
        return self.ideal_play(self.board.available_plays(), self.my_plays(), self.opponent_plays())

    def ideal_play(self, available_plays, my_plays, opponent_plays):
        if len(available_plays) == 9:
            return choice([0, 2, 6, 8])
        elif len(available_plays) == 8:
            if Board.is_a_corner(opponent_plays.get(0)):
                return self.play_at_center()
            else:
                return self.play_at_corners()
        else:
            return 0

    @staticmethod
    def play_at_corners():
        return choice([0, 2, 6, 8])

    @staticmethod
    def play_at_center():
        return 4
