import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("Black")

# Create a turtle for drawing
art_turtle = turtle.Turtle()
art_turtle.speed(0)  # Set drawing speed to fastest
art_turtle.color('white')

# Simulate a random walk
def random_walk(steps, step_length):
    for _ in range(steps):
        angle = random.randint(0, 360)
        art_turtle.setheading(angle)
        art_turtle.forward(step_length)

# Set the parameters
num_steps = 2000
step_length = 10

# Set the initial position
art_turtle.penup()
art_turtle.goto(0, 0)
art_turtle.pendown()

# Perform the random walk
random_walk(num_steps, step_length)

# Hide the turtle
art_turtle.hideturtle()

# Keep the window open until it's closed by the user
turtle.done()
