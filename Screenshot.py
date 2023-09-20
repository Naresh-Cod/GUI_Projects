import tkinter as tk
import pyautogui
from PIL import ImageGrab, ImageTk
import os

class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot Tool")

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.start_selection)
        self.canvas.bind("<B1-Motion>", self.update_selection)
        self.canvas.bind("<ButtonRelease-1>", self.take_screenshot)

        self.selection_rect = None
        self.screenshot_image = None

    def start_selection(self, event):
        self.selection_rect = (event.x, event.y, event.x, event.y)

    def update_selection(self, event):
        self.selection_rect = (self.selection_rect[0], self.selection_rect[1], event.x, event.y)
        self.canvas.delete("selection")
        self.canvas.create_rectangle(*self.selection_rect, outline="blue", width=2, tags="selection")

    def take_screenshot(self, event):
        x1, y1, x2, y2 = self.selection_rect
        if x1 < x2 and y1 < y2:
            screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            self.screenshot_image = ImageTk.PhotoImage(screenshot)

            save_path = os.path.join(os.path.expanduser("~"), "screenshot.png")
            screenshot.save(save_path)
            print(f"Screenshot saved to: {save_path}")

            self.canvas.create_image(x1, y1, image=self.screenshot_image, anchor=tk.NW)
            self.canvas.image = self.screenshot_image

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()
