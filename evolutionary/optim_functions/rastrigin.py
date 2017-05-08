"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: April - 2017
"""

import numpy as np

from .functions import Function


class Rastrigin(Function):
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
        self.name = "Rastrigin"
        super(self.__class__, self).__init__(self.name)

    def evaluate(self, population):
        """
        """

        # Check the var type of the population
        super(self.__class__, self)._check(str(type(population)) == "<type 'numpy.ndarray'>",
                                           'The population has to be a numpy array')

        # Case of matrix
        if len(population.shape) == 2:
            return np.apply_along_axis(self.evaluate, 1, population)

        # Calculate the sums over the population
        sum_1 = np.sum(population ** 2)
        sum_2 = np.sum(np.cos(population * np.pi * 2))

        # Return the value of the function
        res = 10 * len(population) + sum_1 - 10 * sum_2
        return res if self.minimize else -res

    def plot(self, d3=True, samples=1000):
        """
        Makes a 2d plot using the parent class.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        if d3:
            super(self.__class__, self).plot3d(self.lower, self.upper, samples)
        else:
            super(self.__class__, self).plot(self.lower, self.upper, samples)