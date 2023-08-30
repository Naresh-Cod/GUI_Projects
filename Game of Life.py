import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the dimensions of the grid
width, height = 50, 50

# Initialize the grid with random initial states
grid = np.random.choice([0, 1], size=(width, height))


# Function to update the grid for each generation
def update(frameNum, img, grid, width, height):
    new_grid = grid.copy()
    for x in range(width):
        for y in range(height):
            # Count the live neighbors
            neighbors = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                         (x, y - 1), (x, y + 1),
                         (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]

            live_neighbors = sum(grid[i % width, j % height] for i, j in neighbors)

            # Apply the rules of the Game of Life
            if grid[x, y] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[x, y] = 0
            else:
                if live_neighbors == 3:
                    new_grid[x, y] = 1

    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img


# Create a figure and axis for visualization
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, width, height), frames=10, interval=200)

plt.show()
