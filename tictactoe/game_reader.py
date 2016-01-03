# Reads all games in a file.


def read_file():
    game_stats = []
    f = open('games.txt', 'r')

    for line in f:
        game_play = line.split(',')
        game_stats.append(game_play)

    return game_stats


def list_to_dict(game_stats):
    game_hash = {}
    for game_play in game_stats:
        game_key = tuple(game_play[0:-2])
        game_value = game_play[-1]
        if game_value is 0:
            game_value = 1
        else:
            game_value = 100
        game_hash[game_key] = game_value
    return game_hash
