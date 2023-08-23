import tkinter as tk
from tkinter import colorchooser

class PixelArtEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art Editor")

        self.canvas_width = 400
        self.canvas_height = 400
        self.pixel_size = 10
        self.pixels = {}

        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.color = "black"

        self.color_button = tk.Button(root, text="Choose Color", command=self.choose_color)
        self.color_button.pack()

        self.clear_button = tk.Button(root, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack()

        self.canvas.bind("<Button-1>", self.draw_pixel)

    def choose_color(self):
        self.color = colorchooser.askcolor()[1]

    def clear_canvas(self):
        self.canvas.delete("all")
        self.pixels = {}

    def draw_pixel(self, event):
        x = event.x // self.pixel_size * self.pixel_size
        y = event.y // self.pixel_size * self.pixel_size

        if (x, y) not in self.pixels:
            pixel = self.canvas.create_rectangle(x, y, x + self.pixel_size, y + self.pixel_size, fill=self.color, outline="")
            self.pixels[(x, y)] = pixel

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    editor = PixelArtEditor(root)
    editor.run()
