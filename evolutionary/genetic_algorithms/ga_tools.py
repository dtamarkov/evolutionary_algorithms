"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""
import numpy as np


def wheel_prob(fitness, minimize):
    """
    :param fitness:
    :param minimize:
    :return:
    """
    if minimize:
        # Normalize the fitness matrix so it is suitable for a minimization problem
        norm_fitness = np.absolute(fitness - np.max(fitness)) + np.min(fitness)
    else:
        # Normalize the fitness matrix so it is suitable for a minimization problem
        norm_fitness = fitness - np.min(fitness)

    # Compute the probabilities proportionaly to the fitness
    return norm_fitness / np.sum(norm_fitness)


def n_sort(fitness, n, minimize):
    """


    :param fitness: fitness value of each chromosome
    :param n: number of chromosomes that are going to be returned
    :param minimize: minimization problem or maximization (boolean)
    :return: return n chromosomes from a sorted array regarding if it is a minimization
             or maximization problem
    """
    if minimize:
        return fitness.argsort()[:n]
    else:
        return fitness.argsort()[-n:][::-1]