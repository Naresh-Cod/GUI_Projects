import tkinter as tk
import webbrowser

# Function to open the website
def open_website():
    url = entry.get()
    webbrowser.open(url)

# Create the main application window
app = tk.Tk()
app.title("Website Opener")
font = ("Helvetica", 22)

# Create a label widget
label = tk.Label(app, text="Enter URL:", font=font)
label.pack(pady=10)

# Create an entry widget to input the URL
entry = tk.Entry(app, width=40, font=font)
entry.pack()

# Create a button to open the website
button = tk.Button(app, text="Open Website", command=open_website, font=("Helvetica", 12))
button.pack(pady=10)

# Start the main loop
app.mainloop()
