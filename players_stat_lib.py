import re

def each_players_stats(play_by_play, all_players_name):
    players_stats = []

    p2_pattern = re.compile(r'(\w\. \w+) makes 2-pt', re.I)
    p2m_pattern = re.compile(r'(\w\. \w+) misses 2-pt', re.I)
    p3_pattern = re.compile(r'(\w\. \w+) makes 3-pt', re.I)
    p3m_pattern = re.compile(r'(\w\. \w+) misses 3-pt', re.I)
    orb_pattern = re.compile(r'Offensive rebound by (\w\. \w+)', re.I)
    ft_pattern = re.compile(r'(\w\. \w+) makes free throw', re.I)
    ft_1_pattern = re.compile(r'(\w\. \w+) makes clear path free throw', re.I)
    ft_misses_pattern = re.compile(r'(\w\. \w+) misses free throw', re.I)

    pf_pattern = re.compile(r'foul by (\w\. \w+)', re.I)
    defens_pattern = re.compile(r'Defensive rebound by (\w\. \w+)', re.I)
    turnover_pattern = re.compile(r'Turnover by (\w\. \w+)', re.I)
    stl_pattern = re.compile(r'steal by (\w\. \w+)', re.I)
    blk_pattern = re.compile(r'block by (\w\. \w+)', re.I)
    ast_pattern = re.compile(r'assist by (\w\. \w+)', re.I)
    for player_name in all_players_name:
        each_player_stat = {"player_name": 0, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0,
                            "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0,
                            "PF": 0, "PTS": 0}
        p2_count = 0
        each_player_stat['player_name'] = player_name
        for i in play_by_play:
            p3 = p3_pattern.search(i[-1])
            if p3:
                if p3.group(1) == player_name:
                    each_player_stat['3P'] += 1
                    each_player_stat['3PA'] += 1
                    each_player_stat['FG'] += 1
                    each_player_stat['FGA'] += 1
            p3_a = p3m_pattern.search(i[-1])
            if p3_a:
                if p3_a.group(1) == player_name:
                    each_player_stat['3PA'] += 1
                    each_player_stat['FGA'] += 1
            p2 = p2_pattern.search(i[-1])
            if p2:
                if p2.group(1) == player_name:
                    each_player_stat['FG'] += 1
                    each_player_stat['FGA'] += 1
                    p2_count += 1
            p2a = p2m_pattern.search(i[-1])
            if p2a:
                if p2a.group(1) == player_name:
                    each_player_stat['FGA'] += 1
            ft = ft_pattern.search(i[-1])
            if ft:
                if ft.group(1) == player_name:
                    each_player_stat['FT'] += 1
                    each_player_stat['FTA'] += 1
            ft1 = ft_1_pattern.search(i[-1])
            if ft1:
                if ft1.group(1) == player_name:
                    each_player_stat['FT'] += 1
                    each_player_stat['FTA'] += 1
            fta = ft_misses_pattern.search(i[-1])
            if fta:
                if fta.group(1) == player_name:
                    each_player_stat['FTA'] += 1
            orb = orb_pattern.search(i[-1])
            if orb:
                if orb.group(1) == player_name:
                    each_player_stat['ORB'] += 1
                    each_player_stat['TRB'] += 1
            drb = defens_pattern.search(i[-1])
            if drb:
                if drb.group(1) == player_name:
                    each_player_stat['DRB'] += 1
                    each_player_stat['TRB'] += 1
            ast = ast_pattern.search(i[-1])
            if ast:
                if ast.group(1) == player_name:
                    each_player_stat['AST'] += 1
            stl = stl_pattern.search(i[-1])
            if stl:
                if stl.group(1) == player_name:
                    each_player_stat['STL'] += 1
            blk = blk_pattern.search(i[-1])
            if blk:
                if blk.group(1) == player_name:
                    each_player_stat["BLK"] += 1
            tov = turnover_pattern.search(i[-1])
            if tov:
                if tov.group(1) == player_name:
                    each_player_stat['TOV'] += 1
            pf = pf_pattern.search(i[-1])
            if pf:
                if pf.group(1) == player_name:
                    each_player_stat['PF'] += 1
        each_player_stat['PTS'] = (each_player_stat['3P'] * 3) + (p2_count * 2) + each_player_stat['FT']
        if each_player_stat['FG'] != 0 and each_player_stat['FGA'] != 0:
            each_player_stat['FG%'] = "{:.3f}".format(each_player_stat['FG'] / each_player_stat['FGA'])
        if each_player_stat['3P'] != 0 and each_player_stat['3PA'] != 0:
            each_player_stat['3P%'] = "{:.3f}".format(each_player_stat['3P'] / each_player_stat['3PA'])
        if each_player_stat['FT'] != 0 and each_player_stat['FTA'] != 0:
            each_player_stat['FT%'] = "{:.3f}".format(each_player_stat['FT'] / each_player_stat['FTA'])
        players_stats.append(each_player_stat)

    return players_stats

