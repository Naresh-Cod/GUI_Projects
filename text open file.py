import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, file_contents)

def save_file():
    file_contents = text_widget.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(file_contents)

def zoom_in():
    current_font = text_widget.tag_cget("zoom", "font")
    new_size = int(current_font.split(" ")[-1]) + 2
    text_widget.tag_configure("zoom", font=("Arial", new_size))
    text_widget.tag_add("zoom", "1.0", "end")

def zoom_out():
    current_font = text_widget.tag_cget("zoom", "font")
    new_size = max(6, int(current_font.split(" ")[-1]) - 2)
    text_widget.tag_configure("zoom", font=("Arial", new_size))
    text_widget.tag_add("zoom", "1.0", "end")

window = tk.Tk()
window.title("Text File Viewer")

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

text_widget = tk.Text(window, height=40, width=70)
text_widget.pack()

# Define the "zoom" tag initially with a default font size
text_widget.tag_configure("zoom", font=("Arial", 12))

zoom_in_button = tk.Button(window, text="Zoom In", command=zoom_in)
zoom_in_button.pack()
zoom_out_button = tk.Button(window, text="Zoom Out", command=zoom_out)
zoom_out_button.pack()

window.mainloop()
