import matplotlib.pyplot as plt
import numpy as np

# Simulation parameters
num_rays = 1000
num_droplets = 500
width, height = 1000, 800
colors = [(148, 0, 211), (75, 0, 130), (0, 0, 255), (0, 255, 0), (255, 255, 0), (255, 127, 0), (255, 0, 0)]

# Initialize the canvas
canvas = np.zeros((height, width, 3), dtype=np.uint8)


# Define a function to calculate the rainbow color based on deviation angle
def rainbow_color(angle):
    wavelength = 400 + angle * 2.5
    r, g, b = 0, 0, 0

    if 400 <= wavelength <= 499:
        r = (-(wavelength - 499) / 100)
        g = 0.0
        b = 1.0
    elif 500 <= wavelength <= 579:
        r = 0.0
        g = ((wavelength - 500) / 80)
        b = 1.0
    elif 580 <= wavelength <= 644:
        r = 1.0
        g = 1.0
        b = (-(wavelength - 645) / 65)

    return [int(255 * r), int(255 * g), int(255 * b)]


# Simulate rainbow formation
for _ in range(num_rays):
    x, y = np.random.randint(0, width), np.random.randint(0, int(height / 2))
    angle = np.random.uniform(0, 180)
    color = rainbow_color(angle)

    for _ in range(num_droplets):
        deviation = np.random.uniform(-5, 5)  # Simulate raindrop deviation
        droplet_x = int(x + deviation)
        droplet_y = int(y + np.random.uniform(0, height / 2))

        if 0 <= droplet_x < width and 0 <= droplet_y < height:
            canvas[droplet_y, droplet_x] = color

# Display the rainbow
plt.imshow(canvas)
plt.axis('off')
plt.show()
