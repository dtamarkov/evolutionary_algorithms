"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

from .functions import Function
import numpy as np

#################################################################        
class Forrester(Function):
    """    
    This function is a simple one-dimensional test function. 
    It is multimodal, with one global minimum, one local minimum and a zero-gradient inflection point. 
    (Source: https://www.sfu.ca/~ssurjano/forretal08.html)
    """
    def __init__(self):
        """
        """
        super(self.__class__, self).__init__("Forrester")
    
    def evaluate(self, population):
        """
        """
        # Check the var type of the population
        assert str(type(population)) == "<type 'numpy.ndarray'>"
        
        # Case of matrix
        if len(population.shape) == 2:
            return np.apply_along_axis(self.evaluate, 1, population)
        
        # Check the var type of the population
        assert len(population)==1
        
        # Make syntax closer to the source
        x = float(population[0])
        
        # Return its value
        return (6*x-2)**2 * np.sin(12*x-4)
            
    
    def plot(self, d3=False, lower=0, upper=1, samples=1000):
        """
        Makes a 2d plot using the parent class.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        if d3:
            print "Matyas function is 1 dimensional, therefore it cannot have a 3d plot"
        else:
            super(self.__class__, self).plot(lower, upper, samples)

            