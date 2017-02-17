"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

class Population(object):
    """
    Chromosome is an object that has the chromosomes and sigma.
    It is used in evolutionary algorithms.
    The chromosomes is the n-dimensional array that will be evaluated by the fitness function.
    Regarding the evolutionary-strategy followed sigma will be None or an array of values
    """
    
    def __init__(self, chromosomes=None, sigma=None):
        self.chromosomes = chromosomes
        self.sigma = sigma
    
    def chromosomes(self, chromosomes):
        self.chromosomes = chromosomes
        
    def set_sigma(self, sigma):
        self.sigma = sigma