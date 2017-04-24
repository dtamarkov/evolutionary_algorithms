from __future__ import division

import numpy as np

from evolutionary import EAL, optim_functions as functions

seeds = np.array([82634, 16345, 12397, 84567, 34523, 65831, 40986, 8652, 12345, 98765, 19285, 97531])

# print functions.Schwefel().evaluate(np.ones(10)*420.9687)


gga = EAL(
    goal = 10**-4,
    minimization=False,
    problem=functions.Schwefel,
    n_dimensions=10,
    n_population=200,
    n_iterations=1000,
    n_children=200,
    xover_prob=0.8,
    mutat_prob=0.05,
    selection='tournament',
    crossover='one-point',
    mutation='gga-mutation',
    replacement='generational',
    grid_intervals=20,
    alpha_prob=0.9,
    control_alpha=10**-2,
    control_s=6
)

gga.fit(type="gga", iter_log=100, seed=seeds[1])

