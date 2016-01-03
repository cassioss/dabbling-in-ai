from random_player import RandomPlayer
from competitive_player import CompetitivePlayer
from board import Board
from random import randint
from win_conditions import win
from win_conditions import draw
from game_writer import write_output

GAME_TYPE_1 = 1
GAME_TYPE_2 = 2
GAME_TYPE_3 = 3
GAME_TYPE_4 = 4
GAME_TYPE_5 = 5
GAME_TYPE_6 = 6

GAMES_LIMIT = 1000000


class Game:
    def __init__(self, game_type):
        self.board = Board()
        self.coin_toss = randint(0, 1) == 1
        self.number_of_games = 0
        self.number_of_draws = 0
        self.game_plays = []

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
        print "NEW GAME\n"
        while self.number_of_games < GAMES_LIMIT:
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
        play, symbol = player.play()
        self.board.play_at_num(play, symbol)
        self.game_plays.append(play)

        print self.board

        if self.won():
            self.winner(player)
            self.print_board()
            write_output(self.game_plays, 1)
            return True

        elif self.drew():
            self.draw()
            self.print_board()
            write_output(self.game_plays, 0)
            return True

        else:
            return False

    def won(self):
        return win(self.board.grid)

    def drew(self):
        return draw(self.board.grid)

    @staticmethod
    def winner(player):
        print "Player " + str(player.id) + " wins!"
        player.score += 1

    def draw(self):
        print "It's a draw"
        self.number_of_draws += 1

    def print_board(self):
        self.number_of_games += 1
        print "Number of games: " + str(self.number_of_games) + "\n"
        self.print_scores()
        print "Plays: " + str(self.game_plays) + "\n"

    def turn(self):
        if self.coin_toss is True:
            self.take_turns(self.player_1, self.player_2)
        else:
            self.take_turns(self.player_2, self.player_1)

    def take_turns(self, first_player, second_player):
        if self.compute_play(first_player):
            self.restart()
        elif self.compute_play(second_player):
            self.restart()

    def restart(self):
        self.board.restart()
        self.game_plays = []


Game(1)
