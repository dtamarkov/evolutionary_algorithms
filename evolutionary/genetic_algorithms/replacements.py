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
    assertion is a boolean which should be true in order to avoid to throw an exception.
    message is an string with the error message to show if the exception is thrown
    If it doesn't pass the assertion it raises an exception.
    """
    try:
        assert assertion
    except AssertionError as e:
        e.args += message
        raise
        
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
    
    # Gather the parents and children and its fitness
    chromosomes = np.vstack((parents, children))
    fitness = np.hstack((pa_fitness, ch_fitness))
    
    # Get the number of chromosomes to sample as elitist and the rest of chromosomes
    n_elitist = int(np.ceil(M*elitism))
    n_rest = int(M-n_elitist)
    
    # Check that the fitness values are meaningful, if not assing equiprobability
    if np.sum(fitness)<1e-15:
        fitness_prob = np.ones(fitness.shape)*(1.0/len(fitness))
    else:
        # Calculate its probabilites
        if minimize:
            # Normalize the fitness matrix so it is suitable for a minimization problem
            norm_fitness = np.absolute(fitness-np.max(fitness))
            
            # Compute the probabilities proportionaly to the fitness
            fitness_prob = norm_fitness/ np.sum(norm_fitness)
        else:
            # Compute the probabilities proportionaly to the fitness
            fitness_prob = fitness/ np.sum(fitness)
        
    # Get the non elitist part of the chromosomes with a probability proportional
    # to the value of the fitness
    rest_chromosomes = chromosomes[np.random.choice(np.arange(0,len(chromosomes)), n_rest, replace=replacement, p=fitness_prob)]
    
    # Get
    if minimize:
        elitist_chromosomes = chromosomes[fitness.argsort()[:n_elitist]]
    else:
        elitist_chromosomes = chromosomes[fitness.argsort()[-n_elitist:][::-1]]

    # Group the elitist and the rest of the chromosomes together
    final_chromosomes = np.vstack((elitist_chromosomes, rest_chromosomes))
    
    # Shuffle the final matrix to avoid groups of elitist
    shuffle = np.arange(len(final_chromosomes))
    np.random.shuffle(shuffle)
    
    # Return the shuffled array
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