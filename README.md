# [Under construction]

# Evolutionary Algorithms Library

The following library wraps the evolutionary process of the genetic algorithms and other evolutionary methods to make them easier to use. 

The library includes:
- [x] Logger
- [x] Optimization Functions
- [x] Genetic Algorithm
- [x] Evolutionary strategies (simple version (1 sigma))
- [ ] Evolutionary strategies (array of sigmas)

## Optimization functions
The optimization functions are adepted pieces of code obtained from the [web](https://www.sfu.ca/~ssurjano/)

In particular, the library has implemented the following:
- **Ackley**
- **Forrester**
- **Beale**
- **Rothyp**
- **Booth**
- **Easom**
- **Griweank**
- **Matyas**
- **Powell**
- **Zakharov**

An example of the functions plotted can be found [here](notebooks/simulated_annealing_ackley.ipynb)

## Initializations
- **uniform** uses a uniform distribution to sample the elements.
- **permutation** creates a permutation of *N* elements.

## Selections
- **wheel**: sample from the parents population with a probability of each member proportional to the value of their fitness
- **tournament**:

## Mutations

- **position swap**:
- **uniform**:
- **non-uniform**:
- **gaussian**: (Note: this is the mutation used for Evolutionary Strategies[ES])

## Crossovers
- **one-point**:
- **one-point (permutation)**:
- **two-point**:
- **blend**:

## Replacements
- **worst-fitness**: removes only the chromosomes in the parents population.
- **elitist**:

## Code example

```python
from evolutionary import EAL, optim_functions as functions

# Example of a Genetic Algorithm to solve the ackley function
eal_ga = EAL(
    seed=82634,
    minimization=False,
    problem=functions.Ackley,
    n_dimensions=10,
    n_population=50,
    n_iterations=1000,
    n_children=50,
    xover_prob=0.8,
    mutat_prob=0.2,
    selection='tournament',
    mutation='gaussian',
    replacement='elitist'
)
eal_ga.ga()

eal_es = EAL(
    seed=82634,
    minimization=False,
    problem=functions.Ackley,
    n_dimensions=10,
    n_population=50,
    n_iterations=1000,
    n_children=50,
    xover_prob=0.8,
    mutat_prob=0.2,
    selection='tournament',
    mutation='gaussian',
    replacement='elitist'
)

eal_es.es(iter_log=50)
```