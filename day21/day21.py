with open("input.txt") as INP:
    lines = INP.read().splitlines()
    alg_dict = {}
    for line in lines:
        ingredients, allergens = line.split('(')
        ingredients = tuple(ingredients.strip().split(' '))
        allergens = tuple(allergens.replace('contains', '').strip(' )').split(', '))
        alg_dict[allergens] = ingredients
allergens = []
set_ingredients = []
print(alg_dict)
for tup in alg_dict.keys():
    for alg in tup:
        if alg not in allergens:
            allergens.append(alg)
    for ing in alg_dict[tup]:
        if ing not in set_ingredients:
            set_ingredients.append(ing)
reduced = {}
for allergen in allergens:
    possibly_contain = []
    remove = []
    for key in alg_dict:
        if allergen in key:
            if not possibly_contain:
                for ing in alg_dict[key]:
                    possibly_contain.append(ing)
            else:
                for ing in possibly_contain:
                    if ing not in alg_dict[key]:
                        remove.append(ing)
    possibly_contain = [el for el in possibly_contain if el not in remove]
    reduced[allergen] = possibly_contain

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
              for ingredients in alg_dict.values()])
print(f"Solution part 1: {part_1}")
