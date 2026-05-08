# Maze Generator & Solver

A real-time visualization of a **depth-first search (DFS)** maze generation algorithm and a **backtracking** pathfinder. This project uses **Python**, **Pygame**, and **OpenGL** to simulate an "invisible mouse" that eats through a grid of walls to create a labyrinth and then finds its way from start to finish.

## Features

* **Real-Time Generation**: Watch the "mouse" traverse the grid and clear paths.
* **Dual-Algorithm Logic**: Uses a stack-based approach for both building and solving.
* **Visual Feedback**:
    * **White Marker**: Represents the generation mouse.
    * **Red Path**: Represents the current solver path.
    * **Blue Dots**: Represent backtracked cells (dead ends).
* **Braided Maze Support**: Includes a 5% chance to create cycles, making the maze non-perfect and testing the robustness of the solver.

---

## How it Works

### 1. The Generation (The "Mouse" Logic)
The maze is generated using a **Randomized Depth-First Search**. 
* The algorithm starts at a random cell and marks it as visited.
* It looks for unvisited neighbors, picks one at random, and "eats" the wall between them.
* The "mouse" uses a **Stack** to keep track of its path. When it reaches a cell with no unvisited neighbors, it pops the stack to backtrack until it finds a cell with a new potential path.

### 2. The Solver (Backtracking)
Once the maze is complete, a solver mouse is placed at the **Start Node (0,0)**.
* It moves toward the **End Node (R-1, C-1)** by only passing through broken walls.
* It marks its path with a **Red Stack**.
* If it hits a dead end, it backtracks and leaves a **Blue Dot** behind. Because the solver tracks "visited" cells, it cannot be trapped by cycles or infinite loops.

---

## Tech Stack

* **Language**: Python 3.x
* **Graphics**: OpenGL (via `PyOpenGL`)
* **Window Management**: Pygame
* **Coordinate System**: 2D Orthographic projection with normalized offsets for centering.

---

## 📁 Project Structure

* `main.py`: The entry point and simulation controller.
* `maze_logic.py`: The "Brain"—contains the DFS and pathfinding mathematical logic.
* `maze_graphics.py`: The "Artist"—contains all OpenGL vertex definitions and rendering functions.

---

##  Setup

1.  **Install dependencies**:
    ```bash
    pip install pygame PyOpenGL PyOpenGL_accelerate
    ```
2.  **Run the simulation**:
    ```bash
    python main.py
    ```

---

> **Note on Modularization**: This project is split into separate files to decouple the mathematical simulation from the graphical rendering, adhering to software engineering best practices.
