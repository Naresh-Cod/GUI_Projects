import tkinter as tk
from tkinter import colorchooser
class TextArtAnimator:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Art Animator")

        self.canvas_width = 800
        self.canvas_height = 600

        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()
        self.color = "black"

        self.text = input('Enter Text: ')
        self.text_id = None
        self.x = self.canvas_width // 8
        self.y = self.canvas_height // 2

        self.animate_button = tk.Button(root, text="Animate", command=self.animate_text)
        self.animate_button.pack()

        self.color_button = tk.Button(root, text="Choose Color", command=self.choose_color)
        self.color_button.pack()

    def choose_color(self):
        self.color = colorchooser.askcolor()[1]
    def animate_text(self):
        self.canvas.delete("all")
        self.text_id = self.canvas.create_text(self.x, self.y, text=self.text, fill=self.color, font=("Helvetica", 24))
        self.move_text()

    def move_text(self):
        self.x += 5
        self.canvas.delete(self.text_id)
        self.text_id = self.canvas.create_text(self.x, self.y, text=self.text, fill=self.color, font=("Helvetica", 24))
        if self.x < self.canvas_width:
            self.root.after(100, self.move_text)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    animator = TextArtAnimator(root)
    animator.run()
