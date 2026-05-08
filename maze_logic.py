import random
R, C = 20, 20

# Returns the two walls
def init_maze():
    northWall = [[1 for _ in range(C)] for _ in range(R + 1)] 
    eastWall = [[1 for _ in range(C + 1)] for _ in range(R)] 
    return northWall, eastWall

def step_generator(curr, R, C, northWall, eastWall, visited_gen, gen_stack):
    r, c = curr
    visited_gen[r][c] = True
    neighbors = []
    if r < R-1 and not visited_gen[r+1][c]: neighbors.append((r+1, c, 'N'))
    if r > 0 and not visited_gen[r-1][c]: neighbors.append((r-1, c, 'S'))
    if c < C-1 and not visited_gen[r][c+1]: neighbors.append((r, c+1, 'E'))
    if c > 0 and not visited_gen[r][c-1]: neighbors.append((r, c-1, 'W'))

    if neighbors:
        next_r, next_c, direction = random.choice(neighbors)
        gen_stack.append((r, c))
        if direction == 'N': northWall[r+1][c] = 0
        if direction == 'S': northWall[r][c] = 0
        if direction == 'E': eastWall[r][c+1] = 0
        if direction == 'W': eastWall[r][c] = 0
        return (next_r, next_c)
    elif gen_stack:
        return gen_stack.pop()
    return None