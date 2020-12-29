import re
from collections import deque

rules, strings = open("input.txt").read().strip().split("\n\n")
rule_dict = {}
for rule in rules.splitlines():
    key, sub_rules = rule.split(':')
    rule_dict[key] = sub_rules.replace('"', '')

queue = deque([(key, val) for key, val
               in rule_dict.items() if val.strip(' ') in ('a', 'b')])
while queue:
    rep_key, rep_val = queue[-1]
    queue.pop()
    for key, val in rule_dict.items():
        if rep_key in val.split(' '):
            string_list = val.split(' ')
            replace_index = [i for i, el in enumerate(string_list)
                             if el == rep_key]
            for ind in replace_index:
                if '|' in rep_val:
                    string_list[ind] = '(' + rep_val + ')'
                else:
                    string_list[ind] = rep_val
            rule_dict[key] = ' '.join(string_list)
            if all(el not in rule_dict.keys() for el in set(rule_dict[key])):
                queue.appendleft((key, rule_dict[key]))
rule = rule_dict['0']
rule = rule.replace(' ', '')
match = match_2 = 0
for string in strings.splitlines():
    m_o = re.match(rule+'$', string)
    if m_o:
        match += 1

match_2 = 0
for string in strings.splitlines():
    m_o = re.match('(' + rule_dict['42'].replace(' ', '') + ')+', string)
    if m_o:
        next_i = m_o.span(0)[1]
        length = len(m_o.group(0))
        m_o = re.match('(' + rule_dict['31'].replace(' ', '') + ')+$',
                       string[next_i:])
        if m_o and len(m_o.group(0)) < length:
            match_2 += 1
print(f"Solution part 1: {match}")
print(f"Solution part 2: {match_2}")
