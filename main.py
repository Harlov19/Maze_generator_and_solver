import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from maze_logic import init_maze, step_generator 
from maze_graphics import draw_maze, draw_marker 
import random

# Constants
R, C = 20, 20
CELL_SIZE = 2.0
OFFSET_X, OFFSET_Y = -(C*CELL_SIZE)/2, -(R*CELL_SIZE)/2
ANIMATION_SPEED = 30 # speed for generation

# Data Structures
northWall, eastWall = init_maze()
visited_gen = [[False for _ in range(C)] for _ in range(R)]
gen_stack = []

def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Maze Generating...")
    
    gluPerspective(45, 1.33, 0.1, 100.0)
    glTranslatef(0.0, 0.0, -60)
    
    # Initial random starting point for the mouse
    curr_gen = (random.randint(0, R-1), random.randint(0, C-1))
    
    clock = pygame.time.Clock()
    generating = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw the walls
        draw_maze(R, C, northWall, eastWall, OFFSET_X, OFFSET_Y, CELL_SIZE)
        
        # Move the generation mouse one step
        if generating:
            next_step = step_generator(curr_gen, R, C, northWall, eastWall, visited_gen, gen_stack)
            if next_step:
                curr_gen = next_step
                
                draw_marker(curr_gen[0], curr_gen[1], (1, 1, 1), OFFSET_X, OFFSET_Y, CELL_SIZE, 10)
            else:
                generating = False
                pygame.display.set_caption("Maze Generation Complete!")

        pygame.display.flip()
        clock.tick(ANIMATION_SPEED)

if __name__ == '__main__':
    main()