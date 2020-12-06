if __name__ == "__main__":
    with open('inputs/06.txt', 'r') as file:
        groups = file.read().split('\n\n')

    union_counter, inter_counter = 0, 0
    for group in groups:
        sets = [set(lines) for lines in group.split('\n')]
        union_counter += len(set.union(*sets))
        inter_counter += len(set.intersection(*sets))

    # part 1
    print(union_counter)

    # part 2
    print(inter_counter)
