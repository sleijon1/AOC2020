from copy import deepcopy as dc
grid = list(map(list, open("input.txt").read().splitlines()))

def adjacent(x, y):
    return [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1),
            (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), ]

while True:
    copy = dc(grid)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            adjacent_occ = 0
            directions = [(-1, 0), (-1, -1), (0, -1), (1, -1),
                          (1, 0), (1, 1), (0, 1), (-1, 1)]
            for dx, dy in directions:
                t_x, t_y = x, y
                while True:
                    t_x += dx
                    t_y += dy
                    if t_y < 0 or t_x < 0:
                        break
                    try:
                        if copy[t_y][t_x] == '#':
                            adjacent_occ += 1
                            break
                        elif copy[t_y][t_x] == 'L':
                            break
                    except IndexError:
                        # out of grid
                        break

            if copy[y][x] == 'L' and adjacent_occ == 0:
                grid[y][x] = '#'
            elif copy[y][x] == '#' and adjacent_occ >= 5:
                grid[y][x] = 'L'
    if copy == grid:
        # no changes -> steady state
        break

occupied = sum([row.count('#') for row in grid])
print(f"Solution part 2: {occupied}")
