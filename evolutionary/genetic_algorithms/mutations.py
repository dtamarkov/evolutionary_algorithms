"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""
from __future__ import division
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

        
def pos_swap(population, prob):
    """
    Try to make a small change on the structure of the children by swapping 
    two randomly sampled positions of the population
    """
    _check(len(population)>0)
    
    for row in population:
        if np.random.uniform(0,1) <= prob:
            values = np.random.randint(len(row), size=2)
            row[values[0]], row[values[1]] = row[values[1]], row[values[0]]
    return population


def non_uniform(population, prob, upper, lower, t, tmax, b=5):
    """
    TODO: check implementation
    xj' = xj + tau * (uj - lj) * (1 - ui^(1-(t/tmax))^b 
    """
    _check(len(population)>0)
    
    to_mutate = np.random.uniform(0, 1, population.shape)<=prob
    
    def f(value):
        tau = upper-lower if np.random.uniform(0, 1)>0.5 else lower-upper
        snd_part = (1-np.random.uniform(0, 1)**((1-t/tmax)**b))
        return value + tau * snd_part
    
    for i in range(len(population)):
        for j in range(len(population[i])):
            if to_mutate[i, j]:
                population[i, j] = f(population[i, j])
                while (lower > population[i, j] or upper < population[i, j]):
                    population[i, j] = f(population[i, j])
    return population