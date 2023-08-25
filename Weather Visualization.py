import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")

# Create the Turtle objects
sun_turtle = turtle.Turtle()
cloud_turtle = turtle.Turtle()
rain_turtle = turtle.Turtle()
# wind_turtle = turtle.Turtle()

# Function to draw the sun
def draw_sun():
    sun_turtle.penup()
    sun_turtle.goto(-300, 200)
    sun_turtle.pendown()
    sun_turtle.color("yellow")
    sun_turtle.begin_fill()
    sun_turtle.circle(50)
    sun_turtle.end_fill()

# Function to draw clouds
def draw_cloud(x, y):
    cloud_turtle.penup()
    cloud_turtle.goto(x, y)
    cloud_turtle.pendown()
    cloud_turtle.color("white")
    cloud_turtle.begin_fill()
    for _ in range(2):
        cloud_turtle.circle(30, 180)
        cloud_turtle.forward(60)
    cloud_turtle.end_fill()

# Function to draw raindrops
def draw_rain(x, y):
    rain_turtle.penup()
    rain_turtle.goto(x, y)
    rain_turtle.pendown()
    rain_turtle.color("blue")
    rain_turtle.shape("triangle")
    rain_turtle.setheading(270)
    rain_turtle.shapesize(0.2, 0.5)
    rain_turtle.stamp()

# Function to simulate wind
def simulate_wind():
    for _ in range(20):
        x = random.randint(-350, 350)
        y = random.randint(-100, 100)
        draw_cloud(x, y)

    for _ in range(100):
        x = random.randint(-350, 350)
        y = random.randint(-100, 100)
        draw_rain(x, y)

# Draw the initial scene
draw_sun()
simulate_wind()

# Close the window on click
screen.exitonclick()
