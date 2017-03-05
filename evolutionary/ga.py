"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: March - 2017
"""

# Set real division
from __future__ import division

import numpy as np
import evolutionary.crossovers as crossovers
import evolutionary.initializations as initializations
import evolutionary.mutations as mutations
import evolutionary.replacements as replacements
import evolutionary.selections as selections
import optim_functions as functions
from evolutionary import Logger
from evolutionary import Population


class GA(object):
    """

    """

    def __init__(self,
                 n_dimensions=10,
                 n_population=100,
                 n_iterations=1000,
                 n_children=100,
                 xover_prob=0.8,
                 mutat_prob=0.1,
                 minimization=False,
                 seed=12345,
                 logger=Logger({'mean', 'best', 'worst'}),
                 initialization=initializations.uniform,
                 problem=functions.Ackley,
                 selection='wheel',
                 crossover='blend',
                 mutation='non_uniform',
                 replacement='elitist'):
        """

        :param n_dimensions:
        :param n_population:
        :param n_iterations:
        :param n_children:
        :param xover_prob:
        :param mutat_prob:
        :param minimization:
        :param seed:
        :param logger:
        :param initialization:
        :param problem:
        :param selection:
        :param crossover:
        :param mutation:
        :param replacement:
        """

        self.n_dimensions = n_dimensions
        self.n_population = n_population
        self.n_iterations = n_iterations
        self.n_children = n_children
        self.xover_prob = xover_prob
        self.mutat_prob = mutat_prob
        self.minimization = minimization
        self.seed = seed
        self.logger = logger
        self.initialization = initialization
        self.problem = problem
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.replacement = replacement

    def run(self, iter_log=50):
        """

        :param iter_log:
        :return:
        """

        # Set a random generator seed to reproduce the same experiments
        np.random.seed(self.seed)


        # Define the problem to solve and get its fitness function
        problem = self.problem(minimize=self.minimization)
        fitness_function = problem.evaluate

        # Set the dimensions of the problem
        if problem.dim and self.n_dimensions > problem.dim:
            import warnings
            warnings.warn("Changing the number of dimensions of the problem from "
                          + str(self.n_dimensions) + " to " + str(problem.dim))
        self.n_dimensions = self.n_dimensions if not problem.dim else problem.dim

        # Print a description of the problem
        self.logger.print_description(problem.name, self.n_dimensions,
                                      self.n_population, self.n_iterations,
                                      self.xover_prob, self.mutat_prob)

        # Define the bounds to explore the problem
        upper = np.ones((self.n_population, self.n_dimensions)) * problem.upper
        lower = np.ones((self.n_population, self.n_dimensions)) * problem.lower

        # Create the class Population and initialize its chromosomes
        population = Population(
            chromosomes=self.initialization(self.n_population, lower,
                                            upper, self.n_dimensions))

        # Iterate simulating the evolutionary process
        for i in range(self.n_iterations):
            # Apply the function in each row to get the array of fitness
            fitness = fitness_function(population.chromosomes)

            # Log the values
            self.logger.log({'mean': np.mean(fitness),
                             'worst': np.max(fitness) if self.minimization else np.min(fitness),
                             'best': np.min(fitness) if self.minimization else  np.max(fitness)})

            # Print the iteration result
            if iter_log and (i + 1) % iter_log == 0:
                self.logger.print_log(i)

            # Select a subgroup of parents
            if self.selection == 'wheel':
                parents, idx = selections.wheel(population.chromosomes, fitness,
                                                M=self.n_children, minimize=self.minimization)
            # iterations=1, N=n_population,)

            # Use recombination to generate new children
            if self.crossover == 'blend':
                children = crossovers.blend(parents, self.xover_prob, upper[idx], lower[idx])

            # Mutate the generated children
            if self.mutation == 'non_uniform':
                children = mutations.non_uniform(children, self.mutat_prob, upper[idx], lower[idx],
                                                 i, self.n_iterations)
            elif self.mutation == 'uniform':
                children = mutations.uniform(children, self.mutat_prob, upper[idx], lower[idx])

            # Replace the current chromosomes of parents and childrens to
            # create the new chromosomes
            if self.replacement == 'elitist':
                population.chromosomes = replacements.elitist(population.chromosomes, fitness,
                                                              children, fitness_function(children),
                                                              self.n_population, minimize=self.minimization)
        # Print the best chromosome
        print "Best individual:", (population.chromosomes[np.argmin(fitness)]
              if self.minimization else population.chromosomes[np.argmax(fitness)])

        # Plot the graph with all the results
        self.logger.plot()
