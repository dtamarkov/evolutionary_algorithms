"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

from .functions import Function
import numpy as np

#################################################################        
class Ackley(Function):
    """    
    The Ackley function is widely used for testing optimization algorithms.
    It is characterized by a nearly flat outer region, and a large hole at the centre. 
    The function poses a risk for optimization algorithms, particularly hillclimbing algorithms, 
    to be trapped in one of its many local minima. 
    (Source: https://www.sfu.ca/~ssurjano/ackley.html)
    """
    def __init__(self, a=False, b=False, c=False):
        """
        Initialize the Ackley class with the values of a, b and c
        """
        super(self.__class__, self).__init__("Ackley")
        self.a = 20 if not a else a
        self.b = 0.2 if not b else b
        self.c = 2 * np.pi if not c else c
    
    def evaluate(self, population):
        """
        Returns the fitness of a population using the Ackley function.
        Population has to be a numpy array for this method to work.
        """
        # Check the var type of the population
        assert str(type(population)) == "<type 'numpy.ndarray'>" and len(population)>0
        
        if len(population.shape) > 1:
            return np.apply_along_axis(self.evaluate, 1, population)
        
        # Initialize vars
        firstSum = 0.0
        secondSum = 0.0 
        n = float(len(population))
        
        # Compute the sums on the population
        for i in population:
            firstSum += i**2.0
            secondSum += np.cos(2.0*self.c*i)

        # Return the function
        return -self.a*np.exp(-self.b*np.sqrt(firstSum/n)) - np.exp(secondSum/n) +  self.a + np.e
    
    def plot(self, d3=True, lower=-32, upper=32, samples=1000):
        """
        Makes a 2d/3d (regarding the d3 var) plot using the parent classes.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        if d3:
            super(self.__class__, self).plot3d(lower, upper, samples)
        else:
            super(self.__class__, self).plot(lower, upper, samples)
        
