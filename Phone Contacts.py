import tkinter as tk
from tkinter import messagebox

# Function to add a contact to the list
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contact_list.insert(tk.END, f"{name}: {phone}")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter both name and phone.")

# Function to delete a selected contact
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        contact_list.delete(selected)

# Create the main window
root = tk.Tk()
root.title("Phone Contacts")
root.geometry("320x450")

# Create labels and entry fields
name_label = tk.Label(root, text="Name:", font=("Helvetica", 15))
name_label.pack()
name_entry = tk.Entry(root, font=("Helvetica", 19))
name_entry.pack()

phone_label = tk.Label(root, text="Phone:", font=("Helvetica", 15))
phone_label.pack()
phone_entry = tk.Entry(root, font=("Helvetica", 19))
phone_entry.pack()

# Create buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact, font=("Helvetica", 16))
add_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, font=("Helvetica", 16))
delete_button.pack()

# Create the contact list
contact_list = tk.Listbox(root, font=("Helvetica", 18))
contact_list.pack()

# Start the GUI application
root.mainloop()
