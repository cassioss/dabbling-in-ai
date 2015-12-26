# Defines a generic player of tic-tac-toe.

from abc import ABCMeta, abstractmethod


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

    @abstractmethod
    def strategy(self):
        while False:
            yield None
