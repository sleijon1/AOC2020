cups = list(map(int, list("135468729")))
cup = cups[0]
for _ in range(100):
    cup_i = cups.index(cup)
    pick_up = []
    for i in range(1, 4):
        if cup_i+i < len(cups):
            pick_up.append(cups[cup_i+i])
        else:
            pick_up.append(cups[(cup_i+i)-len(cups)])
    dest = cup-1
    while dest in pick_up or (dest not in cups):
        dest = dest-1
        if dest < min(cups):
            dest = max(cups)
    cups = [cp for cp in cups if cp not in pick_up]
    for pu_cup in pick_up[::-1]:
        cups.insert(cups.index(dest)+1, pu_cup)
    try:
        cup = cups[cups.index(cup)+1]
    except IndexError:
        cup = cups[cups.index(cup)+1-len(cups)]

part_1 = cups[cups.index(1):]+cups[:cups.index(1)]
part_1 = list(map(str, part_1[1:]))
print(f"Solution part 1: {''.join(part_1)}")
