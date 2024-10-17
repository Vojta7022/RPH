import random

def monty_hall(strategy="switch"):
    # Define the doors
    doors = (1, 2, 3)

    # Randomly choose the door hiding the car
    car = random.choice(doors)

    # Randomly choose the door the contestant selects
    choice = random.choice(doors)

    # Randomly choose the door Monty opens
    options_to_reveal = [d for d in doors if d != car and d != choice]
    reveal = random.choice(options_to_reveal)

    # Player can switch or stay
    if strategy == "switch":
        choice = next(d for d in doors if d != choice and d != reveal)

    # Did the player win?
    return choice == car

# Simulate the game n times
n = 10000
wins = sum(monty_hall() for _ in range(n))
print(f"Strategy: switch, wins: {wins/n:.4f}")
