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

"""
Bet is the amount of money set for each round.
Rounds is the amount of rounds per simulation.
Simulations equals the total amount of simulations.
p_gewinn is the winning propability 
the parameters set the requirements for the simulation
"""

def monte_carlo_simulation(simulation_seed):

    random.seed(simulation_seed)
    minus_100 = 0

    for _ in range(simulations):
        kapital = 0

        for _ in range(rounds):
            if random.random() < p_gewinn:
                kapital += bet
            else:
                kapital -= bet

        if kapital <= -100:
            minus_100 += 1

    return minus_100 / simulations
"""
Initializes the random number generator with the provided seed to ensure reproducibility.
Repeats the roulette simulation for a predefined number of seeds (simulations).
return gives the estimated probability that the player loses  at least 100 € 
after 200 rounds in the Monte-Carlo simulation.
The roulette simulation starts by opening a loop for the number of simulations of the first seed 
setting the capital to 0. 
it continues by opening another loop for the 200 rounds which using the propability (p_gewinn) 
is adding 5€ or subtracting 5€ 
After the 200 rounds if the capital is smaller or equals -100€ 1 is added to minus_100 and the second simulation
starts. After all the simulations minus_100 is divided by the total number of simulations returning the 
propability for the first seed. As the last step the first loop starts again with the second seed.
this continues until all 10 seeds have a propability
"""
random.seed(10)
seeds = [random.randint(1, 1000) for _ in range(10)]
"""
creates 10 random seeds between 1 and 1000  
"""
print("Generated seeds:")
print(seeds)
print("\nSimulation results:\n")
"""
first prints generated seeds, then all seeds which were generated in a row and last it prints simulation results.
"""
for s in seeds:
    probability = monte_carlo_simulation(s)
    print(f"Seed {s}: {probability:.4%}")
"""
prints the first the generated seed and then the propability to lose 100€ for this seed
"""


