import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def on_canvas_click(event):
    x, y = event.x, event.y
    canvas.create_text(x, y, text='*', font=("Arial", 20))
    star_data.append((x, y))
    update_graph()

def update_graph():
    if star_data:
        x, y = zip(*star_data)
        ax.clear()
        ax.plot(x, y, 'r*')
        ax.set_xlim(0, 400)
        ax.set_ylim(0, 400)
        canvas_widget.draw()

app = tk.Tk()
app.title("Star Pattern Drawer")

canvas = tk.Canvas(app, width=400, height=400, bg='white')
canvas.pack()

canvas.bind("<Button-1>", on_canvas_click)

star_data = []

fig, ax = plt.subplots(figsize=(4, 4))
canvas_widget = FigureCanvasTkAgg(fig, master=app)
canvas_widget.get_tk_widget().pack()

app.mainloop()
