# Defines a generic player of tic-tac-toe.

from abc import ABCMeta, abstractmethod
from random import choice


class Player():
    __metaclass__ = ABCMeta
    symbol = None
    board = None
    score = 0

    def __init__(self, board, symbol):
        self.board = board
        self.symbol = symbol

    def play(self):
        return self.strategy()

    def my_plays(self):
        if self.symbol is "O":
            return self.board.round_plays
        else:
            return self.board.cross_plays

    def opponent_plays(self):
        if self.symbol is "X":
            return self.board.round_plays
        else:
            return self.board.cross_plays

    def available_plays(self):
        return self.board.available_plays()

    def random_play(self):
        return choice(self.available_plays())

    @abstractmethod
    def strategy(self):
        while False:
            yield None
