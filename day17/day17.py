init_grid = open("input.txt").read().splitlines()
size_lb, size_ub = -15, 15
grid = {(x, y, z, w): '.'
        for x in range(size_lb, size_ub)
        for y in range(size_lb, size_ub)
        for z in range(size_lb, size_ub)
        for w in range(size_lb, size_ub)}
for y, row in enumerate(init_grid):
    for x, col in enumerate(row):
        if col == '#':
            grid[(x, y, 0, 0)] = '#'
for i in range(6):
    update = []
    for square in grid.items():
        (x, y, z, w), state = square
        neighbour_states = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                for k in (-1, 0, 1):
                    for l in (-1, 0, 1):
                        neighbour = (x+i, y+j, z+k, w+l)
                        if neighbour != (x, y, z, w):
                            try:
                                neighbour_states.append(grid[neighbour])
                            except KeyError:
                                # not in the initial 4d space
                                pass
        if state == '.' and neighbour_states.count('#') == 3:
            update.append([(x, y, z, w), '#'])
        elif state == '#' and neighbour_states.count('#') not in (2, 3):
            update.append([(x, y, z, w), '.'])
    for ud in update:
        grid[ud[0]] = ud[1]
active = list(grid.values()).count('#')
print(f"Solution part 2: {active}")
