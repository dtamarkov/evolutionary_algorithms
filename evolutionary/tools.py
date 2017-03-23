"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""
from __future__ import division
import ga_tools as ga_tools
import numpy as np


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
        self.discrete_space = space_s
        self.delta = delta
        self.alpha = alpha
        self.space_s = space_s

    def gga_initialization(self, upper, lower, n_population, grid_intervals):
        """

        :param upper:
        :param lower:
        :param n_population:
        :return: this function returns the delta, alpha, s and space_s values for all the chromosomes of the population
        """

        def get_iter_params():
            """

            :return: returns the delta, alpha, S and space_s values for one iteration
            """
            aux_delta = np.array([(upper[i] - lower[i]) / grid_intervals for i in range(len(upper))])
            aux_upper_s = np.floor(upper / aux_delta)
            aux_lower_s = np.ceil(lower / aux_delta)
            aux_s = np.array([np.random.randint(aux_lower_s[i], aux_upper_s[i]+1) for i in range(len(aux_lower_s))])
            aux_alpha = np.array([np.random.uniform(0, delta) for delta in aux_delta])

            # Calculate taking into account that each dimension could have a different upper or lower bound
            # for i in range(len(upper[1:])):
            #     # Compute the delta value for the dimension and add it to the array of deltas
            #     aux_delta = np.hstack((aux_delta, (upper[i] - lower[i]) / 10))
            #
            #     # Discretize the search space with the values of the bounds for the dimension i
            #     space_s = np.vstack((space_s,
            #                          np.arange(np.floor(lower[i] / aux_delta[-1]),
            #                                    np.floor(upper[i] / aux_delta[-1])).astype(int)))
            #
            #     # Get the position by sampling one point in the space
            #     aux_s = np.hstack((aux_s, space_s[-1][np.random.randint(len(space_s[-1]))]))
            #
            #     # Sample the alpha values between 0 and delta from a uniform distribution
            #     aux_alpha = np.hstack((aux_alpha, np.random.uniform(0, aux_delta[-1])))
            return aux_delta, aux_alpha, aux_s, aux_upper_s, aux_lower_s

        # Initialize vars
        delta, alpha, S, upper_s, lower_s = get_iter_params()

        # Iterate to generate as many chromosomes as the number of the population
        for _ in range(n_population - 1):
            d, a, s, u_s, l_s = get_iter_params()
            delta = np.vstack((delta, d))
            alpha = np.vstack((alpha, a))
            S = np.vstack((S, s))
            upper_s = np.vstack((upper_s, u_s))
            lower_s = np.vstack((lower_s, l_s))

        self.delta = delta
        self.alpha = alpha
        self.s = S
        self.gga_chromosome()
        return upper_s.astype.astype(int), lower_s.astype(int)

    def gga_chromosome(self, s=None, delta=None, alpha=None):
        """

        :param s:
        :param delta:
        :param alpha:
        :return: The function creates the chromosomes of the population of a grid-based genetic algorithm
         if not given it uses the parameters that the object has itself.
        """
        s = s if s else self.s
        delta = delta if delta else self.delta
        alpha = alpha if alpha else self.alpha
        ga_tools.check(len(s) == len(delta) and len(delta) == len(alpha),
                       "Delta, Alpha and S must have the same number of elements (equal to the number of dimensions")
        self.chromosomes = s * delta + alpha
