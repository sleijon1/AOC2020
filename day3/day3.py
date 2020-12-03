from math import ceil
lines = open("input.txt").read().splitlines()
slope = []
for line in lines:
    slope.append(''.join([line for _ in
                          range(ceil(7*len(lines)/len(lines[0])))]))
movement = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tot_trees = 1
x = y = 0
trees = 0
for dxdy in movement:
    dx, dy = dxdy
    for _ in range(len(slope)//dy):
        if slope[y][x] == '#':
            trees += 1
        x += dx
        y += dy
    x = y = 0
    if dxdy == (3, 1):
        print("Solution part 1: " + str(trees))
    tot_trees *= trees
    trees = 0
print("Solution part 2:", tot_trees)
