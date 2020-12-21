from os import system
import re
import sys

rules, strings = open("input.txt").read().strip().split("\n\n")
rule_dict = {}
for rule in rules.splitlines():
    key, sub_rules = rule.split(':')
    rule_dict[key] = sub_rules.replace('"', '')
    print(rule_dict)
system('clear')

def generate_rule(rule: str):
    try:
        sub_rule = rule_dict[rule]
    except KeyError:
        return rule
    copy_rule = sub_rule
    print(copy_rule)
    print(set(sub_rule.split(' ')))
    for rule in set(sub_rule.split(' ')):
        if rule not in ('|', ' ', ''):
            print("rule:", rule)
            replacement = generate_rule(rule)
            print("replacement(rule): ", replacement)
            if '|' in replacement:
                replacement = '(' + replacement + ')'
            print("rule 2: ", rule)
            print(rule in copy_rule)
            copy_rule = copy_rule.replace(rule, replacement)
            #print("copy_rule: ", copy_rule)
    return copy_rule


rule = generate_rule('0')
rule = rule.replace(' ', '')
print(rule)
match = 0
for string in strings.splitlines():
    m_o = re.match(rule, string)
    if m_o and len(m_o.group(0)) == len(string):
        print(m_o)
        print(m_o.group(0))
        print("matching string", string)
        match += 1

print(f"Solution part 1: {match}")
print(rule_dict['8'])
