import random

# Define parameters
num_agents = 20
num_iterations = 100
num_symbols = 10

# Create agents with random initial languages
agents = [{'language': [random.choice(range(num_symbols))]} for _ in range(num_agents)]

# Simulate language evolution
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

# Print the final languages of the agents
for idx, agent in enumerate(agents):
    print(f"Agent {idx}: {agent['language']}")
