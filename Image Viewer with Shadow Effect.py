import tkinter as tk
from PIL import Image, ImageTk
import os


class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer with Shadow")

        # Set the fixed size for the image frame
        self.image_frame_width = 800
        self.image_frame_height = 600

        self.image_list = []
        self.current_image_index = 0

        self.create_widgets()

    def create_widgets(self):
        self.image_frame = tk.LabelFrame(self.root, text="Image", bd=5, relief=tk.SUNKEN, width=self.image_frame_width,
                                         height=self.image_frame_height)
        self.image_frame.pack(padx=10, pady=10)

        self.image_label = tk.Label(self.image_frame, width=self.image_frame_width, height=self.image_frame_height)
        self.image_label.pack()

        self.navigation_frame = tk.Frame(self.root)
        self.navigation_frame.pack(pady=10)

        self.prev_button = tk.Button(self.navigation_frame, text="Previous", command=self.show_previous_image)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(self.navigation_frame, text="Next", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT)

        self.load_images()
        self.show_image()

    def load_images(self):
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        current_directory = os.getcwd()

        for filename in os.listdir(current_directory):
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                self.image_list.append(filename)

    def show_image(self):
        if self.image_list:
            image_path = self.image_list[self.current_image_index]
            image = Image.open(image_path)
            image.thumbnail((self.image_frame_width, self.image_frame_height))  # Resize the image to fit the frame
            photo = ImageTk.PhotoImage(image)

            self.image_label.configure(image=photo)
            self.image_label.image = photo

    def show_previous_image(self):
        if self.image_list:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_list)
            self.show_image()

    def show_next_image(self):
        if self.image_list:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_list)
            self.show_image()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
