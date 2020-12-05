def get_id(line):
    row = line[:7]
    col = line[7:]
    
    row = row.replace('F', '0').replace('B', '1')
    col = col.replace('L', '0').replace('R', '1')

    return int(row, 2) * 8 + int(col, 2)


if __name__ == "__main__":
    with open('inputs/05.txt', 'r') as file:
        lines = file.read().split('\n')

    # part 1
    id_list = [get_id(line) for line in lines]
    print(max(id_list))

    # part 2
    first, last = min(id_list), max(id_list)
    print((sum(range(first, last+1)) - sum(id_list)))