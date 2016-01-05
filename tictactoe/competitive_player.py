from player import Player
from random import choice
from board import Board
from collections import defaultdict


class CompetitivePlayer(Player):

    def __init__(self, player_id, board, symbol):
        Player.__init__(self, player_id, board, symbol)
        self.complete_win = defaultdict(lambda: None)
        self.add_games()

    def add_game_to_completion(self, a, b, c):
        self.complete_win[(a, b)] = self.complete_win[(b, a)] = c
        self.complete_win[(a, c)] = self.complete_win[(c, a)] = b
        self.complete_win[(b, c)] = self.complete_win[(c, b)] = a

    def add_games(self):
        self.add_game_to_completion(0, 1, 2)
        self.add_game_to_completion(0, 4, 8)
        self.add_game_to_completion(0, 3, 6)
        self.add_game_to_completion(1, 4, 7)
        self.add_game_to_completion(2, 4, 6)
        self.add_game_to_completion(2, 5, 8)
        self.add_game_to_completion(3, 4, 5)
        self.add_game_to_completion(6, 7, 8)

    def to_complete_game(self, first_play, second_play):
        return self.complete_win[(first_play, second_play)]

    def can_complete_game(self, first_play, second_play):
        play = self.to_complete_game(first_play, second_play)
        return (play is not None) and (self.board.can_play_at_number(play))

    def strategy(self):
        return self.ideal_play(len(self.board.available_plays()), self.my_plays(), self.opponent_plays())

    def ideal_play(self, available_plays, my_plays, opponent_plays):
        if available_plays == 9:
            return choice([0, 2, 6, 8])
        elif available_plays == 8:
            if Board.is_a_corner(opponent_plays.get(0)):
                return self.play_at_center()
            else:
                return self.play_at_corner()
        elif len(available_plays) == 7:
            return 0

    @staticmethod
    def play_at_corner():
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