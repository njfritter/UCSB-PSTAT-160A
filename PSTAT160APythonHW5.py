"""
This is the fifth Python HW
By: Nathan Fritter
Professor Hohn
Section: W 10:00 - 10:50 am
TA: Mousavi
"""

# Import necessary libraries 
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def part_b_and_c():
    
    num_sim = 10000
    current_sim = 0
    sim_paths_2 = []
    sim_paths_3 = []
    # Counters for the number of times the process was absorbed
    absorbed_2 = 0
    absorbed_3 = 0

    print("\nPart B and C: Running 10000 simulations of Xn from n = 0 to infinity")
    while current_sim < num_sim:

        # Create lists and counters
        time_steps = 0
        state_space = [1, 2, 3, 4]
        A = [1, 4]
        probs_2 = [1/2, 1/8, 1/4, 1/8]
        probs_3 = [1/4, 1/2, 1/8, 1/8]
        
        # Flags for starting at 2 or three
        start_at_2 = False
        start_at_3 = False
        
        # Pick something randomly
        current_state = np.random.choice(state_space)
        print("First state is %d" % current_state)

        # If already in absorption states, end
        if current_state in A:
            print("Begins in an absorbed state\nAbsorbed\n")
            continue

        # As long as the process has not been absorbed, continue
        while current_state not in A:
            if current_state == 2:
                start_at_2 = True
                current_state = np.random.choice(a = state_space, p = probs_2)
                print("New state is {}").format(current_state)
                time_steps += 1
            if current_state == 3:
                start_at_3 = True
                current_state = np.random.choice(a = state_space, p = probs_3)
                print("New state is {}").format(current_state)
                time_steps += 1

        # Add number of time steps to the appropriate list
        if start_at_2:
            sim_paths_2.append(time_steps)
        if start_at_3: 
            sim_paths_3.append(time_steps)
        
        # See if the process ended up being absorbed (every i in the state space will end up in A)
        # But let's check anyway
        if start_at_2: 
            if current_state in A:
                absorbed_2 += 1
                print("Absorbed")
        
        if start_at_3:
            if current_state in A:
                absorbed_3 += 1
                print("Absorbed")

        # Simulation done
        print("Simulation done\n")
        current_sim += 1            


    # Part B
    # Find the expected time until absorption for each i in the state space
    # E1[TA] = E4[TA] = 0 because it starts in the absorption states
    exp_val_1 = 0
    exp_val_4 = 0
    
    # Find E2[TA] and E3[TA]
    exp_val_2 = sum(sim_paths_2) / len(sim_paths_2)
    exp_val_3 = sum(sim_paths_3) / len(sim_paths_3)

    print("\nThe expected time until absorption for i = 1 is: %.2f" % exp_val_1)
    print("\nThe expected time until absorption for i = 2 is: %.2f" % exp_val_2)
    print("\nThe expected time until absorption for i = 3 is: %.2f" % exp_val_3) 
    print("\nThe expected time until absorption for i = 4 is: %.2f" % exp_val_4) 

    # Part D
    # Find] the probability that at each i, if the process starts in i
    # The process will eventually be absorbed
    # P1(A) and P4(A) are 1, because they started in the absorption states
    prob_1 = 1
    prob_4 = 1

    # Find P2(A) and P3(A)
    prob_2 = absorbed_2 / len(sim_paths_2)
    prob_3 = absorbed_3 / len(sim_paths_3)
    
    print("\nThe probability of absorption for i = 1 is: %.2f" % prob_1)
    print("\nThe probability of absorption for i = 2 is: %.2f" % prob_2)
    print("\nThe probability of absorption for i = 3 is: %.2f" % prob_3)
    print("\nThe probability of absorption for i = 4 is: %.2f" % prob_4)

part_b_and_c()








"""
# Taken from here http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = np.random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w >= r:
         return c
      upto += w
   assert False, "Shouldn't get here"
"""
