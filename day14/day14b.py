import re
import itertools

lines = open("input.txt").read().split('mask')
lines = [line for line in lines if line != '']
memory = {}
for seg in lines:
    mask_values = seg.strip('\n= ').split('\n')
    mask = mask_values[0]
    values = mask_values[1:]

    for value in values:
        mem_addr, value = map(int, re.findall('\d+', value))
        bin_value = format(mem_addr, '036b') # zero padding
        result = []
        for i in range(36):
            if mask[i] in ('X', '1'):
                result.append(mask[i])
            else:
                result.append(bin_value[i])
        res_val = ''.join(result)
        X_indices = [i for i, bit in enumerate(res_val) if bit == 'X']
        addresses_perms = list(itertools.product(['0', '1'], repeat=len(X_indices)))
        for perm in addresses_perms:
            for i, val in enumerate(perm):
                result[X_indices[i]] = val
            res_value = int(''.join(result), 2)
            memory[res_value] = value
print(f"Solution part 2: {sum(memory.values())}")
