rules, my_tick, nearby_tick = open("input.txt").read().strip().split("\n\n")
rules_ranges = {}
for rule in rules.splitlines():
    name, ranges = rule.split(':')
    r_1, r_2 = ranges.split(' or ')
    lb_1, ub_1 = r_1.split('-')
    lb_2, ub_2 = r_2.split('-')
    rules_ranges[name] = (list(range(int(lb_1), int(ub_1)+1)) +
                          list(range(int(lb_2), int(ub_2)+1)))
nearby_tick = nearby_tick.splitlines()[1:]
nearby_tick = [list(map(int, ticket.split(',')))
               for ticket in nearby_tick]
my_tick = my_tick.splitlines()[1:][0]
my_tick = list(map(int, my_tick.split(',')))
error_rate = 0
remove = []
for ticket in nearby_tick:
    for field_val in ticket:
        valid = False
        for ranges in rules_ranges.values():
            if field_val in ranges:
                valid = True
                break
        if not valid:
            error_rate += field_val
            remove.append(ticket)
valid_tick = [ticket for ticket in nearby_tick if ticket not in remove]
print(f"Solution part 1: {error_rate}")

fields = {}
all_possible = []
for i in range(len(rules_ranges)):
    possible = list(rules_ranges.keys())
    field_values = [ticket[i] for ticket in valid_tick]
    for value in field_values:
        for rule in possible:
            if value not in rules_ranges[rule]:
                possible.remove(rule)
    all_possible.append((i, possible))
while all_possible:
    for field_num, possible in all_possible:
        if len(possible) == 1:
            fields[field_num] = possible[0]
            all_possible.remove((field_num, possible))
            for possible_2 in all_possible:
                if possible[0] in possible_2[1]:
                    possible_2[1].remove(possible[0])
dep_prod = 1
for field in fields.items():
    if 'departure' in field[1]:
        dep_prod *= my_tick[field[0]]
print(f"Solution part 2: {dep_prod}")
