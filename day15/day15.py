numbers = [1,0,15,2,10,13]
indices = {num:[i] for i, num in enumerate(numbers)}
while len(numbers) < 30000000:
    last_number = numbers[-1]
    new_key = None
    if len(indices[last_number]) == 1:
        numbers.append(0)
        new_key = 0
    else:
        numbers.append(indices[last_number][-1] - indices[last_number][-2])
        new_key = indices[last_number][-1] - indices[last_number][-2]
    try:
        indices[new_key].append(len(numbers)-1)
    except KeyError:
        indices[new_key] = [len(numbers)-1]
print(f"Solution part 2: {numbers[-1]}")
