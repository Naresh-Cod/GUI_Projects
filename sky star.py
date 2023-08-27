import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Create the Turtle object
sky_turtle = turtle.Turtle()
sky_turtle.speed(0)  # Set the drawing speed to the fastest

# Generate random star positions
num_stars = 50
stars = []
for _ in range(num_stars):
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    stars.append((x, y))

# Draw stars
sky_turtle.penup()
sky_turtle.color("white")
for x, y in stars:
    sky_turtle.goto(x, y)
    sky_turtle.dot(random.randint(1, 5))  # Vary the size of stars

# Draw connecting lines to simulate constellation
sky_turtle.pendown()
sky_turtle.color("gray")
for i in range(num_stars):
    for j in range(i + 1, num_stars):
        if random.random() < 0.1:  # Probability of drawing a line
            x1, y1 = stars[i]
            x2, y2 = stars[j]
            sky_turtle.penup()
            sky_turtle.goto(x1, y1)
            sky_turtle.pendown()
            sky_turtle.goto(x2, y2)

# Finish drawing and close the window
turtle.done()
