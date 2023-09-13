import re
def match_to_team(play_by_play, all_players_name):
    team_player = {name: '' for name in all_players_name}
    # turnover_pattern = re.compile(r'Turnover by (\w\. \w+)', re.I)
    # p3_pattern = re.compile(r'(\S\. \S+) misses 3-pt')
    # p2_pattern = re.compile(r'(\w\. \w+) makes 2-pt')
    # pf_pattern = re.compile(r'foul by (\S\. \S+)')
    # ft_pattern = re.compile(r'(\S\. \S+) makes free throw')
    # ft_cl_pattern = re.compile(r'(\S\. \S+) makes clear path free throw')
    # enters_pattern = re.compile(r'(\S\. \S+) enters')
    turnover_pattern = re.compile(r'Turnover by (\w\. \w+-\w+)|(\w\. \w+)', re.I)
    p3_pattern = re.compile(r'(\w\. \w+-\w+)|(\w\. \w+) misses 3-pt', re.I)
    p2_pattern = re.compile(r'(\w\. \w+-\w+)|(\w\. \w+) makes 2-pt', re.I)
    pf_pattern = re.compile(r'foul by (\w\. \w+-\w+)|(\w\. \w+)', re.I)
    ft_pattern = re.compile(r'(\w\. \w+-\w+)|(\w\. \w+) makes free throw', re.I)
    rb_pattern = re.compile(r'Defensive rebound by (\w\. \w+-\w+)|(\w\. \w+)', re.I)
    enters_pattern = re.compile(r'(\w\. \w+-\w+)|(\w\. \w+) enters', re.I)
    for event in play_by_play:
        p2 = p2_pattern.search(event[-1])
        # print(p2)

        if p2:
            name = p2.group(1)
            team_player[name] = event[2]
        p3 = p3_pattern.search(event[-1])
        if p3:
            name = p3.group(1)
            team_player[name] = event[2]

        ft = ft_pattern.search(event[-1])
        if ft:
            name = ft.group(1)
            team_player[name] = event[2]
        # ft_cl = ft_cl_pattern.search(event[-1])
        # if ft_cl:
        #     name = ft_cl.group(1)
        #     team_player[name] = event[2]
        enter = enters_pattern.search(event[-1])
        if enter:
            name = enter.group(1)
            team_player[name] = event[2]
        tov = turnover_pattern.search(event[-1])
        if tov:
            name = tov.group(1)
            team_player[name] = event[2]
    return team_player