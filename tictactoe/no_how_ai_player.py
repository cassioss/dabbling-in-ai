from player import Player


class NoHowAIPlayer(Player):
    def __init__(self, player_id, board, symbol):
        Player.__init__(self, player_id, board, symbol)

    def strategy(self):
        return self.random_play()
