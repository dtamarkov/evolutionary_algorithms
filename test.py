from __future__ import division

import numpy as np

parents = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
children = np.array([[1., 1., 1.]])
fitness = np.array([1., 2., 3.])
fitness_c = np.array([4.])
upper = np.array([[32., 32., 32.], [32., 32., 32.], [32., 32., 32.]])
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

# a = np.array( [[1,2,3],[1,2,3]])
# b = np.array([[4,1,2],[4,1,2]])
# # print (np.hstack((a,b)))
# print np.minimum.reduce([a,b])
from evolutionary.ga import EAL

a = EAL(
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

b = EAL(
    seed=82634,
    minimization=False,
    n_dimensions=10,
    n_population=100,
    n_iterations=1000,
    n_children=100,
    xover_prob=0.8,
    mutat_prob=0.2,
    selection='tournament',
    crossover='blend',
    mutation='gaussian',
    replacement='elitist'
)
b.es(iter_log=100)
# a.ga(iter_log=50)
