import random

"""
Monte Carlo simulation of a European roulette game.
A player bets a fixed amount of 5 € on a simple chance (red) for 200 rounds.
The simulation estimates the probability that the player ends up with
a total loss of at least 100 €.
To test reproducibility and stability, multiple simulations are performed
using different random seeds that are generated from a fixed initial seed.
"""

bet = 5
rounds = 200
simulations = 10000
p_gewinn = 18 / 37

"""Bet is the amount of money set for each round.
Rounds is the amount of rounds per simulation.
Simulations equals the total amount of simulations.
the parameters set the requirements for the simulation
"""

def monte_carlo_simulation(simulation_seed):

    random.seed(simulation_seed)
    minus_100_oder_mehr = 0

    for _ in range(simulations):
        kapital = 0

        for _ in range(rounds):
            if random.random() < p_gewinn:
                kapital += bet
            else:
                kapital -= bet

        if kapital <= -100:
            minus_100_oder_mehr += 1

    return minus_100_oder_mehr / simulations

random.seed(10)
seeds = [random.randint(1, 1000) for _ in range(10)]

print("Generated seeds:")
print(seeds)
print("\nSimulation results:\n")

for seed in seeds:
    probability = monte_carlo_simulation(seed)
    print(f"Seed {seed}: {probability:.4%}")
