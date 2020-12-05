lines = open("input.txt").read().splitlines()


def split(left, right, split, start, end):
    if split == left:
        end = (end+start)//2
    if split == right:
        start = (end+start)//2
    return start, end


seat_ids = []
for line in lines:
    start = 0
    end = 128
    row = col = None
    left, right = ('F', 'B')
    for i, spl in enumerate(line):
        start, end = split(left, right, spl, start, end)
        if i == 5:
            left, right = ('L', 'R')
            row = start if line[-4] == 'F' else end-1
            start = 0
            end = 8
    col = start if line[-1] == 'F' else end-1
    seat_ids.append(row*8+col)
print("Solution part 1:", max(seat_ids))
seat_ids = sorted(seat_ids)
for i in range(len(seat_ids)):
    if int(seat_ids[i+1]) - int(seat_ids[i]) != 1:
        print("Solution part 2:", int(seat_ids[i])+1)
        exit(0)

