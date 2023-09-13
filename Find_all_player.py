import re
def find_all_players(play_by_play):
    name_pattern = re.compile(r'\w\. \w+', re.I)  # re.I ignore case pattern
    all_players = []
    for event in play_by_play:
        name = name_pattern.search(event[-1])
        # print(event[-1])

        if name:
            all_players.append(name.group(0))
    return list(set(all_players))
