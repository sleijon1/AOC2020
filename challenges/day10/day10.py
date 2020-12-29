from itertools import combinations
joltages = list(map(int, open("input.txt").read().splitlines()))
joltages.append(0)
joltages.sort()
joltages.append(joltages[-1]+3)
differences = [joltages[i+1] - joltages[i] for i in range(len(joltages)-1)]
result = differences.count(3)*differences.count(1)
print(f"Solution part 1: {result}")

arrangements = 1
permutable = []
for i in range(len(joltages)-1):
    permutable.append(joltages[i])
    if joltages[i+1] - joltages[i] == 3:
        individually_removable = []
        temp_arr = 1
        for j in range(1, len(permutable)-1):
            if permutable[j+1] - permutable[j-1] <= 3:
                individually_removable.append(permutable[j])
        for k in range(1, len(individually_removable)+1):
            comb = combinations(individually_removable, k)
            for c in list(comb):
                copy_perm = list(permutable)
                for to_rem in c:
                    copy_perm.remove(to_rem)
                differences = [copy_perm[i+1] - copy_perm[i]
                               for i in range(len(copy_perm)-1)]
                if max(differences) <= 3:
                    temp_arr += 1
        arrangements *= temp_arr
        permutable.clear()
print(f"Solution part 2: {arrangements}")
