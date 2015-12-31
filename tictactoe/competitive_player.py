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

    @staticmethod
    def play_at_adjacent_corner(previous_corner, opponent_play):
        if previous_corner is (0 or 8):
            if opponent_play is not (0 or 1 or 2 or 5 or 8):
                return 2
            else:
                return 6
        elif previous_corner is (2 or 6):
            if opponent_play is not (2 or 5 or 6 or 7 or 8):
                return 8
            else:
                return 0

    @staticmethod
    def complete_win(first_play, second_play):
        if first_play is 0:
            if second_play is 1:
                return 2
            if second_play is 2:
                return 1
            if second_play is 3:
                return 6
            if second_play is 6:
                return 3
            else:
                return 8
        else:
            return 2

