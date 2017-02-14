"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

import numpy as np


def tournament(population, fitness, N=5, M=2, iterations=1, minimize=False):
    """
    This function returns the M best genes (parents) out of the N randomly sampled from the population
    first it gets the parents with smallest fitness
    second it gets its indexes in the population
    finally it returns their genes
    """
    
    assert len(population)>0
    
    samples = np.array([])
    for i in range(iterations):
        random_parents = np.random.randint(len(population), size=N)
        if minimize:
            samples = np.append(samples, population[random_parents[fitness[random_parents].argsort()[:M]]])
        else:
            samples = np.append(samples, population[random_parents[fitness[random_parents].argsort()[-M:]]])
    return samples.reshape(M*iterations, len(population[0]))

def parent_replace(population, fitness, children):
    """
    Select the N worst fitness, where N is the number of children, out of the population 
    and change them for the new generated children
    """
    population[fitness.argsort()[-2:]] = children
    return population