directions = open("input.txt").read().splitlines()
dir_dict = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0),}
dx, dy = 10, 1
x, y = 0, 0
for direction in directions:
    move, steps = direction[0], int(direction[1:])
    if move in ('L', 'R'):
        if steps == 180:
            dx, dy = dx*-1, dy*-1
        elif steps in (90, 270):
            if move == 'L' and steps == 90 or\
               move == 'R' and steps == 270:
                dx, dy = -dy, dx
            elif move == 'R' and steps == 90 or\
                 move == 'L' and steps == 270:
                dx, dy = dy, -dx
    elif move == 'F':
        x, y = x + dx*steps, y + dy*steps
    elif move in ('N', 'S', 'E', 'W'):
        tx, ty = dir_dict[move]
        dx, dy = dx + tx*steps, dy + ty*steps
print(f"Solution part 2: {abs(x) + abs(y)}")
