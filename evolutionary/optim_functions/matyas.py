"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

from .functions import Function
import numpy as np

#################################################################        
class Matyas(Function):
    """    
    This function is a simple one-dimensional test function. 
    It is multimodal, with one global minimum, one local minimum and a zero-gradient inflection point. 
    2 dimensional
    (Source: https://www.sfu.ca/~ssurjano/matya.html)
    """
    def __init__(self):
        """
        Initialize the function. 
        Call to its parent class and store the name of the optimization function.
        """
        super(self.__class__, self).__init__("Matyas")
    
    def evaluate(self, population):
        """
        """
        # Check the var type of the population
        assert str(type(population)) == "<type 'numpy.ndarray'>"
        
        # Case of matrix
        if len(population.shape) == 2:
            return np.apply_along_axis(self.evaluate, 1, population)
        
        # Check the var type of the population
        assert len(population)==2
        
        # Make syntax closer to the source
        x1 = float(population[0])
        x2 = float(population[1])
        
        # Return its value
        return 0.26*(x1**2 + x2**2) - 0.48*x1*x2   
    
    def plot(self, d3=True, lower=-10, upper=10, samples=1000):
        """
        Makes a 2d plot using the parent class.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        if d3:
            super(self.__class__, self).plot3d(lower, upper, samples)
        else:
            print "Matyas function is 2 dimensional, therefore it cannot have a 2d plot"
        