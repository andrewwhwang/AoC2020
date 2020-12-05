# parse input into list of tuples: (low, high, letter, password)
def parse(input):
    lines = input.split('\n')
    res = []
    for line in lines:
        nums, letter, password = line.split(' ')
        low, high = nums.split('-')
        res.append((int(low), int(high), letter[:-1], password))
    return res

def part1(entry):
    low, high, letter, password = entry
    return low <= password.count(letter) <= high

def part2(entry):
    low, high, letter, password = entry
    return (password[low-1] == letter) != (password[high-1] == letter)

if __name__ == "__main__":
    with open('inputs/02.txt', 'r') as file:
        input = file.read()
    lines = parse(input)

    # part 1
    print(sum(map(part1, lines)))

    # part 2
    print(sum(map(part2, lines)))
