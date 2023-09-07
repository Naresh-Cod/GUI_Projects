import turtle
import time

# Set up the Turtle screen
screen = turtle.Screen()        
screen.title("Digital Watch with Icons")
screen.setup(width=400, height=200)
screen.bgcolor("black")

# Create a Turtle object for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()

# Define icons (icons can be any ASCII art)
icons = {
    'sun': "Here goes your sun icon ASCII art",
    'moon': "Here goes your moon icon ASCII art",
    'star': "Here goes your star icon ASCII art",
    'heart': "Here goes your heart icon ASCII art",
    'flower': "Here goes your flower icon ASCII art"
}


def display_time():
    current_time = time.strftime("%H:%M:%S")
    pen.clear()
    pen.goto(0, 0)
    pen.write(current_time, align="center", font=("Courier", 24, "normal"))

    # Display an icon based on the current time
    hour = int(time.strftime("%H"))
    if 6 <= hour < 12:
        icon = icons['sun']
    elif 18 <= hour < 24:
        icon = icons['moon']
    else:
        icon = icons['star']

    pen.goto(0, -50)  # Adjust the position for the icon
    pen.write(icon, align="center", font=("Courier", 12, "normal"))

    screen.ontimer(display_time, 1000)  # Update time every second (1000 milliseconds)


# Start displaying time
display_time()

# Close the window when clicked
screen.exitonclick()
