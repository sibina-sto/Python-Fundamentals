# 07-03. OBJECTS AND CLASSES [More Exercises]
# 03. MOBA Challenger

players = {}

while True:
    command = input()
    if command == 'Season end':
        break

    try:
        player, position, skill = command.split(' -> ')
        is_duel = False
    except ValueError:
        player_1, player_2 = command.split(' vs ')
        is_duel = True

    if not is_duel:
        if player not in players:
            players[player] = {}
        if position not in players[player]:
            players[player][position] = int(skill)
        elif int(skill) > players[player][position]:
            players[player][position] = int(skill)

    else:
        if player_1 in players and player_2 in players:
            common = ''
            for position in players[player_1].keys():
                if position in players[player_2].keys():
                    common = position
                    break
            if common is not '':
                if players[player_1][common] < players[player_2][common]:
                    players.pop(player_1)
                elif players[player_1][common] > players[player_2][common]:
                    players.pop(player_2)

players = dict(sorted(players.items(), key=lambda x: -sum(x[1].values())))

for player in players:
    players[player] = dict(sorted(players[player].items(), key=lambda x: (-x[1], x[0])))

for player in players:
    print(f'{player}: {sum(players[player].values())} skill')
    for position, skill in players[player].items():
        print(f'- {position} <::> {skill}')
