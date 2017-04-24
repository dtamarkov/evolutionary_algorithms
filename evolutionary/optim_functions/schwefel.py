"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: April - 2017
"""

import numpy as np

from .functions import Function


class Schwefel(Function):
    """

    """

    def __init__(self, lower=-500., upper=500., minimize=True):
        """
        Initialize the function.
        Call to its parent class and store the name of the optimization function.
        """
        self.lower = lower
        self.upper = upper
        self.minimize = minimize
        self.dim = None
        self.name = "Schwefel"
        super(self.__class__, self).__init__(self.name)

    def evaluate(self, population):
        """
        """

        # Check the var type of the population
        super(self.__class__, self)._check(str(type(population)) == "<type 'numpy.ndarray'>",
                                           'The population has to be a numpy array')
        offset = 0.000127278374748

        # Case of matrix
        if len(population.shape) == 2:
            return np.apply_along_axis(self.evaluate, 1, population)

        # Calculate the sums over the population
        sum = np.sum(population * np.sin(np.sqrt(np.abs(population))))

        # Return the value of the function
        return (418.9829*len(population) - sum - offset) if self.minimize else -(418.9829*len(population) - sum - offset)

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