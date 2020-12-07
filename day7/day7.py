from collections import defaultdict
rules = open("input.txt").read().splitlines()
rules_dict = defaultdict(list)
for rule in rules:
    parent, children = rule.split('contain')
    for child in children.split(','):
        rules_dict[parent.strip(' ')].append(child.strip('. '))
print(rules_dict)


def shiny_gold_bag(parent: str) -> int:
    if 'no other bags' in rules_dict[parent]:
        return 0
    if ['dummy' for child in rules_dict[parent] if 'shiny gold' in child]:
        return 1
    for child in rules_dict[parent]:
        _, att_1, att_2, bags = child.split(' ')
        key = att_1 + ' ' + att_2 + ' ' + bags
        if bags[-1] == 'g':
            key += 's'
        if (shiny_gold_bag(key)):
            return 1
    return 0


containers = 0
for parent in rules_dict:
    containers += shiny_gold_bag(parent)
print(containers)
