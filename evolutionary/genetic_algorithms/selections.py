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
    samples = np.array([])
    for i in range(iterations):
        random_parents = np.random.randint(len(parents), size=N)
        if minimize:
            samples = np.append(samples, parents[fitness[random_parents].argsort()[:M]])
        else:
            samples = np.append(samples, parents[fitness[random_parents].argsort()[-M:][::-1]])
    return samples.reshape(M*iterations, len(parents[0]))


def wheel(parents, fitness, N, M, iterations=1, replacement=True):
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
    samples = np.array([])

    # Loop iterations times
    for i in range(iterations):
        # Select N parents from the parents
        random_parents = np.random.randint(len(parents), size=N)
        
        # Calculate its probabilites
        wheel_prob = fitness[random_parents]/ float(np.sum(fitness[random_parents]))

        # Sample M parents from random_parents with the calculated probabilities
        samples = np.append(samples, parents[np.random.choice(np.arange(0, N), M, replace=replacement, p=wheel_prob)])

    return samples.reshape(M*iterations, len(parents[0]))
    
def elitist(parents, pa_fitness, children, ch_fitness, M, elitism=0.5, replacement=True, minimize=True):
    """
    parents is the current chromosomes
    pa_fitness is parents fitness value
    children is the generated chromosomes
    ch_fitness is children fitness value
    M is the number of elements to select
    """
    _check(len(parents)>0, "The parents cannot be an empty matrix")
    _check(len(parents)+len(children) >= M, "Number of survival chromosomes cannot be higher than the number of parents and children")
    _check(len(parents)==len(pa_fitness), "len(parents) and len(pa_fitness) are not the same")
    _check(len(children)==len(ch_fitness), "len(children) and len(ch_fitness) are not the same")
    
    chromosomes = np.vstack((parents, children))
    fitness = np.hstack((pa_fitness, ch_fitness))
    
    n_elitist = int(np.ceil(M*elitism))
    n_rest = int(M-n_elitist)
    fitness_scaled = fitness - np.min(fitness)
    if np.sum(fitness_scaled)<1e-15:
        fitness_prob = np.ones(fitness.shape)*(1.0/len(fitness))
    else:
        fitness_prob = fitness_scaled/np.sum(fitness_scaled)

    rest_chromosomes = chromosomes[np.random.choice(np.arange(0,len(chromosomes)), n_rest, replace=replacement, p=fitness_prob)]
    
    if minimize:
        elitist_chromosomes = chromosomes[fitness.argsort()[:n_elitist]]
    else:
        elitist_chromosomes = chromosomes[fitness.argsort()[-n_elitist:][::-1]]
        
    final_chromosomes = np.vstack((elitist_chromosomes, rest_chromosomes))
    shuffle = np.arange(len(final_chromosomes))
    np.random.shuffle(shuffle)
    return final_chromosomes[shuffle]
    
def parent_replace(parents, fitness, children, minimize=True):
    """
    Select the N worst fitness, where N is the number of children, out of the population 
    and change them for the new generated children
    """
    _check(len(parents)>0, "The population cannot be an empty matrix")
    _check(len(parents)==len(fitness), "len(parents) and len(pa_fitness) are not the same")

    if worst:
        parents[fitness.argsort()[-len(children):][::-1]] = children
    else:
        parents[fitness.argsort()[:len(children)]] = children
    return parents