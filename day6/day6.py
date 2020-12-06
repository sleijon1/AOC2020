groups = open("input.txt").read().split('\n\n')
yes_count = all_yes_count = 0
for group in groups:
    all_yes = group.replace('\n', '')
    no_ppl = len(group.strip().split('\n'))
    yes_count += len(set(all_yes))
    all_yes_count += sum([1 for ans in set(all_yes)
                          if all_yes.count(ans) == no_ppl])
print(f"Solution part 1: {yes_count}")
print(f"Solution part 2: {all_yes_count}")
