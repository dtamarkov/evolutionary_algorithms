"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

# Set real division
from __future__ import division

import evolutionary.initializations as initialization
import evolutionary.mutations as mutation
import evolutionary.replacements as replacement
import evolutionary.selections as selection
import numpy as np

import evolutionary.crossovers as crossover
import evolutionary.optim_functions as functions
from evolutionary import Logger
from evolutionary import Population

# Log results var
logger = Logger({'mean', 'best', 'worst'})

# Set a random generator seed to reproduce the same experiments
np.random.seed(82634)

# Set the problem characteristics
minimization = False

# Define the problem to solve and get its fitness function
problem = functions.Ackley(minimize=minimization)
fitness_function = problem.evaluate

# Initalize vars
n_dimensions = 10 if not problem.dim else problem.dim
n_population = 100
n_iterations = 1000
n_children = n_population
xover_prob = 0.8
mutat_prob = 0.1
iter_log = 50

logger.print_description(problem.name, n_dimensions, n_population, n_iterations, xover_prob, mutat_prob)

# Define the bounds to explore the problem
upper = np.ones((n_population, n_dimensions)) * problem.upper
lower = np.ones((n_population, n_dimensions)) * problem.lower

# Create the class Population and initialize its chromosomes
population = Population(chromosomes=initialization.uniform(n_population, lower, upper, n_dimensions))

# Iterate simulating the evolutionary process
for i in range(n_iterations):
    # Apply the function in each row to get the array of fitness
    fitness = fitness_function(population.chromosomes)

    # Log the values
    logger.log({'mean': np.mean(fitness),
                'worst': np.max(fitness) if minimization else np.min(fitness),
                'best': np.min(fitness) if minimization else  np.max(fitness)})

    # Print the iteration result
    if (i + 1) % iter_log == 0:
        logger.print_log(i)

    # Select a subgroup of parents
    parents, idx = selection.wheel(population.chromosomes, fitness, M=n_children, minimize=minimization)
    # iterations=1, N=n_population,)

    # Use recombination to generate new children
    children = crossover.blend(parents, xover_prob, upper[idx], lower[idx])

    # Mutate the generated children
    children = mutation.non_uniform(children, mutat_prob, upper[idx], lower[idx]
                                    , i, n_iterations)

    # Replace the current chromosomes of parents and childrens to
    # create the new chromosomes
    population.chromosomes = replacement.elitist(population.chromosomes, fitness,
                                                 children, fitness_function(children),
                                                 n_population, minimize=minimization)

# Print the best chromosome
print(population.chromosomes[np.argmin(fitness)] if minimization else population.chromosomes[np.argmax(fitness)])
# Plot the graph with all the results
logger.plot()
