from collections import defaultdict
rules = open("input.txt").read().splitlines()
rules_dict = defaultdict(list)
for rule in rules:
    parent, children = rule.split('contain')
    for child in children.split(','):
        rules_dict[parent.strip(' ')].append(child.strip('. '))


def shiny_gold_bag(parent: str) -> int:
    if 'no other bags' in rules_dict[parent]:
        return 0
    if ['dummy' for child in rules_dict[parent] if 'shiny gold' in child]:
        return 1
    for child in rules_dict[parent]:
        _, att_1, att_2, bags = child.split(' ')
        key = att_1 + ' ' + att_2 + ' ' + bags
        key += 's' if bags[-1] == 'g' else ''
        if (shiny_gold_bag(key)):
            return 1
    return 0


def contains(parent: str, total_bags=0) -> int:
    if 'no other bags' in rules_dict[parent]:
        return total_bags
    for child in rules_dict[parent]:
        no_bags, att_1, att_2, bags = child.split(' ')
        key = att_1 + ' ' + att_2 + ' ' + bags
        key += 's' if bags[-1] == 'g' else ''
        for i in range(int(no_bags)):
            total_bags += (1 + contains(key))
    return total_bags


containers = 0
for parent in rules_dict:
    containers += shiny_gold_bag(parent)
sg_bags = contains('shiny gold bags')
print(f"Solution part 1: {containers}")
print(f"Solution part 2: {sg_bags}")
