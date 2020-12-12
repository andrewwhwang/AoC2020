import numpy as np

def combos(lines):
    cache = {0:1}
    check = set(lines)
    def helper(num):
        if num not in check:
            return 0
        if num in cache:
            return cache[num]
        cache[num] = helper(num-1)+helper(num-2)+helper(num-3)
        return cache[num]
        
    return helper(lines[-1])

if __name__ == "__main__":
    with open('inputs/10.txt', 'r') as file:
        lines = file.read().split('\n')
    lines = np.array([0] + [int(n) for n in lines])
    lines = np.sort(lines)

    # part 1
    output = np.zeros(len(lines)-1)
    output = lines[1:] - lines[:-1]

    ones = np.count_nonzero(output == 1)
    threes = np.count_nonzero(output == 3) + 1

    print(ones * threes)

    # part 2
    print(combos(lines))