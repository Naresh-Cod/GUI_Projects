import tkinter as tk
import math

# Set up the main window
root = tk.Tk()
root.title("Interactive Spirograph")

# Set the canvas dimensions
canvas_width = 800
canvas_height = 600

# Create the canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Initialize the spirograph parameters
R = 150
r = 50
d = 100

# Function to draw the spirograph
def draw_spirograph(R, r, d):
    canvas.delete("all")
    angle = 0
    while angle < 360 * 10:
        theta = math.radians(angle)
        x = (R - r) * math.cos(theta) + d * math.cos((R - r) * theta / r)
        y = (R - r) * math.sin(theta) - d * math.sin((R - r) * theta / r)
        canvas.create_oval(canvas_width / 2 + x, canvas_height / 2 + y, canvas_width / 2 + x + 1, canvas_height / 2 + y + 1, fill="black")
        angle += 1

# Function to update the spirograph parameters
def update_parameters():
    global R, r, d
    R = int(R_entry.get())
    r = int(r_entry.get())
    d = int(d_entry.get())
    draw_spirograph(R, r, d)

# Labels and entry fields for parameters
R_label = tk.Label(root, text="R:")
R_label.pack()
R_entry = tk.Entry(root)
R_entry.pack()

r_label = tk.Label(root, text="r:")
r_label.pack()
r_entry = tk.Entry(root)
r_entry.pack()

d_label = tk.Label(root, text="d:")
d_label.pack()
d_entry = tk.Entry(root)
d_entry.pack()

update_button = tk.Button(root, text="Update", command=update_parameters)
update_button.pack()

# Initial drawing
draw_spirograph(R, r, d)

root.mainloop()
