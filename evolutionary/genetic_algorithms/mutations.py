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

def pos_swapping(population, prob):
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

# TODO change population object so it has [chromosome, sigma]
def gaussian(population, prob, lower, upper, sigma):
    _check(len(population)>0)
    tau = 1/np.sqrt(len(population))
    for i in range(len(population)):
        sigma = max(sigma * np.exp(tau*np.random.normal(0, 1), 1e-10)
        population[i] = population[i] + sigma*np.random.normal()
        # verificar que estan entre los rangos especificados upper y lower
        population[>upper] = upper
        population[<lower] = lower
            
return population


def not_uniform(population, prob, upper, lower, t, tmax, b=5):
    """
    xj' = xj + tao * (uj - lj) * (1 - ui^(1-(t/tmax))^b 
    """
    _check(len(population)>0)
    
    to_mutate = np.random.uniform(0, 1, population.shape)
    for i in range(len(population)):
        for j in range(len(population[i])):
            if to_mutate[i,j] < prob:
                while(upper < population[i, j] or lower > population[i, j]):
                    tau = upper-lower if np.random.uniform(0, 1, 1)>0.5 else lower-upper
                    population[i, j] = population[i, j] + tao * (1- np.random.uniform(0, 1, 1)**(1-t/tmax)**b)
    return population