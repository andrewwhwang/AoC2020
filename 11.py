def get_adj(grid, row, col):
    adj = []
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == y == 0:
                continue
            if 0 <= row+x < len(grid) and 0 <= col+y < len(grid[0]):
                adj.append(grid[row+x][col+y])
    return adj

def get_los(grid, row, col):
    adj = []
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == y == 0:
                continue
            i = 1
            while 0 <= row+i*x < len(grid) and 0 <= col+i*y < len(grid[0]):
                ch = grid[row+i*x][col+i*y]
                if ch != '.':
                    adj.append(ch)
                    break
                i += 1
    return adj

def step(grid, threshold, fn):
    newgrid = []
    for row in range(len(grid)):
        newrow = []
        for col in range(len(grid[0])):
            adj = fn(grid, row, col)
            if grid[row][col] == 'L' and '#' not in adj:
                newrow.append('#') 
            elif grid[row][col] == '#' and adj.count('#') >= threshold:
                newrow.append('L')
            else:
                newrow.append(grid[row][col])
        newgrid.append("".join(newrow))
    return newgrid

if __name__ == "__main__":
    with open('inputs/11.txt', 'r') as file:
        lines = file.read().split('\n')

    # part 1
    grid = lines.copy()
    while grid != (after:=step(grid, 4, get_adj)):
        grid = after
    print(''.join(grid).count('#'))

    # part 2
    grid = lines.copy()
    while grid != (after:=step(grid, 5, get_los)):
        grid = after
    print(''.join(grid).count('#'))