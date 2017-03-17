"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: March - 2017
"""

import warnings
import numpy as np
import evolutionary.crossovers as crossovers
import evolutionary.initializations as initializations
import evolutionary.mutations as mutations
import evolutionary.replacements as replacements
import evolutionary.selections as selections
import evolutionary.optim_functions as functions
from evolutionary import Logger
from evolutionary import Population


class EAL(object):
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
                 initialization='uniform',
                 problem=functions.Ackley,
                 selection='wheel',
                 crossover='blend',
                 mutation='non_uniform',
                 replacement='elitist',
                 tournament_competitors=3,
                 tournament_winners=1,
                 replacement_elitism=0.5,
                 ):
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
        self.initialization = initialization
        self.problem = problem
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.replacement = replacement
        self.tournament_competitors = tournament_competitors
        self.tournament_winners = tournament_winners
        self.replacement_elitism = replacement_elitism

    def fit(self, type="ga", iter_log=50):
        """

        :param iter_log:
        :return:
        """

        # Set a random generator seed to reproduce the same experiments
        np.random.seed(self.seed)

        logger = Logger()

        # Define the problem to solve and get its fitness function
        problem = self.problem(minimize=self.minimization)
        fitness_function = problem.evaluate

        # Set the dimensions of the problem
        if problem.dim and self.n_dimensions > problem.dim:
            warnings.warn("Changing the number of dimensions of the problem from "
                          + str(self.n_dimensions) + " to " + str(problem.dim))
        self.n_dimensions = self.n_dimensions if not problem.dim else problem.dim

        # Print a description of the problem
        logger.print_description(problem.name, self.n_dimensions,
                                      self.n_population, self.n_iterations,
                                      self.xover_prob, self.mutat_prob)

        # Define the bounds to explore the problem
        upper = np.ones((self.n_population, self.n_dimensions)) * problem.upper
        lower = np.ones((self.n_population, self.n_dimensions)) * problem.lower

        try:
            # Create the class Population and initialize its chromosomes
            if type == "ga":
                if self.initialization == 'uniform':
                    population = Population(
                        chromosomes=initializations.uniform(self.n_population, lower,
                                                            upper, self.n_dimensions))
                elif self.initialization == 'permutation':
                    population = Population(
                        chromosomes=initializations.permutation(self.n_population, self.n_dimensions))
                else:
                    raise ValueError("The specified initialization doesn't match. Stopping the algorithm")
            elif type == "es":
                if self.initialization == 'uniform':
                    population = Population(
                        chromosomes=initializations.uniform(self.n_population, lower,
                                                            upper, self.n_dimensions),
                        sigma=np.random.uniform() * (np.mean(upper) - np.mean(lower)) / 10)
                elif self.initialization == 'permutation':
                    raise ValueError("The permutation initialization is not allowed yet with an evolutionary strategy")
                else:
                    raise ValueError("The specified initialization doesn't match. Stopping the algorithm")

            # Iterate simulating the evolutionary process
            for i in range(self.n_iterations):
                # Apply the function in each row to get the array of fitness
                fitness = fitness_function(population.chromosomes)

                # Log the values
                logger.log({'mean': np.mean(fitness),
                                 'worst': np.max(fitness) if self.minimization else np.min(fitness),
                                 'best': np.min(fitness) if self.minimization else  np.max(fitness),
                                 'best_chromosome': population.chromosomes[np.argmin(fitness)] if self.minimization else  population.chromosomes[np.argmax(fitness)]})


                # Print the iteration result
                if iter_log and (i + 1) % iter_log == 0:
                    logger.print_log(i)

                # Select a subgroup of parents
                if self.selection == 'wheel':
                    idx = selections.wheel(fitness, M=self.n_children, minimize=self.minimization)
                elif self.selection == 'tournament':
                    idx = selections.tournament(fitness, N=self.tournament_competitors,
                                                M=self.tournament_winners,
                                                iterations=int(self.n_children / self.tournament_winners),
                                                minimize=self.minimization)
                else:
                    raise ValueError("The specified selection doesn't match. Not applying the selection operation")
                parents = population.chromosomes[idx]

                # Use recombination to generate new children
                if not self.crossover:
                    warnings.warn("Warning: Crossover won't be applied")
                elif self.crossover == 'blend':
                    if type != "ga":
                        raise ValueError(
                            "The " + self.mutation +
                            " mutation is supported only by evolutionary strategies")
                    else:
                        children = crossovers.blend(parents, self.xover_prob, upper[idx], lower[idx])
                elif self.crossover == 'one_point':
                    if type != "ga":
                        raise ValueError(
                            "The " + self.mutation +
                            " mutation is supported only by evolutionary strategies")
                    else:
                        children = crossovers.one_point(parents, self.xover_prob)
                elif self.crossover == 'one_point_permutation':
                    if type != "ga":
                        raise ValueError(
                            "The " + self.mutation +
                            " mutation is supported only by evolutionary strategies")
                    else:
                        children = crossovers.one_point_permutation(parents, self.xover_prob)
                elif self.crossover == 'two_point':
                    if type != "ga":
                        raise ValueError(
                            "The " + self.mutation +
                            " mutation is supported only by evolutionary strategies")
                    else:
                        children = crossovers.two_point(parents, self.xover_prob)
                else:
                    raise ValueError("The specified crossover doesn't match. Not applying the crossover operation")

                # Mutate the generated children
                if not self.mutation:
                    warnings.warn("Warning: Mutation won't be applied")
                elif self.mutation == 'non_uniform':
                    if type != "ga":
                        raise ValueError(
                            "The " + self.mutation +
                            " mutation is supported only by genetic algorithms")
                    else:
                        children = mutations.non_uniform(children, self.mutat_prob, upper[idx], lower[idx],
                                                         i, self.n_iterations)
                elif self.mutation == 'uniform':
                    if type != "ga":
                        raise ValueError(
                            "The " + self.mutation +
                            " mutation is supported only by genetic algorithms")
                    else:
                        children = mutations.uniform(children, self.mutat_prob, upper[idx], lower[idx])
                elif self.mutation == 'swap':
                    if type != "ga":
                        raise ValueError(
                            "The " + self.mutation +
                            " mutation is supported only by genetic algorithms")
                    else:
                        children = mutations.pos_swap(children, self.mutat_prob)
                elif self.mutation == 'gaussian':
                    if type != "es":
                        raise ValueError(
                            "The " + self.mutation +
                            " mutation is supported only by evolutionary strategies")
                    else:
                        children, population.sigma = mutations.gaussian(parents, self.mutat_prob, lower, upper,
                                                                        population.sigma)
                else:
                    raise ValueError("The specified mutation doesn't match. Not applying the mutation operation")

                # Replace the current chromosomes of parents and childrens to
                # create the new chromosomes
                if self.replacement == 'elitist':
                    population.chromosomes = replacements.elitist(population.chromosomes, fitness,
                                                                  children, fitness_function(children),
                                                                  self.n_population, elitism=self.replacement_elitism,
                                                                  minimize=self.minimization)
                elif self.replacement == 'worst_parents':
                    population.chromosomes = replacements.worst_parents(parents, fitness, children, self.minimization)
                else:
                    raise ValueError("The specified replacement doesn't match. Not applying the replacement operation")

            # Print the best chromosome
            best = logger.get_log('best_chromosome')
            # Check that best is not an empty object
            if best.size:
                res = "\n-----------------------------------------\n"
                res += "Best individual:\n" + str(best[np.argmin(logger.get_log('best'))] if self.minimization else best[np.argmax(logger.get_log('best'))])
                print (res)

            # Plot the graph with all the results
            logger.plot()

        except ValueError as err:
            print(err.args)
