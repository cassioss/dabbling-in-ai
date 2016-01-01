from random_player import RandomPlayer
from competitive_player import CompetitivePlayer
from board import Board
from random import randint

GAME_TYPE_1 = 1
GAME_TYPE_2 = 2
GAME_TYPE_3 = 3
GAME_TYPE_4 = 4
GAME_TYPE_5 = 5
GAME_TYPE_6 = 6


class Game():
    def __init__(self, game_type):
        self.board = Board()
        self.coin_toss = randint(0, 1) == 1

        if game_type is GAME_TYPE_1:
            self.player_1 = RandomPlayer(self.board, self.coin_tossed(True))
            self.player_2 = RandomPlayer(self.board, self.coin_tossed(False))

        elif game_type is GAME_TYPE_2:
            self.player_1 = RandomPlayer(self.board, self.coin_tossed(True))
            self.player_2 = CompetitivePlayer(self.board, self.coin_tossed(False))

        elif game_type is GAME_TYPE_3:
            self.player_1 = CompetitivePlayer(self.board, self.coin_tossed(True))
            self.player_2 = CompetitivePlayer(self.board, self.coin_tossed(False))

    def coin_tossed(self, is_player_1):
        if self.coin_toss is is_player_1:
            return "O"
        else:
            return "X"
