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

    def winning_play(self, first_play, second_play):
        return self.complete_win[(first_play, second_play)]

    def can_complete_game(self, first_play, second_play):
        play = self.winning_play(first_play, second_play)
        return (play is not None) and (self.board.can_play_at_number(play))

    # Strategic methods - set to only allow wins and ties

    def strategy(self):
        return self.ideal_play(len(self.board.available_plays()), self.my_plays(), self.opponent_plays())

    # Non-losing strategies for the competitive player's first turn

    @staticmethod
    def first_turn():
        return choice([0, 2, 4, 6, 8])

    # Non-losing strategies for the competitive player's second turn

    @staticmethod
    def played_at_center(play):
        return play == 4

    def second_turn(self, opp_first):
        if self.played_at_center(opp_first):
            return choice([0, 2, 6, 8])
        else:
            return 4

    # Non-losing strategies for the competitive player's third turn

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

    def third_turn(self, you_first, opp_first):
        if self.played_at_corner(you_first):
            if not self.played_at_center(opp_first):
                return 4
            else:
                return self.closest_corner(you_first)

        elif self.played_at_center(you_first):
            if not self.played_at_corner(opp_first):
                return self.play_at_distant_corner(opp_first)
            else:
                return self.play_at_opposite_corner(opp_first)

    # Non-losing strategies for the competitive player's fourth turn

    def defensive_play(self, opponent_play_1, opponent_play_2):
        return self.winning_play(opponent_play_1, opponent_play_2)

    @staticmethod
    def played_at_opposite_corner(your_play, opponent_play):
        return your_play + opponent_play == 8

    @staticmethod
    def play_at_remaining_corner(your_corner):
        if your_corner is (0 or 8):
            return choice([2, 6])
        elif your_corner is (2 or 6):
            return choice([0, 8])

    @staticmethod
    def play_at_any_edge():
        return choice([1, 3, 5, 7])

    def fourth_turn(self, you_first, opp_first, opp_second):
        if self.played_at_corner(you_first):
            if self.played_at_opposite_corner(you_first, opp_second):
                return self.play_at_remaining_corner(you_first)
            else:
                return self.defensive_play(opp_first, opp_second)
        elif self.played_at_opposite_corner(opp_first, opp_second):
            return self.play_at_any_edge()
        else:
            return self.defensive_play(opp_first, opp_second)

    # Non-losing strategies for the competitive player's fifth turn - possibility to win from now on

    @staticmethod
    def keep_double_win_status(your_corner, opp_edge):
        if your_corner is 0:
            if opp_edge is 1:
                return 6
            elif opp_edge is 3:
                return 2

        elif your_corner is 2:
            if opp_edge is 1:
                return 8
            elif opp_edge is 5:
                return 0

        elif your_corner is 6:
            if opp_edge is 3:
                return 8
            elif opp_edge is 7:
                return 0

        elif your_corner is 8:
            if opp_edge is 5:
                return 6
            elif opp_edge is 7:
                return 2

    def fifth_turn(self, you_first, you_second, opp_first, opp_second):
        if self.can_complete_game(you_first, you_second):
            return self.winning_play(you_first, you_second)

        elif self.can_complete_game(opp_first, opp_second):
            return self.defensive_play(opp_first, opp_second)

        elif self.played_at_center(you_first):
            return self.keep_double_win_status(you_second, opp_second)

    # Last turn - play the only remaining game

    @staticmethod
    def last_turn(available_plays):
        return available_plays.get(0)

    # Every turn is gathered around to make the ideal play for the competitive player

    def ideal_play(self, available_plays, my_plays, opponent_plays):
        if available_plays == 9:
            return self.first_turn()
        elif available_plays == 8:
            return self.second_turn(opponent_plays.get(0))
        elif len(available_plays) == 7:
            return self.third_turn(my_plays.get(0), opponent_plays.get(0))
        elif len(available_plays) == 6:
            return self.fourth_turn(my_plays.get(0), opponent_plays.get(0), opponent_plays.get(1))
        elif len(available_plays) == 5:
            return self.fifth_turn(my_plays.get(0), my_plays.get(1), opponent_plays.get(0), opponent_plays.get(1))
        else:
            return self.random_play()
