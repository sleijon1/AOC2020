instructions = open("input.txt").read().splitlines()
accumulator = 0
pointer = 0
pointers = []

while True:
    if pointer in pointers:
        break
    pointers.append(pointer)
    op, val = instructions[pointer].split(' ')
    val = int(val)
    if op == 'jmp':
        pointer += val
    elif op == 'acc':
        pointer += 1
        accumulator += val
    elif op == 'nop':
        pointer += 1

print(f"Solution part 1:{accumulator}")
