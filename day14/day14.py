import re


lines = open("input.txt").read().split('mask')
lines = [line for line in lines if line != '']
memory = {}
for seg in lines:
    mask_values = seg.strip('\n= ').split('\n')
    mask = mask_values[0]
    values = mask_values[1:]

    for value in values:
        mem_addr, value = map(int, re.findall('\d+', value))
        bin_value = format(value, '036b') # zero padding
        result = []
        for i in range(36):
            if mask[i] == 'X':
                result.append(bin_value[i])
            else:
                result.append(mask[i])
        res_val = int(''.join(result), 2)
        memory[mem_addr] = res_val
print(f"Solution part 1: {sum(memory.values())}")
