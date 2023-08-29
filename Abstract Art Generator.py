import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Abstract Art Generator")

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)
t.penup()

# User-defined parameters
num_rays = 200  # Number of rays
canvas_size = 400  # Size of the canvas
max_ray_length = 150  # Maximum ray length
min_ray_length = 50  # Minimum ray length

# Draw the abstract art
for _ in range(num_rays):
    t.setpos(random.randint(-canvas_size // 2, canvas_size // 2),
             random.randint(-canvas_size // 2, canvas_size // 2))
    t.pendown()

    # Generate random ray length and angle
    ray_length = random.randint(min_ray_length, max_ray_length)
    angle = random.randint(0, 360)

    # Randomly choose a color
    t.color(random.random(), random.random(), random.random())

    t.setheading(angle)
    t.forward(ray_length)
    t.penup()

# Hide the turtle
t.hideturtle()

# Keep the window open until closed by the user
wn.mainloop()
