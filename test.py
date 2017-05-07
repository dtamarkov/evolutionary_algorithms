from __future__ import division

import numpy as np

from evolutionary import EAL, optim_functions as functions
from evolutionary import ga_tools as ga_tools
seeds = np.array([82634, 16345, 12397, 84567, 34523, 65831, 40986, 8652, 12345, 98765, 19285, 97531])

gga = EAL(
    goal = 10**-4,
    minimization=True,
    n_dimensions=10,
    n_population=200,
    n_iterations=2000,
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
    control_s=6,
    tournament_competitors=3,
    tournament_winners=1
)

# res = [None]*10
# for i in range(len(res)):
#     res[i] = ga_tools.geometric(3) - ga_tools.geometric(3)
# print(res)
gga.fit(ea_type="gga",
        problem=functions.Ackley, bounds=[-10, 10],
        iter_log=100,
        seeds=seeds[0:4])

