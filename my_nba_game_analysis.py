import re
import csv
import Find_all_player
import players_stat_lib
import match_team_lib
import devided_teams_lib
import calc_lib

def find_all_players(play_by_play):
    name_pattern = re.compile(r'\w\. \w+', re.I)  # re.I ignore case pattern
    all_players = []
    for event in play_by_play:
        name = name_pattern.search(event[-1])
        # print(event[-1])
        if name:
            all_players.append(name.group(0))
    return list(set(all_players))

def analyse_nba_game(play_by_play):
    all_players_name = Find_all_player.find_all_players(play_by_play)
    players_stats = players_stat_lib.each_players_stats(play_by_play, all_players_name)
    team_players = match_team_lib.match_to_team(play_by_play, all_players_name)
    divided = devided_teams_lib.devide_into_team(play_by_play, team_players, players_stats)
    return divided


def print_nba_game_stats(team_dict):
    headers = [k for k in team_dict['home_team']['players_data'][0].keys()]
    print(*headers, sep='\t')
    for i in team_dict['home_team']['players_data']:
        print(*i.values(), sep='\t')
    total_home = calc_lib.calculate_total_home(team_dict)
    for i in total_home:
        print('Totals \t', *i.values(), sep='\t')
    print('\n\n')
    headers = [k for k in team_dict['away_team']['players_data'][0].keys()]
    print(*headers, sep='\t')
    for i in team_dict['away_team']['players_data']:
        print(*i.values(), sep='\t')
    total_away = calc_lib.calculate_total_away(team_dict)
    for i in total_away:
        print('Totals \t', *i.values(), sep='\t')


# def _main():
#     with open('warriors_thunder_20181016.txt') as csv_text:
#         text_line = csv.reader(csv_text, delimiter='|')
#         play_by_play = [i for i in text_line]
#
#     play_by_play_moves = analyse_nba_game(play_by_play)
#     print_nba_game_stats(play_by_play_moves)
#     # print(printing)
#
#
# _main()

def load_data(filename):
    result = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        fields = next(csvreader)
        for row in csvreader:
            result.append(row)
    return result

def analyse_nba_game(play_by_play_moves):
    for play in play_by_play_moves:
        print(play)
        # break
def _main():
    play_by_play_moves = load_data(filename)
    analyse_nba_game(play_by_play_moves)

_main()
 filename = 'warriors_thunder_20181016.txt'