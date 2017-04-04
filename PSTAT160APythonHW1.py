"""
This is PSTAT 160A HW #1 by Nathan Fritter
Professor: Hohn
Section: 10:00 am - 10:50 am 
TA: Mousavi
"""

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

def main():

    
    # Part A
    # Generate 1000 uniform random variables
    # Good thing numpy has a built in function for that!
    
    n = 1000
    uniform_rv = np.random.uniform(0, 1, n)

    # Part B: Written separately and turned in as PDF

    # Part C
    # Using result from Part B, the inverse function Fx^-1 is: 
    # -5 * ln(1 - x)
    # Now let's generate 1000 exponential random variables using 
    # the inverse function with the uniform random variables as input
    # The second part of Part C is written separately with Part B

    exp_rv = -5 * np.log(1 - (uniform_rv))
        
    # Part D
    # Print out sample mean and sample variance of the exponential
    # random variables then plot histogram
    # Briefly explain why you can tell from histogram that these
    # variables are exponential random variables
    
    exp_mean = np.mean(exp_rv)
    print("The sample mean of the exponential random variables is: %d" % exp_mean)
    exp_var = np.var(exp_rv)
    print("The sample variance of the exponential random variables is: %d" % exp_var)

    num_bins = 16
    n, bins, patches = plt.hist(exp_rv, 
                                bins = num_bins, 
                                normed = True, 
                                facecolor = 'red', 
                                alpha = 0.6)
    plt.title('1000 Exponential Random Variables')
    plt.show()
    # As you can see from the outputted graph, the data clearly exhibits 
    # exponential decay behavior because the points at the far left are 
    # the highest, and then the values decrease rapidly moving left to right

main()
