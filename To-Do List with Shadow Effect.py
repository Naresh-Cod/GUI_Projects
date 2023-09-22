import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

root = tk.Tk()
root.title("To-Do List with Shadow")
root.geometry("800x800")
root.configure(bg="black")

task_frame = tk.Frame(root, bg="black")
task_frame.pack(pady=20)

task_label = tk.Label(task_frame, text="Enter Task:", font=("Helvetica", 16), bg="black", fg="white")
task_label.grid(row=0, column=0)

task_entry = tk.Entry(task_frame, font=("Helvetica", 16))
task_entry.grid(row=0, column=1)

add_button = tk.Button(task_frame, text="Add Task", font=("Helvetica", 16), bg="black", fg="white", command=add_task)
add_button.grid(row=0, column=2)

remove_button = tk.Button(task_frame, text="Remove Task", font=("Helvetica", 16), bg="black", fg="white", command=remove_task)
remove_button.grid(row=0, column=3)

task_listbox = tk.Listbox(root, font=("Helvetica", 14), selectbackground="black", selectforeground="white")
task_listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
