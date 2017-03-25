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
from evolutionary import EAL, optim_functions as functions
#
a = EAL(
    seed=82634,
    minimization=False,
    problem=functions.Ackley,
    n_dimensions=10,
    n_population=100,
    n_iterations=1000,
    n_children=100,
    xover_prob=0.8,
    mutat_prob=0.05,
    selection='tournament',
    crossover='one-point',
    mutation='gga-mutation',
    replacement='elitist',
    grid_intervals=20,
    alpha_prob=0.9,
    control_alpha=10**-2,
    control_s=6
)
#
# b = EAL(
#     seed=82634,
#     minimization=False,
#     problem=functions.Ackley,
#     n_dimensions=10,
#     n_population=50,
#     n_iterations=1000,
#     n_children=50,
#     xover_prob=0.8,
#     mutat_prob=0.2,
#     selection='tournament',
#     crossover=None,
#     mutation='gaussian',
#     replacement='elitist'
# )
#
a.fit(type="gga", iter_log=100)
# b.fit(type="es", iter_log=50)
#

# if True:
#     prueba = 1
#
# prueba += 1
# print (prueba)

from evolutionary import tools

upper = np.ones(10) * 32
lower = np.ones(10) * -32
#
# aux_delta = np.array([(upper[0] - lower[0]) / 10])
# space_s = np.arange(np.floor(lower[0] / aux_delta[-1]), np.floor(upper[0] / aux_delta[-1])).astype(int)
# aux_s = space_s[np.random.randint(len(space_s))]
# aux_alpha = np.random.uniform(0, aux_delta)
#
# # Calculate taking into account that each dimension could have a different upper or lower bound
# for i in range(len(upper[1:])):
#     # Compute the delta value for the dimension and add it to the array of deltas
#     aux_delta = np.hstack((aux_delta, (upper[i] - lower[i]) / 10))
#
#     # Get the values of S according to delta
#     space_s = np.vstack(
#         (space_s, np.arange(np.floor(lower[i] / aux_delta[-1]), np.floor(upper[i] / aux_delta[-1])).astype(int)))
#     aux_s = np.hstack((aux_s, space_s[-1][np.random.randint(len(space_s[-1]))]))
#     # Sample the alpha values between 0 and delta from a uniform distribution
#     aux_alpha = np.hstack((aux_alpha, np.random.uniform(0, aux_delta[-1])))
#
# print aux_alpha
# print aux_delta
# print aux_s
# print space_s
# upper = np.array([32,32,32])
# lower = upper * -1
# p = tools.Population()
# print (p.gga_initialization(upper, lower, 10, 20))
# print (p.s)
# print (p.alpha)
# print (p.delta)

# print (a)
# print np.repeat(np.array([[1, 2, 3]]), 10, axis=0)

# a = np.array([1.,2.,3.,4.])
# b = np.array([4.,3.,2.,1.])
# print (a > b)
# a[a>2] -= b[a>2]
# print (a)
# aux_s = np.random.randint(np.array([0,0]), np.array([1,1]))