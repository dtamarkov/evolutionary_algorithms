"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

from .functions import Function
import numpy as np

#################################################################
class Beale(Function):
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
        super(self.__class__, self).__init__("Beale")
    
    def evaluate(self, population):
        # ensure population is 2 dimensiona
        assert len(population) == 2
        
        # Make sintax closer to the source
        x1 = float(population[0])
        x2 = float(population[1])
        
        # Compute the three parts of the function
        part1 = (1.5 - x1 + x1*x2)**2
        part2 = (2.225 - x1 + x1*(x2**2))**2
        part3 = (2.625 - x1 + x1*(x2**3))**2
        
        # Return the value of the function
        return part1 + part2 + part3
    
    def plot(self, d3=True, upper=0, lower=0,  samples=0):
        """
        Makes a 2d plot using the parent class.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        if d3:
            super(self.__class__, self).plot3d(lower, upper, samples)
        else:
            print "Beale function is 2 dimensional, therefore, it cannot be displayed in a 2d plot"
        