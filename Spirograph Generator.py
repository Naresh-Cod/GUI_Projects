import turtle
import math
import colorsys

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Spirograph Generator")

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)
t.penup()

# User-defined parameters
R = 150  # Radius of the large circle
r = 75   # Radius of the small circle
d = 100  # Distance from the center of the small circle to the point

# Draw the spirograph pattern with multiple colors
num_colors = 72  # Number of colors (one for each degree)
for theta in range(0, 361, 5):
    # Calculate RGB color based on theta angle
    hue = theta / 360.0
    rgb = colorsys.hsv_to_rgb(hue, 1, 1)
    t.color(rgb[0], rgb[1], rgb[2])

    t.setpos(R * math.cos(math.radians(theta)), R * math.sin(math.radians(theta)))
    t.pendown()
    t.setpos((R - r) * math.cos(math.radians(theta)) + d * math.cos(math.radians((R - r) * theta / r)),
             (R - r) * math.sin(math.radians(theta)) - d * math.sin(math.radians((R - r) * theta / r)))
    t.penup()

# Hide the turtle
t.hideturtle()

# Keep the window open until closed by the user
wn.mainloop()
