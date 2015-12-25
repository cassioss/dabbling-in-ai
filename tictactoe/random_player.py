from player import Player
import random


class RandomPlayer(Player):
    def __init__(self, board, symbol):
        Player.__init__(self, board, symbol)

    def strategy(self):
        return self.random_play()

    def available_plays(self):
        return self.board.available_plays()

    def random_play(self):
        print random.choice(self.available_plays())
