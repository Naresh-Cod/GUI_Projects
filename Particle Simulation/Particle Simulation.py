import tkinter as tk
import math
import random

# Constants
WIDTH, HEIGHT = 900, 900
PARTICLE_RADIUS = 5
TIME_STEP = 0.01

# Particle Simulation Particle Simulation
charge_prey = -1.0  # Charge of the prey (e.g., electron)
charge_predator = 1.0  # Charge of the predator
mass = 1.0  # Mass of particles
initial_velocity = 10.0  # Initial velocity of particles
magnetic_field_strength = 0.1  # Reduced strength of the magnetic field
magnetic_field_angle = math.pi / 4  # Direction of the magnetic field (45 degrees)

# Initialize tkinter
root = tk.Tk()
root.title("Magnetic Field Simulator")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Create multiple blue particles (prey)
num_prey = 50
prey_particles = []

for _ in range(num_prey):
    prey_x = random.uniform(0, WIDTH)
    prey_y = random.uniform(0, HEIGHT)
    prey_vx = initial_velocity
    prey_vy = 0.0
    prey_particles.append([prey_x, prey_y, prey_vx, prey_vy, "blue"])

num_predators = 50
predators = []

for _ in range(num_predators):
    predator_x = random.uniform(0, WIDTH)
    predator_y = random.uniform(0, HEIGHT)
    predator_vx = initial_velocity
    predator_vy = 0.0
    predators.append([predator_x, predator_y, predator_vx, predator_vy, "red"])


def update_particles():
    for i in range(num_prey):
        prey_x, prey_y, prey_vx, prey_vy, prey_color = prey_particles[i]

        # Wrap particles around the screen
        if prey_x < 0:
            prey_x = WIDTH
        if prey_x > WIDTH:
            prey_x = 0
        if prey_y < 0:
            prey_y = HEIGHT
        if prey_y > HEIGHT:
            prey_y = 0

        # Calculate the Lorentz force for prey
        magnetic_force_prey = charge_prey * (prey_vx * math.sin(magnetic_field_angle) -
                                             prey_vy * math.cos(magnetic_field_angle)) * magnetic_field_strength
        acceleration_prey = magnetic_force_prey / mass

        # Update prey velocity using F = ma
        prey_particles[i][2] += acceleration_prey * math.sin(magnetic_field_angle) * TIME_STEP
        prey_particles[i][3] += acceleration_prey * math.cos(magnetic_field_angle) * TIME_STEP

        # Update prey position using the new velocity
        prey_particles[i][0] += prey_particles[i][2] * TIME_STEP
        prey_particles[i][1] += prey_particles[i][3] * TIME_STEP

    for i in range(num_predators):
        predator_x, predator_y, predator_vx, predator_vy, predator_color = predators[i]

        # Calculate the Lorentz force for predators
        magnetic_force_predator = charge_predator * (predator_vx * math.sin(magnetic_field_angle) -
                                                     predator_vy * math.cos(
                    magnetic_field_angle)) * magnetic_field_strength
        acceleration_predator = magnetic_force_predator / mass

        # Update predator velocity using F = ma
        predators[i][2] += acceleration_predator * math.sin(magnetic_field_angle) * TIME_STEP
        predators[i][3] += acceleration_predator * math.cos(magnetic_field_angle) * TIME_STEP

        # Update predator position using the new velocity
        predators[i][0] += predators[i][2] * TIME_STEP
        predators[i][1] += predators[i][3] * TIME_STEP

    # Check for collisions between predators and prey
    for prey in prey_particles:
        for predator in predators:
            dist = math.sqrt((prey[0] - predator[0]) ** 2 + (prey[1] - predator[1]) ** 2)
            if dist < 2 * PARTICLE_RADIUS:
                # Predator touched prey, change predator color to yellow
                predator[4] = "yellow"

    # Draw the particles on the canvas
    canvas.delete("particle")
    for prey in prey_particles:
        canvas.create_oval(
            prey[0] - PARTICLE_RADIUS, prey[1] - PARTICLE_RADIUS,
            prey[0] + PARTICLE_RADIUS, prey[1] + PARTICLE_RADIUS,
            fill=prey[4], tags="particle"
        )

    for predator in predators:
        canvas.create_oval(
            predator[0] - PARTICLE_RADIUS, predator[1] - PARTICLE_RADIUS,
            predator[0] + PARTICLE_RADIUS, predator[1] + PARTICLE_RADIUS,
            fill=predator[4], tags="particle"
        )

    # Schedule the next update
    root.after(int(TIME_STEP * 1000), update_particles)


# Start the simulation
update_particles()

root.mainloop()
