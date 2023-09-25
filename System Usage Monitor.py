import tkinter as tk
import psutil


# Function to update CPU and memory usage
def update_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()

    cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
    memory_label.config(text=f"Memory Usage: {memory_info.percent}%")

    root.after(1000, update_usage)  # Schedule the next update after 1 second


# Create the main window
root = tk.Tk()
root.title("System Usage Monitor")

# Create a label to display CPU usage
cpu_label = tk.Label(root, text="CPU Usage: N/A", font=("Helvetica", 52))
cpu_label.pack()

# Create a label to display memory usage
memory_label = tk.Label(root, text="Memory Usage: N/A", font=("Helvetica", 52))
memory_label.pack()

# Start the CPU and memory usage update loop
update_usage()

# Start the tkinter main loop
root.mainloop()
