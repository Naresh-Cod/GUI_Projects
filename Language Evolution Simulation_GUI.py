import tkinter as tk
import random

# Define parameters
num_agents = 20
num_iterations = 100
num_symbols = 10

# Create agents with random initial languages
agents = [{'language': [random.choice(range(num_symbols))]} for _ in range(num_agents)]

# Initialize the Tkinter application
root = tk.Tk()
root.title("Language Evolution Simulation")

# Function to update the simulation
def run_simulation():
    for iteration in range(num_iterations):
        # Communication between agents
        sender_idx = random.randint(0, num_agents - 1)
        receiver_idx = random.randint(0, num_agents - 1)

        sender = agents[sender_idx]
        receiver = agents[receiver_idx]

        # Randomly select a symbol to communicate
        symbol_to_send = random.choice(sender['language'])

        # Receiver learns or misunderstands the symbol
        if random.random() < 0.1:
            symbol_received = random.choice(range(num_symbols))
        else:
            symbol_received = symbol_to_send

        receiver['language'].append(symbol_received)

    # Display the final languages of the agents in the GUI
    result_label.config(text="Simulation completed.")
    languages_text.config(state=tk.NORMAL)
    languages_text.delete("1.0", tk.END)  # Clear previous content
    for idx, agent in enumerate(agents):
        languages_text.insert(tk.END, f"Agent {idx}: {agent['language']}\n")
    languages_text.config(state=tk.DISABLED)  # Disable editing

# Create and configure GUI elements
run_button = tk.Button(root, text="Run Simulation", command=run_simulation)
result_label = tk.Label(root, text="")
languages_text = tk.Text(root, wrap=tk.WORD, width=80, height=40)
languages_text.config(state=tk.DISABLED)  # Disable editing

# Layout GUI elements
run_button.pack(pady=20)
result_label.pack()
languages_text.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
