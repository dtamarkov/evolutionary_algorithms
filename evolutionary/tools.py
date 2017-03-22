"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

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
        self.discrete_space
        self.delta = delta
        self.alpha = alpha
        self.space_s = space_s

    def gga_initialization(self, upper, lower, n_population):
        """

        :param upper:
        :param lower:
        :param n_population:
        :return:
        """

        def get_iter_params():
            """

            :return:
            """
            aux_delta = np.array([(upper[0] - lower[0]) / 10])
            space_s = np.arange(np.floor(lower[0] / aux_delta[-1]), np.floor(upper[0] / aux_delta[-1])).astype(int)
            aux_s = space_s[np.random.randint(len(space_s))]
            aux_alpha = np.random.uniform(0, aux_delta)

            # Calculate taking into account that each dimension could have a different upper or lower bound
            for i in range(len(upper[1:])):
                # Compute the delta value for the dimension and add it to the array of deltas
                aux_delta = np.hstack((aux_delta, (upper[i] - lower[i]) / 10))

                # Discretize the search space with the values of the bounds for the dimension i
                space_s = np.vstack((space_s,
                                     np.arange(np.floor(lower[i] / aux_delta[-1]),
                                               np.floor(upper[i] / aux_delta[-1])).astype(int)))

                # Get the position by sampling one point in the space
                aux_s = np.hstack((aux_s, space_s[-1][np.random.randint(len(space_s[-1]))]))

                # Sample the alpha values between 0 and delta from a uniform distribution
                aux_alpha = np.hstack((aux_alpha, np.random.uniform(0, aux_delta[-1])))
            return aux_delta, aux_alpha, aux_s, space_s

        # Initialize vars
        delta, alpha, S, space = get_iter_params()

        # Iterate to generate as many chromosomes as the number of the population
        for _ in range(n_population - 1):
            d, a, s, sp = get_iter_params()
            delta = np.vstack((delta, d))
            alpha = np.vstack((alpha, a))
            S = np.vstack((S, s))
            space = np.vstack((space, sp))
        self.delta = delta
        self.alpha = alpha
        self.s = S
        self.discrete_space = space

    def gga_chromosome(self, s=None, delta=None, alpha=None):
        s = s if s else self.s
        delta = delta if delta else self.delta
        alpha = alpha if alpha else self.alpha
        ga_tools.check(len(s) == len(delta) and len(delta) == len(alpha),
                       "Delta, Alpha and S must have the same number of elements (equal to the number of dimensions")
        return s * delta + alpha
