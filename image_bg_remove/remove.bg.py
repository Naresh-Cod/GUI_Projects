import tkinter as tk
from tkinter import filedialog
import requests
from PIL import Image, ImageTk

# Your Remove.bg API key
api_key = 'Nhohm68nki6' \
          'DiShydUaVEaP6'


# Function to remove the background using the Remove.bg API
def remove_background():
    # Open a file dialog to select an input image
    file_path = filedialog.askopenfilename()

    if not file_path:
        return

    # Create a URL for the Remove.bg API
    api_url = 'https://api.remove.bg/v1.0/removebg'

    # Send a POST request to the API to remove the background
    response = requests.post(api_url, headers={'X-Api-Key': api_key}, files={'image_file': open(file_path, 'rb')})

    if response.status_code == 200:
        # Save the output image with a transparent background
        with open('output_image.png', 'wb') as output_image:
            output_image.write(response.content)
        result_label.config(text='Background removed and saved as output_image.png')

        # Display the output image in the GUI
        #img = Image.open('output_image.png').resize((600, 600), Image.ANTIALIAS)
        img = Image.open('output_image.png')
        img.thumbnail((600, 600), Image.BILINEAR)

        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img
    else:
        result_label.config(text=f'Error: {response.status_code}')
        print(response.text)


# Create a Tkinter window
window = tk.Tk()
window.title('Background Remover')

# Create a button to trigger background removal
remove_button = tk.Button(window, text='Remove Background', command=remove_background)
remove_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text='')
result_label.pack()

# Create a label to display the output image
image_label = tk.Label(window)
image_label.pack()

# Start the Tkinter main loop
window.mainloop()
