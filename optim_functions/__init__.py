# Make possible the sintax:
# from optim_functions import module
from ackley import Ackley
from griewank import Griewank
from beale import Beale
from booth import Booth
from rothyp import Rothyp
from forrester import Forrester
from matyas import Matyas

# Make possible the sintax:
# from optim_functions import *
__all__ = ["Ackley", "Griewank", "Beale", "Booth", "Rothyp", "Forrester", "Matyas"]