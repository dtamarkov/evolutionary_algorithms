"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""
from __future__ import division
import numpy as np

def _check(assertion, message):
    """
    Test function that receives two vars.
    assertion is a boolean which should be true in order to avoid to throw an exception
    message is an string with the error message to show if the exception is thrown
    If it doesn't pass the assertion it raises an exception.
    """
    try:
        assert assertion
    except AssertionError as e:
        e.args += message
        raise

def random_n(N, chromosomes):
    #shuffle the parents to prevent any correlation
    shuffle = np.arange(len(chromosomes))
    np.random.shuffle(shuffle)
    return shuffle[:N]

def tournament(parents, fitness, N=5, M=2, iterations=1, minimize=True):
    """
    parents is an array of chromosomes
    fitness is the chromosomes fitness
    N is the number of parents randomly sampled from parents
    M is the number of parents sampled with the wheel selection
    iterations is the number of times we sample M parents
    
    This function returns the M best genes (parents) out of the N randomly sampled from the population
    first it gets the parents with smallest fitness
    second it gets its indexes in the population
    finally it returns their genes
    """
    # Check that population>0
    _check(len(parents)>0, "The population cannot be an empty matrix")
    _check(len(parents)==len(fitness), "len(population) and len(fitness) are not the same")

    
    # Initialize the array that we will return
    indices = np.array([])
    for i in range(iterations):
        
        # Generate an array of random values to randomly select a subgroup of parents
        random_parents = random_n(N, parents)
        if minimize:
            idx = fitness[random_parents].argsort()[:M]
        else:
            idx = fitness[random_parents].argsort()[-M:][::-1]
            
        indices = np.append(indices, random_parents[idx])

    # Return the indices as an array of integers
    indices = indices.astype(np.int64)
    return parents[indices], indices


def wheel(parents, fitness, N, M, iterations=1, replacement=True, minimize=True):
    """
    Wheel selection method. 
    parents is an array of chromosomes
    fitness is the chromosomes fitness
    N is the number of parents randomly sampled from population
    M is the number of parents sampled with the wheel selection
    iterations is the number of times we sample M parents using the wheel method
    replacement is a boolean either to sample with or without replacement
    
    The wheel selection method assigns a probability of parent_fitness/sum(fitness) to
    a subgroup of N parents from the population. Then using this probabilities it samples M
    parents of the subgroup. This is repeated iterations times. The M*iterations parents 
    that have been sampled are returned.
    """
    _check(len(parents)>0, "The parents cannot be an empty matrix")
    _check(len(parents)==len(fitness), "len(parents) and len(fitness) are not the same")
           
    # Initialize vars
    indices = np.array([])

    # Loop iterations times
    for i in range(iterations):
        # Select N parents from the parents
        random_parents = random_n(N, parents)        

        # Calculate its probabilites
        if minimize:
            # Normalize the fitness matrix so it is suitable for a minimization problem
            norm_fitness = np.absolute(fitness[random_parents]-np.max(fitness))
            
            # Compute the probabilities proportionaly to the fitness
            wheel_prob = norm_fitness/ np.sum(norm_fitness)
        else:
            wheel_prob = fitness[random_parents]/ np.sum(fitness[random_parents])

        # Sample M indices from random_parents with the calculated probabilities
        indices = np.append(indices, random_parents[np.random.choice(np.arange(0, N), M, replace=replacement, p=wheel_prob)])
    
    # Return the indices as an array of integers
    indices = indices.astype(np.int64)
    return parents[indices], indices