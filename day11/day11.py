from copy import deepcopy as dc
grid = list(map(list, open("input.txt").read().splitlines()))

def adjacent(x, y):
    return [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1),
            (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), ]

while True:
    copy = dc(grid)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            adj = [adj for adj in adjacent(x, y) if adj[0] >= 0 and adj[1] >= 0]
            adjacent_occ = 0
            for adj_x, adj_y in adj:
                try:
                    if copy[adj_y][adj_x] == '#':
                        adjacent_occ += 1
                except IndexError:
                    pass
            if copy[y][x] == 'L' and adjacent_occ == 0:
                grid[y][x] = '#'
            elif copy[y][x] == '#' and adjacent_occ >= 4:
                grid[y][x] = 'L'
    if copy == grid:
        # no changes -> steady state
        break

occupied = sum([row.count('#') for row in grid])
print(f"Solution part 1: {occupied}")
