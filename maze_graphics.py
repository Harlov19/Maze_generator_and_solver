from OpenGL.GL import *

def draw_maze(R, C, northWall, eastWall, OFFSET_X, OFFSET_Y, CELL_SIZE):
    glLineWidth(2)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    
    for r in range(R):
        for c in range(C):
            if northWall[r+1][c]:
                glVertex2f(OFFSET_X + c*CELL_SIZE, OFFSET_Y + (r+1)*CELL_SIZE)
                glVertex2f(OFFSET_X + (c+1)*CELL_SIZE, OFFSET_Y + (r+1)*CELL_SIZE)
            if eastWall[r][c+1]:
                glVertex2f(OFFSET_X + (c+1)*CELL_SIZE, OFFSET_Y + r*CELL_SIZE)
                glVertex2f(OFFSET_X + (c+1)*CELL_SIZE, OFFSET_Y + (r+1)*CELL_SIZE)
    
    for c in range(C):
        if northWall[0][c]:
            glVertex2f(OFFSET_X + c*CELL_SIZE, OFFSET_Y); glVertex2f(OFFSET_X + (c+1)*CELL_SIZE, OFFSET_Y)
    for r in range(R):
        if eastWall[r][0]:
            glVertex2f(OFFSET_X, OFFSET_Y + r*CELL_SIZE); glVertex2f(OFFSET_X, OFFSET_Y + (r+1)*CELL_SIZE)
    glEnd()

def draw_marker(r, c, color, OFFSET_X, OFFSET_Y, CELL_SIZE, size=12):
    x = OFFSET_X + c * CELL_SIZE + (CELL_SIZE / 2)
    y = OFFSET_Y + r * CELL_SIZE + (CELL_SIZE / 2)
    glColor3f(*color)
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()