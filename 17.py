import numpy as np
from scipy.ndimage import convolve

def answer(init, dim, iters=6):
    active=np.pad(init[(None,)*(dim-init.ndim)], iters)
    for _ in range(iters):
        nbs=convolve(active,np.ones((3,)*dim),int,mode="constant")
        active[:] = active & (nbs==4) | (nbs==3)
    return np.sum(active)

if __name__ == "__main__":
    with open('inputs/17.txt', 'r') as file:
        lines = file.read().split("\n")

    init = np.array([list(line) for line in lines]) == '#'
    # part 1
    print(answer(init, 3))

    # part 2
    print(answer(init, 4))