from operator import mul
from functools import reduce

def get_trees(right, down, lines):
    # dimensions of forest
    width, height = len(lines[0]), len(lines)
    return sum([lines[i*down][i*right % width] == '#' for i in range(1, height//down)])

if __name__ == "__main__":
    with open('inputs/03.txt', 'r') as file:
        input = file.read()
    lines = input.split('\n')

    # part 1
    print(get_trees(3, 1, lines))

    # part 2
    slopes =  [(1,1), (3,1), (5,1), (7,1), (1,2)]
    total = reduce(mul, [get_trees(right, down, lines) for right, down in slopes])
    print(total)