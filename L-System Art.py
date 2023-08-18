import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle for drawing
lsystem_turtle = turtle.Turtle()
lsystem_turtle.speed(0)  # Set drawing speed to fastest
lsystem_turtle.color('White')

# Define the L-system rules
rules = {
    "F": "F[-F]F[+F][F]"
}

# Generate the L-system string
def generate_lsystem(axiom, rules, iterations):
    lsystem_string = axiom
    for _ in range(iterations):
        lsystem_string = "".join([rules.get(c, c) for c in lsystem_string])
    return lsystem_string

# Interpret the L-system string and draw
def draw_lsystem(t, lsystem_string, angle, distance):
    stack = []

    for char in lsystem_string:
        if char == "F":
            t.forward(distance)
        elif char == "+":
            t.right(angle)
        elif char == "-":
            t.left(angle)
        elif char == "[":
            stack.append((t.heading(), t.pos()))
        elif char == "]":
            heading, pos = stack.pop()
            t.penup()
            t.goto(pos)
            t.setheading(heading)
            t.pendown()

# Set the L-system parameters
axiom = "F"
iterations = 4
angle = 25
distance = 10

# Generate and draw the L-system pattern
lsystem_string = generate_lsystem(axiom, rules, iterations)
lsystem_turtle.penup()
lsystem_turtle.goto(0, -200)
lsystem_turtle.setheading(90)
lsystem_turtle.pendown()
draw_lsystem(lsystem_turtle, lsystem_string, angle, distance)

# Hide the turtle
lsystem_turtle.hideturtle()

# Keep the window open until it's closed by the user
turtle.done()
