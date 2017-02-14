"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

import numpy as np

def pos_swapping(population, prob):
    """
    Try to make a small change on the structure of the children by swapping 
    two randomly sampled positions of the population
    """
    for row in population:
        if np.random.uniform(0,1) < prob:
            values = np.random.randint(len(row), size=2)
            row[values[0]], row[values[1]] = row[values[1]], row[values[0]]
    return population