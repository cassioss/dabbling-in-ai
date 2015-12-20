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

    @abstractmethod
    def strategy(self):
        while False:
            yield None