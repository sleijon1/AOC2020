xmas_data = list(map(int, open("input.txt").read().splitlines()))
index = 0
invalid = None
for i in range(25, len(xmas_data), 1):
    preamble = xmas_data[i-25:i]
    next_number = xmas_data[i]
    valid = False
    for val_1 in preamble:
        if valid:
            break
        for val_2 in preamble:
            if val_1 != val_2 and val_1 + val_2 == next_number:
                valid = True
                break
    if not valid:
        invalid = next_number
        print(f"Solution part 1:{next_number}")
        break


for i in range(len(xmas_data)):
    values = [xmas_data[i]]
    for j in range(i+1, len(xmas_data)):
        values.append(xmas_data[j])
        if sum(values) > invalid:
            break
        elif sum(values) == invalid:
            print(f"Solution part 2:{min(values)+max(values)}")
            exit(0)
