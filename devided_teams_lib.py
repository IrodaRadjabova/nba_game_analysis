
def devide_into_team(play_by_play, team_players, players_stats):
    AWAY_TEAM = play_by_play[0][3]
    HOME_TEAM = play_by_play[0][4]
    divided = {"home_team": {"name": HOME_TEAM, "players_data": []},
               "away_team": {"name": AWAY_TEAM, "players_data": []}}
    divided['away_team']['name'] = AWAY_TEAM
    divided['home_team']['name'] = HOME_TEAM
    for i in players_stats:
        for k, v in team_players.items():
            if i['player_name'] == k and v == HOME_TEAM:
                divided['home_team']['players_data'].append(i)
            if i['player_name'] == k and v == AWAY_TEAM:
                divided['away_team']['players_data'].append(i)

    return divided