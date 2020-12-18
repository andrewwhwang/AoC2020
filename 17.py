import itertools

def step(cubes, dim):
    new_cubes = {}
    for coord in get_new_coords(cubes, dim):
        active_neighbors = get_active_neighbors(cubes, coord, dim)
        if (cubes.get(coord, 0) and 2 <= active_neighbors <= 3) or (not cubes.get(coord, 0) and active_neighbors == 3):
            new_cubes[coord] = 1
        else:
            new_cubes[coord] = 0
    return new_cubes

def get_active_neighbors(cubes, coord, dim):
    total = sum([cubes.get(tuple(coord[i] + offset[i] for i in range(dim)), 0) for offset in itertools.product([-1, 0, 1], repeat=dim)])
    total -= cubes.get(coord, 0)
    return total

def get_new_coords(cubes, dim):
    neighbors = set()
    for coord in cubes.keys():
        for offset in itertools.product([-1, 0, 1], repeat=dim):
            neighbors.add(tuple(coord[i] + offset[i] for i in range(dim)))
    return list(neighbors)

if __name__ == "__main__":
    with open('inputs/17.txt', 'r') as file:
        lines = file.read().split("\n")

    cubes = {}
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            cubes[(row,col,0)] = 1 if char == '#' else 0

    for _ in range(6):
        cubes = step(cubes,3)

    print(sum(cubes.values()))


    cubes = {}
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            cubes[(row,col,0, 0)] = 1 if char == '#' else 0

    for _ in range(6):
        cubes = step(cubes,4)

    print(sum(cubes.values()))