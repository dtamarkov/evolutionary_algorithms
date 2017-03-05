"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""
import crossovers
import mutations
import intializations
import selections
from ...optim_functions import *

class Genetic_algorithm(object):
    """
    """
        
    def __init__(self, initialization, selection, mutation, crossover, survivals, fitness_function, bounds):
        """
        """
        self.name = name
        self.selection = selection
        self.mutation = mutation
        self.crossover = crossover
        self.survivals = survivals
        self.lower = bounds[0]
        self.upper = bounds[1]
        
    def iterate(n_population=100, n_dimensions=2, prob_xover=1, prob_mutation=0.8, n_iterations=100):
        """
        """
        # Create all the population 
        population = self.initialization(n_population, self.lower, self.upper, n_dimensions)

        # Iterate simulating the evolutionary process
        for i in range(n_iterations):
            # Apply the function in each row to get the array of fitness
            fitness = fitness_function(population)

            # Do the evolutionary process: selection -> crossover -> mutation -> 
            parents = self.selection(population, fitness, 8, 2, minimize=True)
            children = self.crossover(parents, 1)
            children = self.mutation(children, 0.8, self.upper, lower, i, n_iterations)
            population = self.survivals(population, fitness, children)




   
