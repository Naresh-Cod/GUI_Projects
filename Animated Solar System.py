import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Create the Turtle object for the sun
sun_turtle = turtle.Turtle()
sun_turtle.shape("circle")
sun_turtle.color("yellow")
sun_turtle.penup()
sun_turtle.goto(0, 0)
sun_turtle.pendown()

# Define planet properties (name, distance from the sun, radius, color, and speed)
planets = [
    {"name": "Mercury", "distance": 50, "radius": 5, "color": "gray", "speed": 2},
    {"name": "Venus", "distance": 100, "radius": 10, "color": "orange", "speed": 1.5},
    {"name": "Earth", "distance": 150, "radius": 12, "color": "blue", "speed": 1},
    # Add more planets here
]

# Create the Turtle objects for planets
planet_turtles = []
for planet in planets:
    planet_turtle = turtle.Turtle()
    planet_turtle.shape("circle")
    planet_turtle.color(planet["color"])
    planet_turtle.penup()
    planet_turtle.goto(planet["distance"], 0)
    planet_turtle.pendown()
    planet_turtles.append(planet_turtle)

# Animate the planets' orbits
while True:
    for planet, planet_turtle in zip(planets, planet_turtles):
        angle = planet_turtle.heading() + planet["speed"]
        planet_turtle.setheading(angle)
        x = planet["distance"] * math.cos(math.radians(angle))
        y = planet["distance"] * math.sin(math.radians(angle))
        planet_turtle.goto(x, y)

# Close the window on click
screen.exitonclick()
