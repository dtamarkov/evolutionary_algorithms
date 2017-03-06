# [Under construction]

# Evolutionary Algorithms Library

The following library wraps the evolutionary process of the genetic algorithms and other evolutionary methods to make them easier to use. 

The library includes:
- [x] Logger
- [x] Optimization Functions
- [x] Genetic Algorithm
- [ ] Evolutionary strategies

## Code example
Working example of the library for solving the Ackley function with a Genetic Algorithm approach.

```python
from evolutionary.ga import GA

a = GA(
    seed=82634,
    minimization=False,
    n_dimensions=10,
    n_population=100,
    n_iterations=1000,
    n_children=100,
    xover_prob=0.8,
    mutat_prob=0.1,
    selection='wheel',
    crossover='blend',
    mutation='non_uniform',
    replacement='elitist'
)

a.run(iter_log=50)
```







