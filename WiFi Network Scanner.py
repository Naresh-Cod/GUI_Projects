import tkinter as tk
from tkinter import ttk
import subprocess

def scan_wifi():
    try:
        wifi_scan_result.delete('1.0', 'end')  # Clear the previous results
        result = subprocess.check_output(['iwlist', 'wlan0', 'scan'])
        print(result)
        wifi_scan_result.insert('end', result.decode('utf-8'))
    except Exception as e:
        wifi_scan_result.insert('end', f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("WiFi Network Scanner")

# Create a label
label = ttk.Label(root, text="Available WiFi Networks:")
label.pack(pady=10)

# Create a text widget to display the scan results
wifi_scan_result = tk.Text(root, wrap=tk.WORD, width=90, height=40)
wifi_scan_result.pack()

# Create a button to initiate the scan
scan_button = ttk.Button(root, text="Scan WiFi Networks", command=scan_wifi)
scan_button.pack(pady=10)

# Start the main loop
root.mainloop()
