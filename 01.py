def parse(input):
    res = input.split('\n')
    res = [int(num) for num in res]
    return res

# O(n), Use set for constant look up times
def complement_product(target, nums):
    num_set = set(nums)
    for num in nums:
        complement = target - num
        if complement in num_set:
            return num * complement
    return None

if __name__ == "__main__":
    # get list of nums from input
    with open('inputs/01.txt', 'r') as file:
        input = file.read()
    nums = parse(input)

    # part 1
    complement = complement_product(2020, nums)
    print(complement)

    # part 2
    for num in nums:
        complement1 = 2020 - num
        complement2 = complement_product(complement1, nums)
        if complement2:
            print(num * complement2)
            break
        