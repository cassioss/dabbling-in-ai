from shutil import copyfile


# Reads all games in a file.

def read_file():
    game_results = []
    f = open('games.txt', 'r')

    for line in f:
        game_play = line.split(',')
        game_results.append(game_play)

    return game_results


def list_to_dict(game_statistics):
    game_dict = dict()

    for game_play in game_statistics:
        game_key = tuple(game_play[0:-1])
        str_value = game_play[-1].replace('\n', '')
        game_value = int(str_value)

        if game_key not in game_dict:
            game_dict[game_key] = game_value

    return game_dict


def dict_to_file(game_dict):
    f = open('games_revised.txt', 'w')
    for key, value in game_dict.iteritems():
        game = str(key).replace('(', '').replace(')', '').replace(' ', '').replace("'", "")
        game += ',' + str(value) + '\n'
        f.write(game)


def remove_duplicates():
    copyfile('games_revised.txt', 'games.txt')


game_stats = read_file()
game_hash = list_to_dict(game_stats)
dict_to_file(game_hash)
remove_duplicates()
