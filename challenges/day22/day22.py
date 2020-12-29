players = open("input.txt").read().split('\n\n')
player_1 = list(map(int, players[0].split(':')[1].strip().split('\n')))
player_2 = list(map(int, players[1].split(':')[1].strip().split('\n')))
while player_1 and player_2:
    draw_1 = player_1[0]
    draw_2 = player_2[0]
    player_1.pop(0)
    player_2.pop(0)
    if draw_1 > draw_2:
        player_1.append(draw_1)
        player_1.append(draw_2)
    else:
        player_2.append(draw_2)
        player_2.append(draw_1)

winner = player_1 if player_1 else player_2
score = sum([(i+1)*val for i, val in
             enumerate(winner[::-1])])
print(f"Solution part 1: {score}")
