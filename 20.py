import numpy as np
from collections import deque

D = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}

def array2bin(array):
    return int(''.join(str(x) for x in array), 2)

def rev(n):
    return int(format(n, '010b')[::-1], 2)

class Tile():
    def __init__(self, id, tile):
        self.edges = [array2bin(tile[0, :]), array2bin(tile[:,-1]), array2bin(tile[-1,:]), array2bin(tile[:, 0])]
        self.id = id
        self.coord = (0,0)
        self.orientation = (0,0)

    def __repr__(self):
        return str(self.id)

    def rotate(self):
        t,r,b,l = self.edges
        self.edges = [rev(l),t,rev(r),b]
        self.orientation = (self.orientation[0], (self.orientation[1]+1)%4)
    
    def flip(self):
        t,r,b,l = self.edges
        self.edges = [rev(t),l,rev(b),r]
        self.orientation = ((self.orientation[0]+1)%2, self.orientation[1])

    def check_tile(self, target, side):
        for _ in range(2):
            self.flip()
            for _ in range(4):
                self.rotate()
                # if self.id == 1427:
                #     print(self.edges)
                if target == self.edges[side]:
                    return tile

        return False

def parse(lines):
    id = int(lines[0][5:-1])
    tile = np.array([[0 if c == '.' else 1 for c in l] for l in lines[1:]])
    return Tile(id, tile)


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
    placed = {(0, 0): start}
    used = {start}
    queue = deque([tiles_dict[start]])

    while queue and len(placed) < len(tiles_dict):
        tile = queue.pop()
        for side, edge in enumerate(tile.edges):
            new_coord = (tile.coord[0]+D[side][0], tile.coord[1]+D[side][1])
            if new_coord in placed:
                continue
            for id, other_tile in tiles_dict.items():
                if id in used:
                    continue
                if other_tile.check_tile(edge, (side+2)%4):
                    used.add(id)
                    placed[new_coord]=id
                    other_tile.coord = new_coord
                    queue.append(other_tile)
                    break

    for coord, id in sorted(placed.items()):
        print(id, coord)