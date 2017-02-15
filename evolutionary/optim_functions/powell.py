"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

from .functions import Function
import numpy as np

#################################################################        
class Powell(Function):
    """    
    D dimensional
    (Source: https://www.sfu.ca/~ssurjano/powell.html)
    """
    def __init__(self):
        """
        Initialize the class
        Store the name of the class calling the parent class Function
        """
        super(self.__class__, self).__init__("Powell")
    
    def evaluate(self, population):
        """
        Returns the fitness of a population using the Ackley function.
        Population has to be a numpy array for this method to work.
        """     
        # Check the var type of the population
        assert str(type(population)) == "<type 'numpy.ndarray'>"
        
        # Case of matrix
        if len(population.shape) == 2:
            return np.apply_along_axis(self.evaluate, 1, population)
        
        # Initialize vars
        total_sum = 0.0
        
        for i in range(len(population)/4):
            part1 = population[i*4-3] + 10*population[i*4-2]
            part2 = 5*(population[i*4-1] - population[4*i])**2
            part3 = population[i*4-2] - 2*population[4*i-1]
            part4 = 10*(population[4*i-3] - population[4*i])**4
            sum += part1 + part2 + part3 + part4
    
        # Return the function
        return total_sum
    
    def plot(self, d3=True, lower=-4, upper=5, samples=1000):
        """
        Makes a 2d/3d (regarding the d3 var) plot using the parent classes.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        if d3:
            super(self.__class__, self).plot3d(lower, upper, samples)
        else:
            super(self.__class__, self).plot(lower, upper, samples)
        
