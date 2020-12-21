import numpy as np
from collections import deque
from scipy.ndimage import convolve

D = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}


MONSTER = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
class Tile():
    def __init__(self, id, tile):
        self.id = id
        self.coord = (0,0)
        self.tile = tile

    def rotate(self):
        self.tile = np.rot90(self.tile)
    
    def flip(self):
        self.tile = np.fliplr(self.tile)

    def get_edge(self, side):
        if side == 0:
            return self.tile[0, :]
        elif side == 1:
            return self.tile[:,-1]
        elif side == 2:
            return self.tile[-1,:]
        else:
            return self.tile[:, 0]

    def check_tile(self, target, side):
        for _ in range(2):
            self.flip()
            for _ in range(4):
                self.rotate()
                if np.array_equal(target, self.get_edge(side)):
                    return True

        return False

def parse(lines):
    id = int(lines[0][5:-1])
    tile = np.array([[0 if c == '.' else 1 for c in l] for l in lines[1:]])
    return Tile(id, tile)

def dfs(tiles_dict, start):
    # part 1
    grid = {(0, 0): start}
    placed = {start}
    queue = deque([tiles_dict[start]])

    while queue and len(grid) < len(tiles_dict):
        tile = queue.pop()
        for side in range(4):
            edge = tile.get_edge(side)
            new_coord = (tile.coord[0]+D[side][0], tile.coord[1]+D[side][1])

            if new_coord in grid:
                continue
            for id, other_tile in tiles_dict.items():
                if id in placed:
                    continue
                if other_tile.check_tile(edge, (side+2)%4):
                    placed.add(id)
                    grid[new_coord] = id
                    other_tile.coord = new_coord
                    queue.append(other_tile)
                    break
    return grid

if __name__ == "__main__":
    # parse into dict
    with open('inputs/20.txt', 'r') as file:
        chunks = file.read().split("\n\n")

    tiles_dict = {}
    for chunk in chunks:
        tile= parse(chunk.split("\n"))
        tiles_dict[tile.id] = tile
    

    # part 1
    start = int(chunks[0].split("\n")[0][5:-1])
    grid = dfs(tiles_dict, start)

    offset = min(grid.items())[0]
    grid = {(coord[0] - offset[0], coord[1] - offset[1]): id for coord, id in grid.items()}

    max_index = max(grid.items())[0][0]
    print(grid[0,0] * grid[0,max_index] * grid[max_index,0] * grid[max_index,max_index])


    # part 2
    final_grid = np.zeros((96,96),dtype=int)
    for coord, id in grid.items():
        tile = tiles_dict[id]
        tile.coord = coord

        row, col = coord[0] * 8, coord[1] * 8
        final_grid[row:row+8, col:col+8] = tile.tile[1:-1,1:-1]



    monster = np.array([[0 if c == ' ' else 1 for c in l] for l in MONSTER.split('\n')])

    # get correct orientation
    for _ in range(2):
        final_grid = np.fliplr(final_grid)
        for _ in range(4):
            final_grid = np.rot90(final_grid)
            nbs = convolve(final_grid, monster, mode="constant")
            if np.max(nbs) == 15:
                break


    nbs = convolve(final_grid, monster, mode="constant")
    num_monsters = np.sum(nbs==15)
    water = np.sum(final_grid==1) - 15 * num_monsters
    print(water)