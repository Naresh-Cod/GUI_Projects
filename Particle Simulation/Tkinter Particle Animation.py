import tkinter as tk
import random

class Particle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.radius = 2
        self.x = random.randint(self.radius, canvas.winfo_width() - self.radius)
        self.y = random.randint(self.radius, canvas.winfo_height() - self.radius)
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)
        self.color = "#FF0000"  # Red

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.canvas.move(self.id, self.dx, self.dy)

class ParticleSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Particle Simulation")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.particles = []
        self.num_particles = 100

        self.start_button = tk.Button(root, text="Start", command=self.start_simulation)
        self.start_button.pack()

    def create_particles(self):
        for _ in range(self.num_particles):
            particle = Particle(self.canvas)
            particle.id = self.canvas.create_oval(
                particle.x - particle.radius,
                particle.y - particle.radius,
                particle.x + particle.radius,
                particle.y + particle.radius,
                fill=particle.color,
            )
            self.particles.append(particle)

    def move_particles(self):
        for particle in self.particles:
            particle.move()

    def start_simulation(self):
        self.create_particles()
        self.root.after(10, self.update_simulation)

    def update_simulation(self):
        self.move_particles()
        self.root.update()
        self.root.after(10, self.update_simulation)

if __name__ == "__main__":
    root = tk.Tk()
    app = ParticleSimulation(root)
    root.mainloop()
