directions = open("input.txt").read().splitlines()
tiles = {(0, 0): 'white'}
step_dict = {'e': (2, 0), 'se': (1, 1), 'sw': (-1, 1), 'nw': (-1, -1),
             'w': (-2, 0), 'ne': (1, -1)}


def adjacent_hex(pos):
    adj = []
    for dx, dy in step_dict.values():
        adj.append((pos[0]+dx, pos[1]+dy))
    return adj


for direction in directions:
    i = 0
    pos = (0, 0)
    while i < len(direction):
        if direction[i] in ('s', 'n'):
            step = direction[i] + direction[i+1]
            i += 2
        else:
            step = direction[i]
            i += 1
        dx, dy = step_dict[step]
        pos = (pos[0]+dx, pos[1]+dy)
        if pos not in tiles.keys():
            tiles[pos] = 'white'

    if tiles[pos] == 'black':
        tiles[pos] = 'white'
    else:
        tiles[pos] = 'black'

black_tiles = list(tiles.values()).count('black')
print(f"Solution part 1: {black_tiles}")

# Part 2
for _ in range(100):
    for pos, color in list(tiles.items()):
        if color == 'black':
            adjacent = adjacent_hex(pos)
            for adj in adjacent:
                if adj not in tiles.keys():
                    tiles[adj] = 'white'
    copy = dict(tiles)
    for pos, color in tiles.items():
        adj_colors = []
        adjacent = adjacent_hex(pos)
        for adj in adjacent:
            try:
                adj_colors.append(tiles[adj])
            except KeyError:
                adj_colors.append('white')
        if color == 'white' and adj_colors.count('black') == 2:
            copy[pos] = 'black'
        elif color == 'black' and (adj_colors.count('black') > 2 or
                                   adj_colors.count('black') == 0):
            copy[pos] = 'white'
    tiles = copy

black_tiles = list(tiles.values()).count('black')
print(f"Solution part 2: {black_tiles}")
