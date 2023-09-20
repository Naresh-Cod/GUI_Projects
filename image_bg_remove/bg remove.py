import requests

# Your Remove.bg API key
api_key = 'Nhohm68nki6DiShydUaVEaP6'

# Input image file path
input_image_path = 'channels4_profile.jpg'  # Replace with your input image path

# URL for the Remove.bg API
api_url = 'https://api.remove.bg/v1.0/removebg'

# Send a POST request to the API to remove the background
response = requests.post(api_url, headers={'X-Api-Key': api_key}, files={'image_file': open(input_image_path, 'rb')})

# Check if the request was successful
if response.status_code == 200:
    # Save the output image with a transparent background
    with open('output_image.png', 'wb') as output_image:
        output_image.write(response.content)
    print('Background removed and saved as output_image.png')
else:
    print(f'Error: {response.status_code}')
    print(response.text)
