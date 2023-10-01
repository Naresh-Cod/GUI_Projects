import pyudev
import tkinter as tk

# Function to display a message when a USB drive is inserted
def display_message(device):
    message = f"USB Drive Detected: {device.get('ID_FS_LABEL')} ({device.get('ID_FS_TYPE')})"
    message_label.config(text=message)
    root.after(5000, clear_message)  # Remove message after 5000 milliseconds (5 seconds)

# Function to clear the message
def clear_message():
    message_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("USB Drive Monitor")
root.geometry("400x300")

# Create a label to display messages
message_label = tk.Label(root, text="")
message_label.pack(pady=20)

# Create a UDev Monitor
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='block', device_type='disk')

# Start monitoring for USB drive insertion
observer = pyudev.MonitorObserver(monitor, callback=display_message)
observer.start()

# Run the main GUI loop
root.mainloop()
