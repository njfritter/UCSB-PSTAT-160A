"""
This is the second Python HW for PSTAT160A
By: Nathan Fritter
Section: W 10:00 am - 10:50 am
TA: Mousavi
"""

# Import necessary libraries
from __future__ import division
import numpy as np


# Part B
def gen_rand_var():
    
    print("\nThis is the output for Part B:")
    # Generate N Bernoulli random variables
    # Minimum premium amount calculated: 104.935
    N = 10000
    prem = 104.935
    claim_amt = 1000
    prob = 0.1
    ber_rand_var = np.random.binomial(n = N, p = prob)

    # Print the amount of claims in the simulation
    num_claims = np.mean(ber_rand_var)
    print("The amount of accident claims were: %d" % num_claims)
    # Print whether or not the company went bankrupt
    went_bankrupt = N * prem < claim_amt * num_claims
    if went_bankrupt:
        print("The company went bankrupt")
    else:
        print("The company survived")

# Part C
def run_sim():
    print("\nThis is the output for Part C:")
    # Run 1000 simulations of Part B
    # To do this we need the below values
    num_sim = 1000
    prem = 104.935
    claim_amt = 1000
    prob = 0.1
    N = 10000
    # Simulate 1000 trials of the company either going bankrupt or not
    sim_rand_var = np.random.binomial(N, prob, num_sim)
    
    # Find how many times the company goes bankrupt
    times_bankrupt = sum(sim_rand_var * claim_amt > N * prem)
    prob_bankrupt = times_bankrupt / num_sim
    print("Number of times company went bankrupt: %d" % times_bankrupt)
    print("The company went bankrupt with a probability of: %.2f" % prob_bankrupt)
    
    

# Run functions
gen_rand_var()
run_sim()
