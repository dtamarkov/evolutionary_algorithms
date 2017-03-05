"""
    @Author: Manuel Lagunas
    @Personal_page: http://giga.cps.unizar.es/~mlagunas/
    @date: Feb - 2017
"""
import numpy as np
import seaborn as sns


class Logger(object):
    """
    Helper class which stores a group of numpy arrays that store the information
    of the evolutionary algorithm over each iteration. We can define the parameters
    to log by passing a dictionary to the Logger class. It also plots the stored values
    as a graph.
    """

    def __init__(self, logs):
        """
        Initializes the Logger object creating the dictionary of arrays
        to store the logged values
        :param logs:
        """
        self.values = {}
        self.log_size = 0
        for key in logs:
            self.values[key] = np.array([])

    def add_log(self, logs):
        """
        Adds a new item to log into the [values] dictionary
        :param logs:
        """

        # Validate that we do not add logs after the logging process
        # has started
        for key in self.values:
            assert (len(self.values[key]) == 0)

        # Add as many keys as given in logs
        for key in logs:
            assert (self.logs[key] == None)
            self.values[key] = np.array([])

    def log(self, values):
        """
        Stores the logged values into the [values] dictionary
        :param values:
        """
        for key in self.values:

            # If the element in value[key] is a number we transform it to an array
            if str(type(values[key])) == "<type 'numpy.float64'>":
                values[key] = np.array([values[key]])
            # We can only log one value at a time
            assert (len(values[key]) == 1)

            # add the value to the log of values
            self.values[key] = np.hstack((self.values[key], values[key]))
        self.log_size += 1

    def get_log(self, key):
        """

        :param key:
        :return: return one of the logged values
        """
        return self.values[key]

    def print_description(self, problem, dim, pop, iter, xover, mutat):
        """

        :param problem:
        :param dim:
        :param pop:
        :param iter:
        :param xover:
        :param mutat:
        :return:
        """

        print "-----------------------------------------"
        print "Problem to solve:", problem
        print "-----------------------------------------"
        print "Number of problem dimensions:", dim
        print "Size of the population:", pop
        print "Max. number of iterations:", iter
        print "Crossover probability:", xover
        print "Mutation probability:", mutat
        print "-----------------------------------------"

    def print_log(self, iteration):
        """
        print the result at the iteration [iteration] of the logged
                values. Useful to keep track of the process
        :param iteration:
        """
        res = "iteration " + str(iteration+1) + " ||"
        for key in self.values:
            res += " " + key + " " + str(self.values[key][iteration]) + " ||"
        print (res)

    def plot(self):
        """
        Draws a plot with the logged values
        :param logs:
        """

        # create a palette of colours with the number of keys
        keys = [key for key in self.values]
        palette = sns.color_palette("husl", len(keys))

        i = 0
        for key in self.values:
            sns.plt.plot(np.arange(0, self.log_size), np.abs(self.values[key]), color=palette[i])
            i += 1

        sns.plt.legend(keys, loc='upper right')
        sns.plt.show()
