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
import seaborn as sns

parents = np.array([[1.,2.,3.], [4.,5.,6.], [7.,8.,9.]])
children = np.array([[1.,1.,1.]])
fitness = np.array([1.,2.,3.])
fitness_c = np.array([4.])
upper =  np.array([[32.,32.,32.],[32.,32.,32.],[32.,32.,32.]])
lower = upper * (-1)

# print(np.vstack((parents,children)))
# parents = replacement.elitist(parents, fitness, children, fitness_c, 4)
# print ("Input", parents)
# children = crossover.blend(parents, 0.8, upper, lower)
# print( "Blend xover", children)
# children = mutation.uniform(children, 0.1, upper, lower)
# print ("Uniform mut.", children)
#
#  mydictionary = {'mean': True, 'best':True, 'worst':True}
# print ([key for key in mydictionary])

# color_a = sns.color_palette("husl", 5)
# for i in range(5):
#     plt.plot(np.cumsum(np.random.randn(10*i,1*i)), color=color_a[i])
# plt.show()

a = np.array([])
b = np.array([-18.69882179])
print (np.hstack((a,b)))

