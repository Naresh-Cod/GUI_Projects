import tkinter as tk
import time

# Create a Tkinter window
window = tk.Tk()
window.title("Animated Digital Watch")

# Function to update the time
def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    window.after(1000, update_time)  # Update time every second (1000 milliseconds)

# Create a label to display the time
label = tk.Label(window, text="", font=("Courier", 24), fg="green")
label.pack(pady=20)

# Start updating the time
update_time()

# Close the window when clicked
window.mainloop()
