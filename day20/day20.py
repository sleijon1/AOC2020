from math import sqrt

tiles_dict = {}
with open("input.txt") as inp:
    tiles = inp.read().strip('\n').split('\n\n')
    for tile in tiles:
        id_, squares = tile.split(':')
        squares = squares.split('\n')[1:]
        id_ = id_.split(' ')[1]
        right_border = ''.join([row[-1] for row in squares])
        left_border = ''.join([row[0] for row in squares])
        borders = {'tb': squares[0], 'rb': right_border,
                   'lb': left_border, 'bb': squares[-1],
                   'rib': right_border[::-1], 'lib': left_border[::-1],
                   'bib': squares[-1][::-1], 'tib': squares[0][::-1]}
        tiles_dict[int(id_)] = borders
        print(id_, borders)

matches = {key: 0 for key in tiles_dict.keys()}
for key, val in tiles_dict.items():
    for key_2, val_2 in tiles_dict.items():
        if key != key_2:
            for b_key, border in val.items():
                for b_key_2, border_2 in val_2.items():
                    if border == border_2:
                        matches[key] += 1
                        print(f"Key {key}, Border {b_key} matching with key {key_2} border {b_key_2}")
print(matches)
edges = [key for key, val in matches.items() if val == 4]
prod = edges[0]*edges[1]*edges[2]*edges[3]
print(f"Solution {edges} part 1: {prod}")
