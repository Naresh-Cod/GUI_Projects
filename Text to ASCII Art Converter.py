import tkinter as tk
from art import *

def convert_text_to_ascii():
    text = input_text.get()
    ascii_art = text2art(text)
    output_text.config(text=ascii_art)

# Create the main window
root = tk.Tk()
root.title("Text to ASCII Art Converter")

# Label for user input
input_label = tk.Label(root, text="Enter your text:")
input_label.pack()

# Entry field for user input
input_text = tk.Entry(root)
input_text.pack()

# Button to convert text to ASCII art
convert_button = tk.Button(root, text="Convert to ASCII Art", command=convert_text_to_ascii)
convert_button.pack()

# Label to display ASCII art
output_text = tk.Label(root, text="", font=("Courier", 12))
output_text.pack()

# Start the tkinter main loop
root.mainloop()
