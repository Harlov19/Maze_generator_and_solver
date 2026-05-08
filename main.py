import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from maze_logic import init_maze, step_generator, step_solver 
from maze_graphics import draw_maze, draw_marker 
import random

# Constants
R, C = 20, 20
CELL_SIZE = 2.0
OFFSET_X, OFFSET_Y = -(C*CELL_SIZE)/2, -(R*CELL_SIZE)/2
ANIMATION_SPEED = 30 

# Data Structures
northWall, eastWall = init_maze()
visited_gen = [[False for _ in range(C)] for _ in range(R)]
visited_solve = [[False for _ in range(C)] for _ in range(R)] 
gen_stack = []
solve_stack = []

START_NODE = (0, 0)
END_NODE = (R-1, C-1)
CURRENT_STEP = "GENERATING"

def main():
    global CURRENT_STEP
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Maze Generating...")
    
    gluPerspective(45, 1.33, 0.1, 100.0)
    glTranslatef(0.0, 0.0, -60)
    
    # Generation and Solving starting positions
    curr_gen = (random.randint(0, R-1), random.randint(0, C-1))
    curr_solve = START_NODE
    
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw the walls
        draw_maze(R, C, northWall, eastWall, OFFSET_X, OFFSET_Y, CELL_SIZE)
        
        # Draw Start/End Goal Markers
        draw_marker(START_NODE[0], START_NODE[1], (0, 0.8, 0), OFFSET_X, OFFSET_Y, CELL_SIZE, 18) # Green Start
        draw_marker(END_NODE[0], END_NODE[1], (1, 0.8, 0), OFFSET_X, OFFSET_Y, CELL_SIZE, 18)    # Gold End

        # Generation Logic 
        if CURRENT_STEP == "GENERATING":
            next_step = step_generator(curr_gen, R, C, northWall, eastWall, visited_gen, gen_stack)
            if next_step:
                curr_gen = next_step
                draw_marker(curr_gen[0], curr_gen[1], (1, 1, 1), OFFSET_X, OFFSET_Y, CELL_SIZE, 10)
            else:
                CURRENT_STEP = "SOLVING"
                pygame.display.set_caption("Solving Maze...")

        # Solver Logic 
        elif CURRENT_STEP == "SOLVING":
            # Draw blue dots 
            for r in range(R):
                for c in range(C):
                    if visited_solve[r][c]:
                        draw_marker(r, c, (0, 0.3, 0.8), OFFSET_X, OFFSET_Y, CELL_SIZE, 6)
            
            # Draw red markers for the current path
            for pos in solve_stack:
                draw_marker(pos[0], pos[1], (1, 0, 0), OFFSET_X, OFFSET_Y, CELL_SIZE, 10)
            
            # Move the solver one step
            next_pos, finished = step_solver(curr_solve, END_NODE, R, C, northWall, eastWall, visited_solve, solve_stack)
            curr_solve = next_pos
            
            # Draw the actual solver 
            draw_marker(curr_solve[0], curr_solve[1], (1, 0, 0), OFFSET_X, OFFSET_Y, CELL_SIZE, 12)
            
            if finished:
                CURRENT_STEP = "DONE"
                pygame.display.set_caption("Maze Solved!")

        pygame.display.flip()
        clock.tick(ANIMATION_SPEED)

if __name__ == '__main__':
    main()