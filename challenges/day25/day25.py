door, card = list(map(int, open("input.txt").read().splitlines()))
#door = 5764801
#card = 17807724
door_ls = card_ls = None
subject = 7
value = 1
i = 0
while True:
    i += 1
    value *= subject
    value = value % 20201227
    if value == card:
        card_ls = i
    if value == door:
        door_ls = i
    if door_ls is not None and card_ls is not None:
        subject = card
        value = 1
        j = 0
        while j < door_ls:
            j += 1
            value *= subject
            value = value % 20201227
        print(f"Solution: {value}")
        break
