"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

from .functions import Function
import numpy as np

#################################################################
class Zakharov(Function):
    """
    The Beale function is multimodal, with sharp peaks at the corners of the input domain.
    2 Dimensional
    Global minima x = (3, 0.5)
    (Source: https://www.sfu.ca/~ssurjano/beale.html)
    """
    def __init__(self):
        """
        Initialize the function. 
        Call to its parent class and store the name of the optimization function.
        """
        super(self.__class__, self).__init__("Zakharov")
    
    def evaluate(self, population):
        # Ensure the data types are correct
        assert str(type(population)) == "<type 'numpy.ndarray'>"

        # Initialize vars
        sum1, sum2 = 0.0, 0.0
        
        # Calculate the sums over the population
        for i in range(len(population)):
            sum1 += population[i]**2
            sum2 += 0.5*(i+1)*population[i]
            
        # Return the value of the function
        return sum1 + sum2**2 + sum2**4
    
    def plot(self, d3=True, lower=-10, upper=10,  samples=1000):
        """
        Makes a 2d plot using the parent class.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        if d3:
            super(self.__class__, self).plot3d(lower, upper, samples)
        else:
            print "Beale function is 2 dimensional, therefore, it cannot be displayed in a 2d plot"
        