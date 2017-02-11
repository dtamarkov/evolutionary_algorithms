"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

from .functions import Function
import numpy as np

#################################################################
class Rothyp(Function):
    """    
    The Rotated Hyper-Ellipsoid function is continuous, convex and unimodal. 
    It is an extension of the Axis Parallel Hyper-Ellipsoid function, 
    also referred to as the Sum Squares function.
    d dimensional.
    Global minima at x = (0,..,0)
    (Source: https://www.sfu.ca/~ssurjano/rothyp.html)
    """
    def __init__(self):
        super(self.__class__, self).__init__("Rothyp")
    
    def evaluate(self, population):
        """
        Returns the fitness of a population using the Rothyp function.
        Population has to be a numpy array for this method to work.
        """
        # Check the var type of the population
        assert str(type(population)) == "<type 'numpy.ndarray'>"
        
        # Initialize vars
        res_sum = 0.0
                        
        # Compute the sums on the population
        for i in range(len(population)):
            for j in range(i+1):
                res_sum += population[j]**2

        # Return the function
        return res_sum
    
    def plot(self, d3=True, lower=-10, upper=10, samples=1000):
        """
        Makes a 2d plot using the parent class.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        if d3:
            super(self.__class__, self).plot3d(lower, upper, samples)
        else:
            super(self.__class__, self).plot(lower, upper, samples)
