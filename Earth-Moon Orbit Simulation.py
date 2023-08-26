import turtle as t
import math

# Set up the screen
screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Earth-Moon Orbit Simulation")

# Create the Earth
earth = t.Turtle()
earth.shape("circle")
earth.color("blue")
earth.penup()
earth.goto(0, 0)
earth.speed(0)

# Create the Moon
moon = t.Turtle()
moon.shape("circle")
moon.color("gray")
moon.penup()
moon.goto(100, 0)
moon.speed(0)

# Function to update the moon's position
def update_moon_position(angle):
    x = 100 * math.cos(angle)
    y = 100 * math.sin(angle)
    moon.goto(x, y)

# Loop to simulate the Earth-Moon system
angle = 0
angle_increment = 0.01
while True:
    earth.goto(0, 0)
    update_moon_position(angle)
    angle += angle_increment
    t.update()

# Close the turtle graphics window when clicked
t.exitonclick()
