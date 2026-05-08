import random
R, C = 20, 20

def init_maze():
    northWall = [[1 for _ in range(C)] for _ in range(R + 1)] 
    eastWall = [[1 for _ in range(C + 1)] for _ in range(R)] 
    return northWall, eastWall