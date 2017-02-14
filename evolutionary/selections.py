"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""
import numpy as np


def tournament(population, fitness, N, M, iterations=1):
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
        samples = np.append(samples, population[random_parents[fitness[random_parents].argsort()[-M:]]])
    return samples.reshape(M*iterations, len(population[0]))