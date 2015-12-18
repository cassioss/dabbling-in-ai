#
# Adds commands to test how the tic-tac-toe board works, changes its tiles, is printed and reset.
#

# Restarts a game board, which is assumed to be rectangular.


class Board():
    rows = 3
    cols = 3
    grid = [[]]

    def __init__(self):
        self.grid = [[None for y in range(self.cols)] for x in range(self.rows)]

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

    def play_at(self, x, y, symbol):
        self.grid[x][y] = symbol

    def restart(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.grid[x][y] = None

    def can_play_at(self, x, y):
        return self.grid[x][y] is None
