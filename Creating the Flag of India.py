import tkinter as tk
import math

def draw_flag():
    canvas.delete("all")  # Clear the canvas

    # Draw saffron stripe
    canvas.create_rectangle(0, 0, width, stripe_height, fill="orange", outline="")

    # Draw white stripe
    canvas.create_rectangle(0, stripe_height, width, stripe_height * 2, fill="white", outline="")

    # Draw green stripe
    canvas.create_rectangle(0, stripe_height * 2, width, stripe_height * 3, fill="green", outline="")

    # Draw Ashoka Chakra (wheel)
    chakra_radius = min(stripe_height, width) // 2 - 5
    chakra_center = (width // 2, stripe_height * 1.5)
    canvas.create_oval(
        chakra_center[0] - chakra_radius,
        chakra_center[1] - chakra_radius,
        chakra_center[0] + chakra_radius,
        chakra_center[1] + chakra_radius,
        outline="navy",
        width=2
    )

    # Draw 24 spokes of the Chakra
    spoke_length = chakra_radius
    spoke_center = chakra_center
    for _ in range(24):
        end_x = spoke_center[0] + spoke_length * math.cos(math.radians(360 / 24 * _))
        end_y = spoke_center[1] - spoke_length * math.sin(math.radians(360 / 24 * _))
        canvas.create_line(spoke_center[0], spoke_center[1], end_x, end_y, fill="navy", width=2)

# Set up the main window
root = tk.Tk()
root.title("Flag of India")

# Dimensions of the flag
width = 400
height = 200
stripe_height = height // 3

# Create a canvas for drawing
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

# Create a button to draw the flag
draw_button = tk.Button(root, text="Draw Flag", command=draw_flag)
draw_button.pack()

# Start the GUI event loop
root.mainloop()
