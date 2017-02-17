"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

import numpy as np

def _check(assertion):
    """
    Fucntion to check that the population is bigger than 0, therefore it is
    not an empty matrix.
    If it doesn't pass the assertion it raises an exception.
    """
    try:
        assert assertion
    except AssertionError as e:
        e.args += "The population cannot be an empty matrix"
        raise
        
def tournament(population, fitness, N=5, M=2, iterations=1, minimize=False):
    """
    This function returns the M best genes (parents) out of the N randomly sampled from the population
    first it gets the parents with smallest fitness
    second it gets its indexes in the population
    finally it returns their genes
    """
    # Check that population>0
    _check(len(population)>0 and len(population)==len(fitness))
    
    # Initialize the array that we will return
    samples = np.array([])
    
    for i in range(iterations):
        random_parents = np.random.randint(len(population), size=N)
        if minimize:
            samples = np.append(samples, population[random_parents[fitness[random_parents].argsort()[:M]]])
        else:
            samples = np.append(samples, population[random_parents[fitness[random_parents].argsort()[-M:]]])
    return samples.reshape(M*iterations, len(population[0]))


def wheel(population, fitness, N, M, iterations=1, replacement=True):
    """
    """
    _check(len(population)>0 and len(population)==len(fitness))

    random_parents = np.random.randint(len(population), size=N)
    wheel_prob = fitness[random_parents]/np.sum(fitness[random_parents])
    return population[np.random.choice(np.arange(0, N), M, replace=replacement, p=wheel_prob)]
    

def parent_replace(population, fitness, children):
    """
    Select the N worst fitness, where N is the number of children, out of the population 
    and change them for the new generated children
    """
    _check(len(population)>0 and len(population)==len(fitness))
    
    population[fitness.argsort()[-len(children):]] = children
    return population