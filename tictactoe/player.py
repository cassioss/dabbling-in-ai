# Defines a generic player of tic-tac-toe.

from abc import ABCMeta, abstractmethod
from random import choice


class Player():
    __metaclass__ = ABCMeta
    symbol = None
    board = None

    def __init__(self, id, board, symbol):
        self.id = id
        self.board = board
        self.symbol = symbol
        self.score = 0

    def play(self):
        output = "Player " + str(self.id) + "'s turn: "
        my_play = self.strategy()
        output += str(my_play)
        print output
        self.board.play_at_num(my_play, self.symbol)

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
