lines = open("input.txt").readlines()
nums = []
for line in lines:
    stripped = line.strip()
    nums.append(int(stripped))

for i, num in enumerate(nums):
    for j, num2 in enumerate(nums):
        for k, num3 in enumerate(nums):
            if i != k and k != j and i != j and (num2 + num3 + num) == 2020:
                print("Solution part 1: " + str(num2*num3*num))
                exit()
