import tkinter as tk
import psutil

def get_running_processes(search_term=""):
    running_processes = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        process_info = process.info
        if search_term.lower() in process_info['name'].lower():
            running_processes.append((process_info['pid'], process_info['name']))
    return running_processes

def update_process_list():
    search_text = search_entry.get()  # Get the search term from the entry widget
    process_list.delete(0, tk.END)
    processes = get_running_processes(search_text)
    for pid, name in processes:
        process_list.insert(tk.END, f"{pid}: {name}")

# Create the main application window
root = tk.Tk()
root.title("Running Processes")
root.geometry("500x500")

# Create an entry widget for searching
search_entry = tk.Entry(root, font=("Helvetica", 16))
search_entry.pack()

# Create a listbox to display the running processes
process_list = tk.Listbox(root, height=15, width=85, font=("Helvetica", 16))
process_list.pack()

# Create a button to refresh the process list
refresh_button = tk.Button(root, text="Refresh", command=update_process_list)
refresh_button.pack()

# Create a button to perform the search
search_button = tk.Button(root, text="Search", command=update_process_list)
search_button.pack()

# Update the process list initially
update_process_list()

root.mainloop()
