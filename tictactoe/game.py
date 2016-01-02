from random_player import RandomPlayer
from competitive_player import CompetitivePlayer
from board import Board
from random import randint
from win_conditions import win
from win_conditions import draw

GAME_TYPE_1 = 1
GAME_TYPE_2 = 2
GAME_TYPE_3 = 3
GAME_TYPE_4 = 4
GAME_TYPE_5 = 5
GAME_TYPE_6 = 6

NUM_OF_GAMES = 4


class Game:
    def __init__(self, game_type):
        self.board = Board()
        self.coin_toss = randint(0, 1) == 1
        self.total_of_games = 0
        self.number_of_draws = 0
        self.set_game(game_type)
        self.run()

    def set_game(self, game_type):
        if game_type is GAME_TYPE_1:
            self.player_1 = RandomPlayer(1, self.board, self.coin_tossed(True))
            self.player_2 = RandomPlayer(2, self.board, self.coin_tossed(False))

        elif game_type is GAME_TYPE_2:
            self.player_1 = RandomPlayer(1, self.board, self.coin_tossed(True))
            self.player_2 = CompetitivePlayer(2, self.board, self.coin_tossed(False))

        elif game_type is GAME_TYPE_3:
            self.player_1 = CompetitivePlayer(1, self.board, self.coin_tossed(True))
            self.player_2 = CompetitivePlayer(2, self.board, self.coin_tossed(False))

    def run(self):
        print "NEW GAME\n"
        while self.total_of_games < NUM_OF_GAMES:
            self.turn()

    def coin_tossed(self, for_player_1):
        if self.coin_toss is for_player_1:
            return "O"
        else:
            return "X"

    def print_scores(self):
        print "Player " + str(self.player_1.id) + "'s score: " + str(self.player_1.score)
        print "Player " + str(self.player_2.id) + "'s score: " + str(self.player_2.score)
        print "Number of draws: " + str(self.number_of_draws) + "\n"

    def compute_play(self, player):
        player.play()
        print self.board
        if win(self.board.grid):
            print "Player " + str(player.id) + " wins!"
            self.total_of_games += 1
            print "Number of games: " + str(self.total_of_games) + "\n"
            player.score += 1
            self.print_scores()
            return True
        elif draw(self.board.grid):
            print "It's a draw"
            self.total_of_games += 1
            print "Number of games: " + str(self.total_of_games) + "\n"
            self.number_of_draws += 1
            self.print_scores()
            return True
        else:
            return False

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
        self.board.restart()


Game(1)
