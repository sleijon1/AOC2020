lines = open("input.txt").read().splitlines()
valid_passwords_1 = valid_passwords_2 = 0
for line in lines:
    occ, char, pw = line.split(" ")
    lb, ub = occ.split("-")
    char = char[0]
    act_occ = pw.count(char)
    if int(lb) <= act_occ <= int(ub):
        valid_passwords_1 += 1
    if sum([pw[int(lb)-1] == char, pw[int(ub)-1] == char]) == 1:
        valid_passwords_2 += 1
print("Solution part 1:", valid_passwords_1)
print("Solution part 2:", valid_passwords_2)
