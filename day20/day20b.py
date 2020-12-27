from math import sqrt
import sys
sys.path.append('../../')
from pyutils.geometry.square import rotations_flips

tiles_dict = {}
with open("input.txt") as inp:
    tiles = inp.read().strip('\n').split('\n\n')
    for tile in tiles:
        id_, squares = tile.split(':')
        squares = squares.split('\n')[1:]
        id_ = id_.split(' ')[1]
        tiles_dict[int(id_)] = squares

def get_borders(square: list):
    right_border = ''.join([row[-1] for row in square])
    left_border = ''.join([row[0] for row in square])
    bottom_border = square[-1]
    top_border = square[0]
    return [left_border, right_border, top_border, bottom_border]


first_key = list(tiles_dict.keys())[0]
not_matched = list(tiles_dict.keys())
not_matched.remove(first_key)
# tiles_dict after proper rotations etc.
adjusted = {first_key: tiles_dict[first_key]}
puzzle = {first_key: [0, 0]}
queue = [first_key]
coord_dict = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
while queue:
    tile = queue[0]
    queue.pop(0)
    borders = get_borders(adjusted[tile])
    # find a fitting piece for each part of the border
    # borders that are already matched wont find a match
    for i, border in enumerate(borders):
        matched = False
        for matching_tile in not_matched:
            if matched:
                matched = False
                break
            permutations = rotations_flips(tiles_dict[matching_tile])
            for j, perm in enumerate(permutations):
                # we can choose any border since we are rotating
                # and reflecting the entire tile as long as we always
                # choose the same one
                if i == 0:
                    matching_border = ''.join([row[-1] for row in perm])
                elif i == 1:
                    matching_border = ''.join([row[0] for row in perm])
                elif i == 2:
                    matching_border = perm[-1]
                elif i == 3:
                    matching_border = perm[0]
                if matching_border == border:
                    not_matched.remove(matching_tile)
                    adjusted[matching_tile] = perm
                    # position relative to current tile
                    dx, dy = coord_dict[i]
                    x, y = puzzle[tile]
                    new_x, new_y = x + dx, y + dy
                    puzzle[matching_tile] = [new_x, new_y]
                    queue.append(matching_tile)
                    matched = True
                    break
min_x = min_y = 1
max_x = max_y = 0
for x, y in puzzle.values():
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y
add_x = abs(min_x)
add_y = abs(min_y)
for key, val in puzzle.items():
    puzzle[key] = [val[0] + add_x, val[1] + add_y]
max_x = max([val[0] for val in puzzle.values()])
max_y = max([val[1] for val in puzzle.values()])
picture = [[key for i in range(max_x+1)
            for key in puzzle.keys()
            if puzzle[key] == [i, j]]
           for j in range(max_y+1)]


actual_picture = []
for row in picture:
    for tile_row in range(1, len(adjusted[row[0]])-1):
        inner_row = []
        for tile in row:
            # range for removing boundaries
            inner_row.append(adjusted[tile][tile_row][1:-1])
        actual_picture.append(''.join(inner_row))

sm_1 = "                  # "
sm_2 = "#    ##    ##    ###"
sm_3 = " #  #  #  #  #  #   "
sm_len = len(sm_1)
for perm in rotations_flips(actual_picture):
    sea_monsters = 0
    for i in range(len(actual_picture)-3):
        for j in range(len(actual_picture[0])-sm_len):
            segment_1 = perm[i][j:j+sm_len]
            segment_2 = perm[i+1][j:j+sm_len]
            segment_3 = perm[i+2][j:j+sm_len]
            match_1 = sum([1 for i, val in enumerate(segment_1) if val == sm_1[i]]) \
                == sm_1.count('#')
            match_2 = sum([1 for i, val in enumerate(segment_2) if val == sm_2[i]]) \
                == sm_2.count('#')
            match_3 = sum([1 for i, val in enumerate(segment_3) if val == sm_3[i]]) \
                == sm_3.count('#')
            if match_1 and match_2 and match_3:
                sea_monsters += 1
    if sea_monsters:
        roughness = sum([row.count('#') for row in actual_picture]) - \
            sum([sm_1.count('#'), sm_2.count('#'), sm_3.count('#')]) * \
            sea_monsters
        print(f"Solution part 2: {roughness}")
        exit(0)
















