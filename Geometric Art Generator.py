import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Create the Turtle object
art_turtle = turtle.Turtle()
art_turtle.speed(0)
art_turtle.pensize(2)

# Set colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Function to draw a geometric pattern
def draw_pattern(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        art_turtle.forward(length)
        art_turtle.right(angle)

# Draw intricate geometric patterns
for _ in range(40):  # Number of patterns
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    art_turtle.penup()
    art_turtle.goto(x, y)
    art_turtle.pendown()

    sides = random.randint(3, 8)
    length = random.randint(20, 100)
    color = random.choice(colors)

    art_turtle.color(color)
    art_turtle.begin_fill()
    draw_pattern(sides, length)
    art_turtle.end_fill()

# Finish drawing and close the window
turtle.done()
