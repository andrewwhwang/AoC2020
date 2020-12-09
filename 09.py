if __name__ == "__main__":
    with open('inputs/09.txt', 'r') as file:
        lines = file.read().split('\n')
    lines = [int(n) for n in lines]
    preamble = {n for n in lines[:25]}

    # part 1
    error = 0
    for first, line in enumerate(lines[25:]):
        if not any([line - p in preamble and line != p for p in preamble]):
            error = line
            break

        preamble.remove(lines[first])
        preamble.add(line)
        
    print(error)

    # part 2
    start, end = 0,0
    total = 0
    while total != error:
        if total < error:
            end += 1
            total += lines[end]
        elif total > error:
            start += 1
            total -= lines[start]

    print(max(lines[start+1:end+1]) + min(lines[start+1:end+1]))