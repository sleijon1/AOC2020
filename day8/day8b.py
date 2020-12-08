instructions = open("input.txt").read().splitlines()
nops_jmps = [instructions.index(instruction) for instruction
             in instructions if 'nop' in instruction
             or 'jmp' in instruction]

while nops_jmps:
    copy = list(instructions) # strings are immutable -> shallow copy
    swap = nops_jmps.pop()
    if 'nop' in copy[swap]:
        copy[swap] = copy[swap].replace('nop', 'jmp')
    else:
        copy[swap] = copy[swap].replace('jmp', 'nop')
    accumulator = pointer = 0
    finished_execution = False
    while True:
        try:
            op, val = copy[pointer].split(' ')
        except IndexError:
            finished_execution = True
            print(f"Solution part 2: {accumulator}")
            exit(0)
        val = int(val)
        if op == 'jmp':
            pointer += val
        elif op == 'acc':
            pointer += 1
            accumulator += val
        elif op == 'nop':
            pointer += 1
        if accumulator > 1000: # If accumulator exceeds this -> infinite loop
            break
