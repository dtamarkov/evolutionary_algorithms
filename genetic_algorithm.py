from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import evolutionary.genetic_algorithms.initializations as initialization
import evolutionary.genetic_algorithms.selections as selection
import evolutionary.genetic_algorithms.mutations as mutation
import evolutionary.genetic_algorithms.crossovers as crossover
import evolutionary.genetic_algorithms.replacements as replacement
import evolutionary.optim_functions as functions
from evolutionary import Population

np.random.seed(82634)

minimization = False

# Define the problem to solve and get its fitness function
problem = functions.Ackley(minimize=minimization)
fitness_function = problem.evaluate

# Initalize vars
n_dimensions = 10
n_population = 100
n_iterations = 1000
xover_prob = 0.8
mutat_prob = 1

# Define the bounds to explore the problem
upper = np.ones((n_population, n_dimensions)) * problem.upper
lower = np.ones((n_population, n_dimensions)) * problem.lower

# Log results var
mean = np.array([])
median = np.array([])
worst = np.array([])
best = np.array([])
best_individual = np.array([])

# Create the class Population and initialize its chromosomes
population = Population(chromosomes=initialization.uniform(n_population, lower, upper, n_dimensions))

# Iterate simulating the evolutionary process
for i in range(n_iterations):
    # Apply the function in each row to get the array of fitness
    fitness = fitness_function(population.chromosomes)

    # Log the values
    mean = np.append(mean, np.mean(fitness))
    median = np.append(median, np.median(fitness))
    if minimization:
        worst = np.append(worst, np.max(fitness))
        best = np.append(best, np.min(fitness))
    else:
        worst = np.append(worst, np.min(fitness))
        best = np.append(best, np.max(fitness))

    # Update the best chromosome
    if i > 0 and best[i - 1] > best[i]:
        if minimization:
            best_individual = population.chromosomes[np.argmin(fitness)]
        else:
            best_individual = population.chromosomes[np.argmax(fitness)]

    # Print the iteration result
    if (i + 1) % 50 == 0:
        print("Iteration", i + 1, "Best", best[i],
              "Mean", mean[i], "Worst", worst[i])

    # Select a subgroup of parents
    parents, idx = selection.wheel(population.chromosomes, fitness, M=50, minimize=minimization)
                                    #iterations=1, N=n_population,)

    # Use recombination to generate new children
    children = crossover.blend(parents, xover_prob, upper[idx], lower[idx])

    # Mutate the generated children
    children = mutation.uniform(children, mutat_prob, upper[idx], lower[idx])
                                #,i, n_iterations)

    # Replace the current chromosomes of parents and childrens to
    # create the new chromosomes
    population.chromosomes = replacement.elitist(population.chromosomes, fitness,
                                                 children, fitness_function(children),
                                                 n_population, minimize=minimization)

print(best_individual)

if i > 0:
    x = np.arange(0, n_iterations, 20)
    plt.plot(x, np.abs(mean[::20]))
    #     plt.plot(x, median[::10])
    plt.plot(x, np.abs(worst[::20]), 'o')
    plt.plot(x, np.abs(best[::20]))
    plt.legend(['Mean', 'Worst value', 'Best value'], loc='upper right')

    plt.show()
