
def get_ingredients(lines):
    ingred = {}
    for line in lines:
        unknown, known = line.split(' (contains ')
        unknown = set(unknown.split(' '))
        known = known[:-1].split(', ')
        for k in known:
            if k in ingred:
                ingred[k] &= unknown
            else:
                ingred[k] = unknown

    while any([len(v) > 1 for v in ingred.values()]):

        ingred_list = sorted(list(ingred.items()), key=lambda x: len(x[1]))

        history = set()
        for known, unknown_set in ingred_list:
            ingred[known] -= history
            if len(unknown_set) == 1:
                history |= unknown_set

    return ingred

if __name__ == "__main__":
    with open('inputs/21.txt', 'r') as file:
        lines = file.read().split("\n")

    # part 2
    ingred = {k:list(v)[0] for k, v in get_ingredients(lines).items()}
    ingred_tuple = sorted(ingred.items())
    print(','.join([v for _, v in ingred_tuple]))


    # part 1
    unknown_set = set(ingred.values())
    total = 0
    for line in lines:
        unknown = line.split(' (contains ')[0].split(' ')
        total += sum([u not in unknown_set for u in unknown])
    print(total)