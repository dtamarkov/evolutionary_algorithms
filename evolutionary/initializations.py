"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

import numpy as np

def uniform(n_population, lower, upper, N):
    """
    Function to initialize the population. 
    Each member of the population is a candidate initialized randomly 
    using the given uniform distribution.
    A number N of samples are generated between the lower(L) and upper(U) bounds.
    """
    
    population = [np.random.uniform(lower, upper, N)]
    for i in range(n_population-1):
        population = np.concatenate((population, [np.random.uniform(lower, upper, N)]))
    return population

def permutation(n_population, N):
    """
    Function to initialize the population. Each member of the population
    is a candidate initialized randomly with a permutation of the number (N)
    """
    
    population = [np.random.permutation(N)]
    for i in range(n_population-1):
        population = np.concatenate((population, [np.random.permutation(N)]))
    return population