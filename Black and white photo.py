import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageOps


def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image = ImageOps.grayscale(image)  # Convert to grayscale
        sketch = ImageOps.invert(image)  # Invert to create sketch effect

        sketch.show()  # Display the sketch
        sketch.save("sketch.jpg")  # Save the sketch as an image file


# Create the main window
root = tk.Tk()
root.title("Photo to Sketch")

# Create and position the Open button
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
