"""
This is the Python Project
For PSTAT 160A
Professor Hohn
TA: Mousavi
"""

from __future__ import division
import numpy as np

def part_d():
    # Simulate 1000 sample paths of the Markov chain computed in the previous parts
    # And find the probability that the epidemic will die out in the next 2 years.
    num_sim = 1000
    current_sim = 0
    time_of_epidemic = []
    more_than_half = []
    days_in_two_years = 365 * 2
    less_than_two_years = 0
    # The state space is as it is below
    # Because the number of infected either
    # Decreases by 1, remains the same or increases by 1
    # In our Markov chain
    # Let the left most state represent i - 1
    # The middle represent i
    # And the right most represent i + 1
    state_space = [-1, 0, 1]

    # We will put together probabilities based on following parameters
    N = 100
    beta = 0.001
    b = gamma = 0.0025

    # Begin simulation
    while current_sim < num_sim:
        # Reset stuffs
        # Keep counter of length of time that 50% or more teachers are infected
        time_more_than_half = 0
        time_steps = 0
        initial_infected = i = 25

        while i > 0:
            prob_dec = (b + gamma) * i
            prob_inc = ((beta * i) * (N - i) / N) 
            prob_stay_same = 1 - (prob_dec + prob_inc) 
            transition_probs = [prob_dec, prob_stay_same, prob_inc]

            # Choose how much transition state changes by
            transition_change = np.random.choice(a = state_space, p = transition_probs)
            i += transition_change
            S = N - i

            # Increment counts 
            time_steps += 1
            # If we get to over 50% infected take note of it
            if i >= 50:
                time_more_than_half += 1
                # We don't really get here do we
                print("More than 50 percent are infected")
                print(i)

        # Keep track of time steps and time where more than half of teachers infected
        time_of_epidemic.append(time_steps)
        more_than_half.append(time_more_than_half)

        # If the epidemic lasts less than two years take note
        if time_steps < days_in_two_years:
            less_than_two_years += 1
        # Increment count
        current_sim += 1
        if current_sim % 50 == 0:
            print("Current simulation is %d" %current_sim)

    print("Showing duration of epidemics for each simulation:")
    print(time_of_epidemic)
    print("\nPart D: The probability that the epidemic will die out within 2 years is %.2f" %(less_than_two_years / 1000))

    # Call Part E and F from here
    part_e(time_of_epidemic)
    part_f(more_than_half)

def part_e(extinction_times):
    # Find the expected duration of the epidemic
    # By taking the average of the duration times of the epidemic
    N = 1000 # Number of simulations
    sum_times = sum(extinction_times)
    exp_time_of_epidemic = sum_times / N

    print("\nPart E: The expected duration of the epidemic is %.2f days" % exp_time_of_epidemic)

def part_f(more_than_half_times):
    # Calculate expected time that 50%+ of teachers are infected
    # By taking average of the duration that 50%+ of teachers are infected
    sum_times = sum(more_than_half_times)
    exp_time_more_than_half = sum_times / 1000

    print("\nPart F: The expected duration where 50 percent or more of the teachers are infected is %.2f days" % exp_time_more_than_half)

part_d()
