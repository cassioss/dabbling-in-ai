from player import Player
from board import Board


class Game():
    def __init__(self, player_1, player_2):
        self.board = Board()
        self.player_1 = player_1
        self.player_2 = player_2
