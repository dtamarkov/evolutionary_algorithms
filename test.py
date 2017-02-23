from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import evolutionary.genetic_algorithms.initializations as initialization
import evolutionary.genetic_algorithms.selections as selection
import evolutionary.genetic_algorithms.mutations as mutation
import evolutionary.genetic_algorithms.crossovers as crossover
import evolutionary.genetic_algorithms.replacements as replacement
import evolutionary.optim_functions as functions
from evolutionary import Population

parents = np.array([[1,2,3], [4,5,6], [7,8,9]])
children = np.array([[1,1,1]])
fitness = np.array([1,2,3])
print(replacement.parent_replace(parents, fitness, children,True))
