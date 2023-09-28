import tkinter as tk
import random

# Global variables
ROWS = 10
COLS = 10
CELL_SIZE = 40

class MazeSolver:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CELL_SIZE*COLS, height=CELL_SIZE*ROWS)
        self.canvas.pack()

        self.grid = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]
        self.start = (0, 0)
        self.end = (ROWS-1, COLS-1)

        self.draw_grid()
        self.solve_maze()

    def draw_grid(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.grid[row][col] == 1:
                    self.canvas.create_rectangle(col*CELL_SIZE, row*CELL_SIZE,
                                                 (col+1)*CELL_SIZE, (row+1)*CELL_SIZE,
                                                 fill="black")

    def solve_maze(self):
        pass  # Implement your path finding algorithm here

def main():
    root = tk.Tk()
    root.title("Maze Solver")
    maze_solver = MazeSolver(root)
    root.mainloop()

if __name__ == "__main__":
    main()
