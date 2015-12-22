from player import Player
import random


class RandomPlayer(Player):
    def __init__(self, board, symbol):
        Player.__init__(self, board, symbol)

    def strategy(self):
        return self.random_play()

    def random_play(self):
        print self.board.available_plays
        return random.choice(self.board.available_plays)
