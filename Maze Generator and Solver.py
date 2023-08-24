import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Create the Turtle object
maze_turtle = turtle.Turtle()
maze_turtle.speed(0)
maze_turtle.penup()

# Define maze dimensions
maze_width = 15
maze_height = 10
cell_size = 40


# Function to draw a grid for the maze
def draw_grid(width, height, cell_size):
    for row in range(height):
        for col in range(width):
            x = col * cell_size - (width * cell_size) / 2
            y = -row * cell_size + (height * cell_size) / 2
            maze_turtle.goto(x, y)
            maze_turtle.pendown()
            for _ in range(4):
                maze_turtle.forward(cell_size)
                maze_turtle.right(90)
            maze_turtle.penup()


# Function to generate a random maze using Prim's algorithm
def generate_maze(width, height):
    grid = [["wall" for _ in range(width)] for _ in range(height)]
    start_row = random.randrange(height)
    start_col = random.randrange(width)
    grid[start_row][start_col] = "path"
    walls = [(start_row - 1, start_col), (start_row, start_col - 1), (start_row, start_col + 1),
             (start_row + 1, start_col)]

    while walls:
        random_wall = random.choice(walls)
        row, col = random_wall
        if row > 0 and row < height - 1 and col > 0 and col < width - 1:
            if grid[row][col] == "wall":
                adjacent_paths = 0
                if grid[row - 1][col] == "path":
                    adjacent_paths += 1
                if grid[row + 1][col] == "path":
                    adjacent_paths += 1
                if grid[row][col - 1] == "path":
                    adjacent_paths += 1
                if grid[row][col + 1] == "path":
                    adjacent_paths += 1

                if adjacent_paths == 1:
                    grid[row][col] = "path"
                    walls.extend([(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)])

        walls.remove(random_wall)

    return grid


# Draw the maze grid
maze_turtle.color("black")
draw_grid(maze_width, maze_height, cell_size)

# Generate and draw the maze
maze = generate_maze(maze_width, maze_height)
maze_turtle.color("blue")
for row in range(maze_height):
    for col in range(maze_width):
        if maze[row][col] == "path":
            x = col * cell_size - (maze_width * cell_size) / 2 + cell_size / 2
            y = -row * cell_size + (maze_height * cell_size) / 2 - cell_size / 2
            maze_turtle.goto(x, y)
            maze_turtle.stamp()

# Close the window on click
screen.exitonclick()
