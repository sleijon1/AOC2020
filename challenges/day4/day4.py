import re
lines = open("input.txt").read()
passports = [{field.split(':')[0]:field.split(':')[1]
              for field in line.strip().replace('\n', ' ').split(' ')}
             for line in lines.split('\n\n')]
valid = [pp for pp in passports
         if len(pp.keys()) == 8 or
         len(pp.keys()) == 7
         and 'cid' not in pp.keys()]
valid2 = []
for vp in valid:
    if not (1920 <= int(vp['byr']) <= 2002):
        continue
    if not (2010 <= int(vp['iyr']) <= 2020):
        continue
    if not (2020 <= int(vp['eyr']) <= 2030):
        continue
    if vp['hgt'][-2:] == 'cm':
        if not (150 <= int(vp['hgt'][0:-2]) <= 193):
            continue
    elif vp['hgt'][-2:] == 'in':
        if not (59 <= int(vp['hgt'][0:-2]) <= 76):
            continue
    else:
        continue
    if not re.search('^#([a-z]|[0-9]){6}$', vp['hcl']):
        continue
    if not (vp['ecl'] in
            ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')):
        continue
    if not (re.search('^[0-9]{9}$', vp['pid'])):
        continue
    valid2.append(vp)
print("Solution part 1:", len(valid))
print("Solution part 2:", len(valid2))
