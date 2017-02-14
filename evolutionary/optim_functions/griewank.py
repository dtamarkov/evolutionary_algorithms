"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

from .functions import Function
import numpy as np

#################################################################        
class Griewank(Function):
    """
    The Griewank function has many widespread local minima, which are regularly distributed.
    D dimensional function
    Global minima at x* = (0, .. 0)
    (Source: https://www.sfu.ca/~ssurjano/griewank.html)
    """
    def __init__(self):
        """
        Initialize the function. 
        Call to its parent class and store the name of the optimization function.
        """
        super(self.__class__, self).__init__("Griewank")
    
    def evaluate(self, population):
        # Initialize vars
        add = 0.0
        mult = 1.0
        
        # Compute the sum and the multiplication
        for i in range(len(population)):
            add += float(population[i])**2
            mult *= np.cos(float(population[i])/np.sqrt(i+1))
        
        # Return the value of the function
        return 1 + add/4000 - mult
    
    def plot(self, d3=True, lower=-600, upper=600, samples=1000):
        """
        Makes a 2d plot using the parent class.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        if d3:
            super(self.__class__, self).plot3d(lower, upper, samples)
        else:
            super(self.__class__, self).plot(lower, upper, samples)