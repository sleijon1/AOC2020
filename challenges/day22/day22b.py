players = open("input.txt").read().split('\n\n')
player_1 = list(map(int, players[0].split(':')[1].strip().split('\n')))
player_2 = list(map(int, players[1].split(':')[1].strip().split('\n')))


def recursive_combat(player_1, player_2):
    game_states = list()
    while player_1 and player_2:
        if [player_1, player_2] in game_states:
            return "player_1"
        game_states.append([list(player_1), list(player_2)])
        draw_1 = player_1[0]
        draw_2 = player_2[0]
        player_1.pop(0)
        player_2.pop(0)
        if len(player_1) >= draw_1 and len(player_2) >= draw_2:
            winner = recursive_combat(list(player_1[0:draw_1]), list(player_2[0:draw_2]))
        else:
            winner = "player_1" if draw_1 > draw_2 else "player_2"
        if winner == "player_1":
            player_1.append(draw_1)
            player_1.append(draw_2)
        elif winner == "player_2":
            player_2.append(draw_2)
            player_2.append(draw_1)

        if not player_1:
            return "player_2"
        elif not player_2:
            return "player_1"

ref_1 = player_1
ref_2 = player_2
winner = recursive_combat(player_1, player_2)
print("Winner:", winner)
winner = player_1 if winner == "player_1" else player_2
score = sum([(i+1)*val for i, val in
             enumerate(winner[::-1])])
print(f"Solution part 2: {score}")
