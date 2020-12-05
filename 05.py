import numpy as np

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
    id_list = np.array([get_id(line) for line in lines])
    print(np.max(id_list))

    # part 2
    id_list = np.sort(id_list)
    diff = id_list[1:] - id_list[:-1]
    index = np.where(diff == 2)
    print(id_list[index][0] + 1)