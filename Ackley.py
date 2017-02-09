def evaluate(population):
    """
    Python adaptation of the Ackley function by Manuel Lagunas.
    Feb 2017
    
    The Ackley function is widely used for testing optimization algorithms.
    It is characterized by a nearly flat outer region, and a large hole at the centre. The function poses a risk for optimization algorithms, particularly hillclimbing algorithms, to be trapped in one of its many local minima. (Source: https://www.sfu.ca/~ssurjano/ackley.html)
    """
    
    # Import numpy in case it was not done before
    import numpy as np
    
    # Using the recommended values in https://www.sfu.ca/~ssurjano/ackley.html
    a = 20.0
    b = 0.2
    c = 2 * np.pi
    
    # Get the size of our population
    n = float(len(population))
    
    # Initialize vars
    firstSum = 0.0
    secondSum = 0.0
    
    # Compute the sums on the population
    for i in population:
        firstSum += i**2.0
        secondSum += np.cos(2.0*c*i)

    # Return the function
    return -a*np.exp(-b*np.sqrt(firstSum/n)) - np.exp(secondSum/n) +  a + np.e
