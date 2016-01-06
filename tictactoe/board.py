#
# Adds commands to test how the tic-tac-toe board works, changes its tiles, is printed and reset.
#

# Class resembling a game board, which is assumed to be rectangular.


class Board:
    rows = 3
    cols = 3

    def __init__(self):
        self.grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.cross_plays = []
        self.round_plays = []

    def __str__(self):
        output = "\n"
        for x in range(self.rows):
            for y in range(self.cols):
                if self.grid[x][y] is None:
                    output += " "
                else:
                    output += self.grid[x][y]
                if y != self.cols - 1:
                    output += "|"
            output += "\n"
            if x != self.rows - 1:
                output += "-" * (2 * self.cols - 1) + "\n"
        return output

    def create_board_from_grid(self, grid):
        self.grid = grid

    def available_plays(self):
        plays = []
        for i in range(9):
            if self.grid[i / 3][i % 3] is None:
                plays.append(i)
        return plays

    def play_at(self, x, y, symbol):
        self.grid[x][y] = symbol
        if symbol is "X":
            self.cross_plays.append(3 * x + y)
        if symbol is "O":
            self.round_plays.append(3 * x + y)

    def play_at_num(self, num, symbol):
        self.play_at(num / 3, num % 3, symbol)

    def can_play_at(self, x, y):
        return self.grid[x][y] is None

    def can_play_at_number(self, num):
        return self.can_play_at(num / 3, num % 3)

    def restart(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.grid[x][y] = None
        self.cross_plays = []
        self.round_plays = []

    def play_to_pos(self, play):
        return self.grid[play / 3][play % 3]

    @staticmethod
    def is_an_edge(play):
        return play == 1 or play == 3 or play == 5 or play == 7

    @staticmethod
    def is_a_corner(play):
        return play == 0 or play == 2 or play == 6 or play == 8
