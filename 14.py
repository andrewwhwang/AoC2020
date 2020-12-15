def parse(filename):
    data = {}
    with open(filename, 'r') as file:
        lines = file.read().split('\n')

    mask = ''
    for line in lines:
        if line.startswith("mask"):
            mask = line[7:]
            data[mask] = []
        else:
            addr, _, val = line.split(" ")
            addr = int(addr[4:-1])
            val = int(val)
            data[mask].append((addr, val))
    return data

# returns modified value
def bitmask1(mask_and, mask_or, val):
    val &= mask_and
    val |= mask_or
    return val


# returns list of addrs
def bitmask2(mask, addr):
    addr = bin(addr)[2:].zfill(36)
    res = []
    count = mask.count('X')
    new = ''.join('{}' if v=='X' else '1' if v=='1' else addr[i] for i, v in enumerate(mask))
    for n in range(2**count):
        n = bin(n)[2:].zfill(count)
        res.append(new.format(*n))
    return [int(x, 2) for x in res]

if __name__ == "__main__":
    data = parse('inputs/14.txt')

    # part 1
    res = {}
    for mask, addrs in data.items():
        mask_and = int(mask.replace('1', '0').replace('X', '1'), 2)
        mask_or = int(mask.replace('X', '0'), 2)
        for addr, val in addrs:
            res[addr] = bitmask1(mask_and, mask_or, val)

    print(sum(res.values()))


    # part 2
    res = {}
    for mask, addrs in data.items():
        for addr, val in addrs:
            for addr in bitmask2(mask, addr):
                res[addr] = val

    print(sum(res.values()))