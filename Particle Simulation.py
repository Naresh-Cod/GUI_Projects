import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set dimensions of the display
width, height = 900, 900

# Create the display surface
screen = pygame.display.set_mode((width, height))

# Define colors
white = (255, 255, 255)


# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.radius = 5
        self.color = white

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off the walls
        if self.x <= 0 or self.x >= width:
            self.vx *= -1
        if self.y <= 0 or self.y >= height:
            self.vy *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


# Create particles
num_particles = 50
particles = [Particle(random.randint(0, width), random.randint(0, height)) for _ in range(num_particles)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update and draw particles
    for particle in particles:
        particle.update()
        particle.draw()

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
