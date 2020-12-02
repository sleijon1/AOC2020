lines = open("input.txt").read().splitlines()
valid_passwords_1 = valid_passwords_2 = 0
for line in lines:
    occ, char, pw = line.replace(":","").split(" ")
    lb, ub = map(int, occ.split("-"))
    act_occ = pw.count(char)
    if lb <= act_occ <= ub:
        valid_passwords_1 += 1
    if sum([pw[lb-1] == char, pw[ub-1] == char]) == 1:
        valid_passwords_2 += 1
print("Solution part 1:", valid_passwords_1)
print("Solution part 2:", valid_passwords_2)
