from player import Player


class CompetitivePlayer(Player):
    def __init__(self, board, symbol):
        Player.__init__(self, board, symbol)

    def strategy(self):
        return self.ideal_play()

    def ideal_play(self):
        return 0
