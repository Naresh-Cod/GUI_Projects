import turtle
import math

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
kaleidoscope_turtle = turtle.Turtle()
kaleidoscope_turtle.speed(0)  # Set drawing speed to fastest

# Reflect and rotate to create a kaleidoscope pattern
def draw_kaleidoscope_pattern(num_slices, size):
    angle = 360 / num_slices

    for _ in range(num_slices):
        draw_symmetric_shapes(size)
        kaleidoscope_turtle.right(angle)

# Draw symmetric shapes (e.g., triangles, squares, circles)
def draw_symmetric_shapes(size):
    for _ in range(3):
        kaleidoscope_turtle.forward(size)
        kaleidoscope_turtle.left(120)

# Set the parameters for the kaleidoscope
num_slices = 424
shape_size = 300

# Set the initial position
kaleidoscope_turtle.penup()
kaleidoscope_turtle.goto(0, 0)
kaleidoscope_turtle.pendown()

# Draw the kaleidoscope pattern
draw_kaleidoscope_pattern(num_slices, shape_size)

# Hide the turtle
kaleidoscope_turtle.hideturtle()

# Keep the window open until it's closed by the user
turtle.done()
