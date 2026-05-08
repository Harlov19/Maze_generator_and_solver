import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from maze_logic import init_maze
from maze_graphics import draw_maze

R, C = 20, 20
CELL_SIZE = 2.0
OFFSET_X, OFFSET_Y = -(C*CELL_SIZE)/2, -(R*CELL_SIZE)/2
northWall, eastWall = init_maze()

def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    gluPerspective(45, 1.33, 0.1, 100.0)
    glTranslatef(0.0, 0.0, -60)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_maze(R, C, northWall, eastWall, OFFSET_X, OFFSET_Y, CELL_SIZE)
        pygame.display.flip()

if __name__ == '__main__': main()