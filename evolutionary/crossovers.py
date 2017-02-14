"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""

import numpy as np

def simple(parents):
    """
    It recombines a pair of parents to generate their childrens.
    In order to do so it splits each parent in 2 halfs from the crossover point,
    then it combinates the halfs of each of them to generate two new children
    """
    
    # Check the input var
    assert len(parents)==2
    
    crossover_point = np.random.randint(len(parents[0]))
    
    # split parents in 2 parts by the crossover point
    parent_1 = np.hsplit(parents[0], [crossover_point])
    parent_2 = np.hsplit(parents[1], [crossover_point])
    
    # recombine to generate their children
    child_1 = np.hstack((parent_1[0], parent_2[1]))
    child_2 = np.hstack((parent_2[0], parent_1[1]))
    
    return np.array([child_1, child_2])


def simple_permutation(parents):
    """
    It recombines a pair of parents to generate their childrens.
    In order to do so it splits each parent in 2 halfs from the crossover point,
    then it combinates the halfs of each of them to generate two new children.
    Now the representation of each parent is a permutation of n elements, where n
    is len(parents[i]).
    """
    
    # Check the input var
    assert len(parents)==2
    
    def add_parent(new_parent, parent):
        """
        Private auxiliary function to minimize the code.
        It appends to a given parents the values that it doesn't
        contain yet from the other parent's tail.
        """
        return np.hstack((new_parent, [x for x in parent if x not in new_parent]))     

    crossover_point = np.random.randint(len(parents[0]))

    # split parents in 2 parts by the crossover point
    parent_1 = np.hsplit(parents[0], [crossover_point])
    parent_2 = np.hsplit(parents[1], [crossover_point])
    
    # recombine to generate their children
    child_1 = add_parent(parent_1[0], np.hstack((parent_2[1], parent_2[0])))
    child_2 = add_parent(parent_2[0], np.hstack((parent_1[1], parent_1[0])))
    
    # Return the generated children as a np array
    return np.array([child_1, child_2])