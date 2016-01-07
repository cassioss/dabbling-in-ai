from player import Player
from random import choice
from collections import defaultdict


class CompetitivePlayer(Player):

    # Non-strategic methods - sets Player and eases how to complete games

    def __init__(self, player_id, board, symbol):
        Player.__init__(self, player_id, board, symbol)
        self.complete_win = defaultdict(lambda: None)
        self.add_games()

    def add_games(self):
        self.add_game_to_completion(0, 1, 2)
        self.add_game_to_completion(0, 4, 8)
        self.add_game_to_completion(0, 3, 6)
        self.add_game_to_completion(1, 4, 7)
        self.add_game_to_completion(2, 4, 6)
        self.add_game_to_completion(2, 5, 8)
        self.add_game_to_completion(3, 4, 5)
        self.add_game_to_completion(6, 7, 8)

    def add_game_to_completion(self, a, b, c):
        self.complete_win[(a, b)] = self.complete_win[(b, a)] = c
        self.complete_win[(a, c)] = self.complete_win[(c, a)] = b
        self.complete_win[(b, c)] = self.complete_win[(c, b)] = a

    def completes_game_in(self, first_play, second_play):
        return self.complete_win[(first_play, second_play)]

    def can_complete_game(self, first_play, second_play):
        play = self.completes_game_in(first_play, second_play)
        return (play is not None) and (self.board.can_play_at_number(play))

    # Strategic methods - set to only allow wins and ties

    def strategy(self):
        return self.ideal_play(len(self.board.available_plays()), self.my_plays(), self.opponent_plays())

    # Non-losing strategies for the first turn

    @staticmethod
    def first_turn():
        return choice([0, 2, 4, 6, 8])

    # Non-losing strategies for the second turn

    @staticmethod
    def played_at_center(play):
        return play == 4

    def second_turn(self, opponent_first_play):
        if self.played_at_center(opponent_first_play):
            return choice([0, 2, 6, 8])
        else:
            return 4

    # Non-losing strategies for the third turn

    @staticmethod
    def played_at_corner(play):
        return play == (0 or 2 or 6 or 8)

    @staticmethod
    def closest_corner(last_corner):
        if last_corner is (0 or 8):
            return choice([2, 6])
        elif last_corner is (2 or 6):
            return choice([0, 8])

    @staticmethod
    def play_at_distant_corner(edge):
        if edge is 1:
            return choice([6, 8])
        elif edge is 3:
            return choice([2, 8])
        elif edge is 5:
            return choice([0, 6])
        elif edge is 7:
            return choice([0, 2])

    @staticmethod
    def play_at_opposite_corner(corner):
        return 8 - corner

    def third_turn(self, your_first_play, opponent_first_play):
        if self.played_at_corner(your_first_play):
            if not self.played_at_center(opponent_first_play):
                return 4
            else:
                return self.closest_corner(your_first_play)

        elif self.played_at_center(your_first_play):
            if not self.played_at_corner(opponent_first_play):
                return self.play_at_distant_corner(opponent_first_play)
            else:
                return self.play_at_opposite_corner(opponent_first_play)

    def ideal_play(self, available_plays, my_plays, opponent_plays):
        if available_plays == 9:
            return self.first_turn()
        elif available_plays == 8:
            return self.second_turn(opponent_plays.get(0))
        elif len(available_plays) == 7:
            return self.third_turn(my_plays.get(0), opponent_plays.get(0))

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
