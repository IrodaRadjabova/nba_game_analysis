def calculate_total_home(divided):
    total_list = []
    total = {'FG': 0, 'FGA': 0, 'FG%': 0, '3P': 0, '3PA': 0, '3P%': 0, 'FT': 0, 'FTA': 0, 'FT%': 0, 'ORB': 0, 'DRB': 0,
             'TRB': 0, 'AST': 0, 'STL': 0, 'BLK': 0, 'TOV': 0, 'PF': 0, 'PTS': 0}
    for i in divided['home_team']['players_data']:
        if i['FG']:
            total['FG'] += i['FG']
        if i['FGA']:
            total['FGA'] += i['FGA']
        if i['FG%']:
            total['FG%'] = "{:.3f}".format(total['FG'] / total['FGA'])
        if i['3P']:
            total['3P'] += i['3P']
        if i['3PA']:
            total['3PA'] += i['3PA']
        if i['3P%']:
            total['3P%'] = "{:.3f}".format(total['3P'] / total['3PA'])
        if i['FT']:
            total['FT'] += i['FT']
        if i['FTA']:
            total['FTA'] += i['FTA']
        if i['FT%']:
            total['FT%'] = "{:.3f}".format(total['FT'] / total['FTA'])
        if i['ORB']:
            total['ORB'] += i['ORB']
        if i['DRB']:
            total['DRB'] += i['DRB']
        if i['TRB']:
            total['TRB'] += i['TRB']
        if i['AST']:
            total['AST'] += i['AST']
        if i['STL']:
            total['STL'] += i['STL']
        if i['BLK']:
            total['BLK'] += i['BLK']
        if i['TOV']:
            total['TOV'] += i['TOV']
        if i['PF']:
            total['PF'] += i['PF']
        if i['PTS']:
            total['PTS'] += i['PTS']
    total_list.append(total)
    return total_list


def calculate_total_away(divided):
    total_list = []
    total = {'FG': 0, 'FGA': 0, 'FG%': 0, '3P': 0, '3PA': 0, '3P%': 0, 'FT': 0, 'FTA': 0, 'FT%': 0, 'ORB': 0, 'DRB': 0,
             'TRB': 0, 'AST': 0, 'STL': 0, 'BLK': 0, 'TOV': 0, 'PF': 0, 'PTS': 0}
    for i in divided['away_team']['players_data']:
        if i['FG']:
            total['FG'] += i['FG']
        if i['FGA']:
            total['FGA'] += i['FGA']
        if i['FG%']:
            total['FG%'] = "{:.3f}".format(total['FG'] / total['FGA'])
        if i['3P']:
            total['3P'] += i['3P']
        if i['3PA']:
            total['3PA'] += i['3PA']
        if i['3P%']:
            total['3P%'] = "{:.3f}".format(total['3P'] / total['3PA'])
        if i['FT']:
            total['FT'] += i['FT']
        if i['FTA']:
            total['FTA'] += i['FTA']
        if i['FT%']:
            total['FT%'] = "{:.3f}".format(total['FT'] / total['FTA'])
        if i['ORB']:
            total['ORB'] += i['ORB']
        if i['DRB']:
            total['DRB'] += i['DRB']
        if i['TRB']:
            total['TRB'] += i['TRB']
        if i['AST']:
            total['AST'] += i['AST']
        if i['STL']:
            total['STL'] += i['STL']
        if i['BLK']:
            total['BLK'] += i['BLK']
        if i['TOV']:
            total['TOV'] += i['TOV']
        if i['PF']:
            total['PF'] += i['PF']
        if i['PTS']:
            total['PTS'] += i['PTS']
    total_list.append(total)
    return total_list