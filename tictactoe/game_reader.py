# Reads all games in a file.


def read_file():
    game_stats = []
    f = open('games.txt', 'r')

    for line in f:
        game_play = line.split(',')
        game_stats.append(game_play)

    return game_stats
