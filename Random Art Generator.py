import tkinter as tk
import random

class RandomArtGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Art Generator")

        self.canvas_width = 800
        self.canvas_height = 600

        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.shapes = ["rectangle", "oval", "line"]
        self.colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink"]

        self.generate_button = tk.Button(root, text="Generate Art", command=self.generate_random_art)
        self.generate_button.pack()

    def generate_random_art(self):
        self.canvas.delete("all")

        num_shapes = random.randint(10, 50)

        for _ in range(num_shapes):
            shape = random.choice(self.shapes)
            color = random.choice(self.colors)
            x1 = random.randint(0, self.canvas_width)
            y1 = random.randint(0, self.canvas_height)
            x2 = random.randint(0, self.canvas_width)
            y2 = random.randint(0, self.canvas_height)

            if shape == "rectangle":
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
            elif shape == "oval":
                self.canvas.create_oval(x1, y1, x2, y2, fill=color)
            elif shape == "line":
                self.canvas.create_line(x1, y1, x2, y2, fill=color, width=random.randint(1, 5))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    generator = RandomArtGenerator(root)
    generator.run()
