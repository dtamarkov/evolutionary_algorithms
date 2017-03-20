"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

import ga_tools as ga_tools


class Population(object):
    """
    Chromosome is an object that has the chromosomes and sigma.
    It is used in evolutionary algorithms.
    The chromosomes is the n-dimensional array that will be evaluated by the fitness function.
    Regarding the evolutionary-strategy followed sigma will be None or an array of values
    """

    def __init__(self, chromosomes=None, sigma=None, delta=None, alpha=None, s=None, space_s=None):
        """

        :param chromosomes:
        :param sigma: Parameter for evolutionary strategies
        :param delta: Paremeter to make a grid in the N-dimensional space and discretize the search space
        :param alpha: real part of the chromosomes in GGA(grid-based Genetic Algorithm)
        :param s: integer part of the chromosomes in GGA
        """
        self.chromosomes = chromosomes
        self.sigma = sigma
        self.s = s
        self.delta = delta
        self.alpha = alpha
        self.space_s = space_s

    def gga_chromosome(self, s=None, delta=None, alpha=None):
        s = s if s else self.s
        delta = delta if delta else self.delta
        alpha = alpha if alpha else self.alpha
        ga_tools.check(len(s) == len(delta) and len(delta) == len(alpha),
                       "Delta, Alpha and S must have the same number of elements (equal to the number of dimensions")
        return s * delta + alpha
