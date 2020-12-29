from itertools import product

def create_grid(dimensions):
    init_grid = open("input.txt").read().splitlines()
    grid = {}
    for y, row in enumerate(init_grid):
        for x, col in enumerate(row):
            if dimensions == 4:
                grid[(x, y, 0, 0)] = col
            else:
                grid[(x, y, 0)] = col
    return grid

def add_neighbours(dimensions, grid):
    for current in [p[0] for p in grid.items() if p[1] == '#']:
        for point in product([-1, 0, 1], repeat=dimensions):
            neighbour = tuple(map(sum, zip(current, point)))
            if neighbour not in grid.keys():
                grid[neighbour] = '.'
    return grid


def run_cycles(dimensions, grid, cycles=6):
    for _ in range(cycles):
        update = []
        grid = add_neighbours(dimensions, grid)
        for square in grid.items():
            current, state = square
            neighbour_states = []
            for point in product([-1, 0, 1], repeat=dimensions):
                neighbour = tuple(map(sum, zip(current, point)))
                if neighbour != current:
                    try:
                        neighbour_states.append(grid[neighbour])
                    except KeyError:
                        pass
            if state == '.' and neighbour_states.count('#') == 3:
                update.append([current, '#'])
            elif state == '#' and neighbour_states.count('#') not in (2, 3):
                update.append([current, '.'])
        for ud in update:
            grid[ud[0]] = ud[1]
    return list(grid.values()).count('#')


part_1 = run_cycles(3, create_grid(3))
part_2 = run_cycles(4, create_grid(4))
print(f"Solution part 1: {part_1}")
print(f"Solution part 2: {part_2}")
