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
