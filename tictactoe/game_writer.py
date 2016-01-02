# Writes the output in a file given the plays made by the players and the game result.


def write_output(plays_list, game_result):
    f = open('games.txt', 'a')
    list_to_write = str(plays_list).replace(' ', '').replace('[', '').replace(']', '') + ',' + str(game_result)
    f.write(list_to_write)
