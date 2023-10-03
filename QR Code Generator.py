import tkinter as tk
import qrcode
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter
from tkinter import filedialog

# Function to generate QR code
def generate_qr_code():
    data = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("qrcode.png")

    # Display the QR code image in the GUI
    display_qr_code()

def save_qr_code():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        qr_code_image.save(file_path)

def display_qr_code():
    global qr_code_image
    # Display the QR code image in the GUI
    qr_code_image = Image.open("qrcode.png")
    qr_code_image.thumbnail((200, 200))
    qr_code_photo = ImageTk.PhotoImage(qr_code_image)
    qr_code_label.config(image=qr_code_photo)
    qr_code_label.image = qr_code_photo

# Create the main window
window = tk.Tk()
window.title("QR Code Generator")

# Create and configure the entry widget
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Create and configure the "Generate" button
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Create and configure the "Save QR Code" button
save_button = tk.Button(window, text="Save QR Code", command=save_qr_code)
save_button.pack()

# Create and configure the QR code image label
qr_code_label = tk.Label(window)
qr_code_label.pack()

# Start the GUI main loop
window.mainloop()
