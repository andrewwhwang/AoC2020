from functools import reduce

# fermat's little theorem
def inverse(a, m):
    """
        only works when m is prime
        a^(m-1) % m == 1 
        multiply both sides by a^-1
        a^(m-2) % m == a^-1
    """
    return pow(a, m - 2, m)


if __name__ == "__main__":
    with open('inputs/13.txt', 'r') as file:
        lines = file.read().split('\n')

    start = int(lines[0])
    bus_IDs = [int(id) for id in lines[1].split(',') if id !='x']

    # part 1
    times = [id - (start%id) for id in bus_IDs]
    earliest = min(times)
    print(earliest * bus_IDs[times.index(earliest)])


    # part 2
    # chinese remainder
    # https://www.youtube.com/watch?v=zIFehsBHB8o
    total_product = reduce(lambda a, b: a*b, bus_IDs)
    answer = 0
    for i, id in enumerate(lines[1].split(',')):
        if id == 'x':
            continue
        id = int(id)

        remainder = id - i
        n = total_product // id
        answer += remainder * n * inverse(n, id)

    answer %= total_product
    print(answer)
