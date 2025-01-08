import numpy as np
import matplotlib.pyplot as plt

# Simulate a single battle round (3 attacker vs 2 defender)
def battle_round():
    # Attacker and defender rolls: 3 dice for attacker, 2 for defender
    attacker_rolls = np.sort(np.random.randint(1, 7, 3))[::-1]
    defender_rolls = np.sort(np.random.randint(1, 7, 2))[::-1]
    
    # Set the variables for tracking the losses
    attacker_losses = 0
    defender_losses = 0
    
    for i in range(2):
        if attacker_rolls[i] > defender_rolls[i]:
            defender_losses += 1
        else:
            attacker_losses += 1
    
    return attacker_losses, defender_losses

# Simulate 1000 battle rounds and create an array for holding the battle round outcomes
num_rounds = 1000
attacker_losses = np.zeros(num_rounds)
defender_losses = np.zeros(num_rounds)

for i in range(num_rounds):
    attacker_losses[i], defender_losses[i] = battle_round()

# Plot the results
plt.figure(figsize=(10, 6))

# Plot losses distribution
plt.hist(attacker_losses, bins=np.arange(0, 4) - 0.5, alpha=0.5, label='Attacker Losses', color='red', edgecolor='black')
plt.hist(defender_losses, bins=np.arange(0, 3) - 0.5, alpha=0.5, label='Defender Losses', color='blue', edgecolor='black')

# Labels and title
plt.xlabel('Units Lost')
plt.ylabel('Frequency')
plt.title('Distribution of Units Lost per Battle Round (3 Attacker vs 2 Defender)')
plt.legend()

plt.show()
