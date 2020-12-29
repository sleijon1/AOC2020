with open("input.txt") as INP:
    lines = INP.read().splitlines()
    alg_list = []
    for line in lines:
        ingredients, allergens = line.split('(')
        ingredients = tuple(ingredients.strip().split(' '))
        allergens = tuple(allergens.replace('contains', '').strip(' )').split(', '))
        alg_list.append([allergens, ingredients])
set_allergens = set()
set_ingredients = set()
for allergens, ingredients in alg_list:
    for alg in allergens:
        set_allergens.add(alg)
    for ing in ingredients:
        set_ingredients.add(ing)
reduced = dict()
for allergen in set_allergens:
    possibly_contain = set()
    for key, val in alg_list:
        if allergen in key:
            if not possibly_contain:
                for ing in val:
                    possibly_contain.add(ing)
            else:
                possibly_contain = possibly_contain & set(val)
    reduced[allergen] = list(possibly_contain)
while any([len(poss) != 1 for poss in reduced.values()]):
    determined = [ing[0] for ing in reduced.values() if len(ing) == 1]
    for key in reduced:
        if len(reduced[key]) != 1:
            for dtm in determined:
                if dtm in reduced[key]:
                    reduced[key].remove(dtm)

ct_allergens = [val[0] for val in reduced.values()]
no_allergens = [ing for ing in set_ingredients if ing not in ct_allergens]
part_1 = sum([sum([1 for alg in no_allergens if alg in ingredients])
              for _, ingredients in alg_list])
reverse_reduced = {val[0]: key for key, val in reduced.items()}
ct_allergens = sorted(ct_allergens,
                      key=lambda allergen: reverse_reduced[allergen])
print(f"Solution part 1: {part_1}")
print(f"Solution part 1: {','.join(ct_allergens)}")
