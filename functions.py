# Import numpy in case it was not done before
import numpy as np

#################################################################
class Function(object):
    """
    Python adaptation of a group of functionf by Manuel Lagunas.
    The functions are obtained from https://www.sfu.ca
    Feb 2017
    """
    def __init__(self, name):
        self.name = name
    
    def evaluate(self, population):
        # Returns the value of the function for a population
        raise NotImplementedError("Subclass must implement abstract method")
        
    def plot(self, lower, upper, samples):
        """
        2dplot the function considering a lower and upper bounds and the number of samples
        to sample between them.
        """
        import matplotlib.pyplot as plt
        
        # Create the array of values between the bounds and calculate its fitness
        x = np.linspace(lower, upper, samples)
        fitness = np.empty(0)
        for i in x:
            fitness = np.append(fitness, self.evaluate(np.array([i])))
        
        # Plot the values and the fitness
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.plot(x, fitness)
        fig.suptitle(self.name, fontsize=14)
        ax.set_xlabel("X")
        ax.set_ylabel("Fitness")        

#################################################################
class Ackley(Function):
    """    
    The Ackley function is widely used for testing optimization algorithms.
    It is characterized by a nearly flat outer region, and a large hole at the centre. 
    The function poses a risk for optimization algorithms, particularly hillclimbing algorithms, 
    to be trapped in one of its many local minima. 
    (Source: https://www.sfu.ca/~ssurjano/ackley.html)
    """
    def __init__(self, a=False, b=False, c=False):
        """
        Initialize the Ackley class with the values of a, b and c
        """
        super(self.__class__, self).__init__("Ackley")
        self.a = 20 if not a else a
        self.b = 0.2 if not b else b
        self.c = 2 * np.pi if not c else c
    
    def evaluate(self, population):
        """
        Returns the fitness of a population using the Ackley function.
        Population has to be a numpy array for this method to work.
        """
        # Check the var type of the population
        assert str(type(population)) == "<type 'numpy.ndarray'>"
        
        # Initialize vars
        firstSum = 0.0
        secondSum = 0.0 
        n = float(len(population))
        
        # Compute the sums on the population
        for i in population:
            firstSum += i**2.0
            secondSum += np.cos(2.0*self.c*i)

        # Return the function
        return -self.a*np.exp(-self.b*np.sqrt(firstSum/n)) - np.exp(secondSum/n) +  self.a + np.e
    
    def plot(self, lower=-32, upper=32, samples=1000):
        """
        Makes a 2d plot using the parent class.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        super(self.__class__, self).plot(lower, upper, samples)

#################################################################        
class Griewank(Function):
    """
    The Griewank function has many widespread local minima, which are regularly distributed.
    D dimensional function
    Global minima at x* = (0, .. 0)
    (Source: https://www.sfu.ca/~ssurjano/griewank.html)
    """
    def __init__(self):
        super(self.__class__, self).__init__("Griewank")
    
    def evaluate(self, population):
        # Initialize vars
        add = 0.0
        mult = 1.0
        
        # Compute the sum and the multiplication
        for i in range(len(population)):
            add += float(population[i])**2
            mult *= np.cos(float(population[i])/np.sqrt(i+1))
        
        # Return the value of the function
        return 1 + add/4000 - mult
    
    def plot(self, lower=-600, upper=600, samples=1000):
        """
        Makes a 2d plot using the parent class.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        super(self.__class__, self).plot(lower, upper, samples)
        
#################################################################
class Beale(Function):
    """
    The Beale function is multimodal, with sharp peaks at the corners of the input domain.
    2 Dimensional
    Global minima x = (3, 0.5)
    (Source: https://www.sfu.ca/~ssurjano/beale.html)
    """
    def __init__(self):
        super(self.__class__, self).__init__("Beale")
    
    def evaluate(self, population):
        # ensure population is 2 dimensiona
        assert len(population) == 2
        
        # Make sintax closer to the source
        x1 = population[0]
        x2 = population[1]
        
        # Compute the three parts of the function
        part1 = (1.5 - x1 + x1*x2)**2
        part2 = (2,225 - x1 + x1*x2**2)**2
        part3 = (2,625 - x1 + x1*x2**3)**2
        
        # Return the value of the function
        return part1 + part2 + part3
    
    def plot(self, upper=0, lower=0,  samples=0):
        print "Beale function is 2 dimensional, therefore, it cannot be displayed in a 2d plot"
        
#################################################################        
class Booth(Function):
    """
    Global minima at x* = (1,3)
    (Source: https://www.sfu.ca/~ssurjano/griewank.html)
    """
    def __init__(self):
        super(self.__class__, self).__init__("Booth")
    
    def evaluate(self, population):
        # ensure population is 2 dimensional
        assert len(population) == 2
        
        # Make sintax closer to the source
        x1 = population[0]
        x2 = population[1]
        
        # part1
        part1 = (x1 + 2*x2 - 7)**2
        part2 = (2*x1 + x2 - 5)**2
        
        # Return the value of the function
        return part1 + part2
    
    def plot(self, lower=-10, upper=10, samples=1000):
        print "Booth function is 2 dimensional, therefore, it cannot be displayed in a 2d plot"

#################################################################
class Rothyp(Function):
    """    
    The Rotated Hyper-Ellipsoid function is continuous, convex and unimodal. 
    It is an extension of the Axis Parallel Hyper-Ellipsoid function, 
    also referred to as the Sum Squares function.
    d dimensional.
    Global minima at x = (0,..,0)
    (Source: https://www.sfu.ca/~ssurjano/rothyp.html)
    """
    def __init__(self):
        super(self.__class__, self).__init__("Rothyp")
    
    def evaluate(self, population):
        """
        Returns the fitness of a population using the Rothyp function.
        Population has to be a numpy array for this method to work.
        """
        # Check the var type of the population
        assert str(type(population)) == "<type 'numpy.ndarray'>"
        
        # Initialize vars
        res_sum = 0.0
                        
        # Compute the sums on the population
        for i in range(len(population)):
            for j in range(i+1):
                res_sum += population[j]**2

        # Return the function
        return res_sum
    
    def plot(self, lower=-65.536, upper=65.536, samples=1000):
        """
        Makes a 2d plot using the parent class.
        It creates an array of samples between the upper and lower bounds
        and compute its fitness which will be plotted together.
        """
        super(self.__class__, self).plot(lower, upper, samples)