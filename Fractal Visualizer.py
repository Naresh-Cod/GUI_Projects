import tkinter as tk

# Set up the main window
root = tk.Tk()
root.title("Mandelbrot Set Visualizer")

# Set the canvas dimensions
canvas_width = 800
canvas_height = 800

# Define the complex plane boundaries
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

# Create the canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

# Function to map coordinates to complex plane
def map_to_complex(x, y):
    real = xmin + (xmax - xmin) * x / canvas_width
    imag = ymin + (ymax - ymin) * y / canvas_height
    return complex(real, imag)

# Function to determine the color of a point based on iterations
def get_color(iterations, max_iterations):
    if iterations == max_iterations:
        return "#000000"  # Black for points in the Mandelbrot Set
    else:
        t = iterations / max_iterations
        r = int(9 * (1-t) * t * t * t * 255)
        g = int(15 * (1-t) * (1-t) * t * t * 255)
        b = int(8.5 * (1-t) * (1-t) * (1-t) * t * 255)
        return f"#{r:02X}{g:02X}{b:02X}"

# Function to determine the iterations for a given point
def mandelbrot_iterations(c, max_iterations):
    z = c
    for iterations in range(max_iterations):
        if abs(z) > 2:
            return iterations
        z = z * z + c
    return max_iterations

# Draw the Mandelbrot Set on the canvas
def draw_mandelbrot():
    max_iterations = 100
    for x in range(canvas_width):
        for y in range(canvas_height):
            c = map_to_complex(x, y)
            iterations = mandelbrot_iterations(c, max_iterations)
            color = get_color(iterations, max_iterations)
            canvas.create_rectangle(x, y, x+1, y+1, fill=color, outline="")

# Draw the Mandelbrot Set
draw_mandelbrot()

root.mainloop()
