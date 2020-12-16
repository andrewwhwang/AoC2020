import re

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching


def get_valid_set(rules):
    valid = set()
    for t1, t2, t3, t4 in rules:
        valid |= set(range(t1, t2 + 1))
        valid |= set(range(t3, t4 + 1))
    return valid


if __name__ == "__main__":

    with open('inputs/16.txt', 'r') as file:
        lines = file.read().split('\n')

    rules = [list(map(int, re.findall(r'\d+', x))) for x in lines[:20]]
    mine = np.array([int(x) for x in lines[22].split(',')], dtype=np.int64)
    nearby = [list(map(int, re.findall(r'\d+', x))) for x in lines[25:]]

    # Part 1
    valid = get_valid_set(rules)
    total = 0
    for line in nearby:
        for num in line:
            if num not in valid:
                total += num
    print(total)

    # Part 2
    nearby = [line for line in nearby if all(num in valid for num in line)]

    graph = []
    for j in range(len(nearby[0])):
        check = []
        for t1, t2, t3, t4 in rules:
            check.append(all((t1 <= l[j] <= t2) or (t3 <= l[j] <= t4) for l in nearby))
        graph.append(check)

    m = maximum_bipartite_matching(csr_matrix(graph))
    print(mine[m[:6]].prod())