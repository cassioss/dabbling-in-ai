from random_player import RandomPlayer
from competitive_player import CompetitivePlayer
from board import Board
from random import randint
from win_conditions import win

GAME_TYPE_1 = 1
GAME_TYPE_2 = 2
GAME_TYPE_3 = 3
GAME_TYPE_4 = 4
GAME_TYPE_5 = 5
GAME_TYPE_6 = 6

NUM_OF_GAMES = 4


class Game():
    def __init__(self, game_type):
        self.board = Board()
        self.coin_toss = randint(0, 1) == 1
        self.total_of_games = 0

        if game_type is GAME_TYPE_1:
            self.player_1 = RandomPlayer(1, self.board, self.coin_tossed(True))
            self.player_2 = RandomPlayer(2, self.board, self.coin_tossed(False))

        elif game_type is GAME_TYPE_2:
            self.player_1 = RandomPlayer(1, self.board, self.coin_tossed(True))
            self.player_2 = CompetitivePlayer(2, self.board, self.coin_tossed(False))

        elif game_type is GAME_TYPE_3:
            self.player_1 = CompetitivePlayer(1, self.board, self.coin_tossed(True))
            self.player_2 = CompetitivePlayer(2, self.board, self.coin_tossed(False))

        self.run()

    def run(self):
        while (self.total_of_games < NUM_OF_GAMES):
            self.turn()
            self.total_of_games += 1

    def coin_tossed(self, for_player_1):
        if self.coin_toss is for_player_1:
            return "O"
        else:
            return "X"

    def compute_play(self, player):
        player.play()
        print self.board
        if win(self.board.grid):
            return True

    def turn(self):
        if self.coin_toss is True:
            self.take_turns(self.player_1, self.player_2)
        else:
            self.take_turns(self.player_2, self.player_1)

    def take_turns(self, first_player, second_player):
        if self.compute_play(first_player):
            self.restart(first_player)
        elif self.compute_play(second_player):
            self.restart(second_player)

    def restart(self, player):
        player.score += 1
        self.board.restart()


Game(1)
