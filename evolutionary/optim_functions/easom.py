"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

from .functions import Function
import numpy as np

#################################################################        
class Easom(Function):
    """    
    The Easom function has several local minima. 
    It is unimodal, and the global minimum has a small area relative to the search space.
    2 dimensonal
    global minima at (pi,pi)
    (Source: https://www.sfu.ca/~ssurjano/ackley.html)
    """
    def __init__(self, a=False, b=False, c=False):
        """
        Initialize the Easom class
        """
        super(self.__class__, self).__init__("Easom")
    
    def evaluate(self, population):
        """
        Returns the fitness of a population using the Easom function.
        Population has to be a numpy array for this method to work.
        """
        # Check the var type of the population
        assert str(type(population)) == "<type 'numpy.ndarray'>" and len(population)==2
        
        # Make sintax closer to the source
        x1 = population[0]
        x2 = population[1]
        
        # Return the function
        return -np.cos(x1) * np.cos(x2) * np.exp(-(x1-np.pi)**2 - (x2-np.pi)**2)
    
    def plot(self, d3=True, lower=-100, upper=100, samples=1000):
        """
        Makes a 2d/3d (regarding the d3 var) plot using the parent classes.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        if d3:
            super(self.__class__, self).plot3d(lower, upper, samples)
        else:
            super(self.__class__, self).plot(lower, upper, samples)
        
