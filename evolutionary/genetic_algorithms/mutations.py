"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""
from __future__ import division
import numpy as np

U = np.random.uniform

def _check(assertion, message):
    """
    Fucntion to check that the population is bigger than 0, therefore it is
    not an empty matrix.
    If it doesn't pass the assertion it raises an exception.
    """
    try:
        assert assertion
    except AssertionError as e:
        e.args += message
        raise

        
def pos_swap(chromosomes, prob):
    """
    Try to make a small change on the structure of the children by swapping 
    two randomly sampled positions of the population
    """
    _check(len(chromosomes)>0, "The population cannot be an empty matrix")
    
    # Convert to 2D matrix if it is a 1D array
    if len(chromosomes.shape) == 1:
        chromosomes = np.array([chromosomes])
    
    _check(len(chromosomes.shape)==2, "The chromosomes can only be a 1D array or 2D matrix")
    
    for row in chromosomes:
        if U(0,1) < prob:
            v1 = np.random.randint(len(row))
            v2 = np.random.randint(len(row))
            while v1==v2:
                v2 = np.random.randint(len(row))
            row[v1], row[v2] = row[v2], row[v1]
    return chromosomes

def uniform(chromosomes, prob, upper, lower):
    """
    Try to make a small change on the structure of the children by swapping 
    two randomly sampled positions of the population
    """
    _check(len(chromosomes)>0, "The population cannot be an empty matrix")
    
    # Convert to 2D matrix if it is a 1D array
    if len(chromosomes.shape) == 1:
        chromosomes = np.array([chromosomes])
    if len(upper.shape) == 1:
        upper = np.array([upper])
    if len(lower.shape) == 1:
        lower = np.array([lower])
    
    _check(len(chromosomes.shape)==2, "The chromosomes can only be a 1D array or 2D matrix")
    
    # Create matrix of booleans that determine wether to mutate or not
    to_mutate = U(0, 1, chromosomes.shape)<prob

    # Iterate over each value of the chromosomes
    for i in range(len(chromosomes)):
        for j in range(len(chromosomes[i])):
            # pre-compute the value after the mutation
            aux = chromosomes[i, j] + (U(0, 1)-0.5)*0.5*(upper[i, j]-lower[i, j])
            
            # check that the pre-computed mutation is between the lower and upper bounds. 
            # repeat the process if it is not
            while (lower[i, j] > aux or upper[i, j] < aux):
                aux = chromosomes[i, j] + (U(0, 1)-0.5)*0.5*(upper[i, j]-lower[i, j])
                
            # once the mutation is between the problem bounds assign it to the chromosomes value
            chromosomes[i, j] = aux
            
    # return the new generated chromosomes
    return chromosomes
    
def non_uniform(chromosomes, prob, upper, lower, t, tmax, b=5.):
    """
    TODO: check implementation
    xj' = xj + tau * (uj - lj) * (1 - ui^(1-(t/tmax))^b 
    """
    _check(len(chromosomes)>0, "The population cannot be an empty matrix")
    
    # Convert to 2D matrix if it is a 1D array
    if len(chromosomes.shape) == 1:
        chromosomes = np.array([chromosomes])
    if len(upper.shape) == 1:
        upper = np.array([upper])
    if len(lower.shape) == 1:
        lower = np.array([lower])
    
    _check(len(chromosomes.shape)==2, "The chromosomes can only be a 1D array or 2D matrix")
    
    # Create matrix of booleans that determine wether to mutate or not
    to_mutate = U(0, 1, chromosomes.shape)<prob
    
    def f(value, i, j):
        tau = upper[i, j]-lower[i, j] if U(0, 1)>0.5 else lower[i, j]-upper[i, j]
        snd_part = (1.-U(0, 1)**((1.-t/tmax)**b))
        return value + tau * snd_part
    
    for i in range(len(chromosomes)):
        for j in range(len(chromosomes[i])):
            if to_mutate[i, j]:
                aux = f(chromosomes[i, j], i, j)
                while (lower[i, j] > aux or upper[i, j] < aux):
                    aux = f(chromosomes[i, j], i, j)
                chromosomes[i, j] = aux
    return chromosomes