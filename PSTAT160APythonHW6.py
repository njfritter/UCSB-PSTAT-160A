"""                                                                                                                                                                                 This is the fifth Python HW                                                                                                                                                         By: Nathan Fritter                                                                                                                                                                  
Professor Hohn                                                                                                                                                                      
Section: W 10:00 - 10:50 am                                                                                                                                                         
TA: Mousavi                                                                                                                                                                         """

# import libraries
from __future__ import division
import numpy as np
from numpy import linalg as LA

our_array = np.array([[1/3, 1/2, 1/6, 0], [1/2, 1/8, 1/4, 1/8], [1/4, 1/2, 1/8, 1/8], [0, 0, 1/2, 1/2]])
print("\nOur transition matrix is: \n{}".format(our_array))

def part_b():
    # Raise matrix to the 100th power
    product = LA.matrix_power(our_array, 100)
    print("\nPart B: The result of raising our transition matrix to the 100th power is: \n{}".format(product))

def part_c():
    # Some counters
    sim_paths_1 = []
    sim_paths_2 = []
    sim_paths_3 = []
    sim_paths_4 = []
    state_space = [1, 2, 3, 4]

    # This state space below is for indexing purposes
    indexed_state_space = [0, 1, 2, 3] 
    probs_1 = [1/3, 1/2, 1/6, 0]
    probs_2 = [1/2, 1/8, 1/4, 1/8]
    probs_3 = [1/4, 1/2, 1/8, 1/8]
    probs_4 = [0, 0, 1/2, 1/2]
    print("\nPart C: Running 10000 simulations of Xn from n = 0 to infinity")
    
    # Go through each state in state space and calculate expected value of returning to state
    # We will used an indexed state space in order to make it easier for Python
    for indexed_state in indexed_state_space:
        print("\nCalculating for state %d" % (indexed_state + 1))
        num_sim = 10000
        current_sim = 0

        while current_sim < num_sim:
            
            # Create counter and flag                                                                                             
            time_steps = 0
            returned = False
            
            # Declare that indexed state is current state
            current_state = indexed_state
                
            # Run the process
            while returned == False:
                
                # Make a new counter to hold previous state
                prev_state = current_state
                    
                # Make a choice
                current_state = np.random.choice(indexed_state_space, p = our_array[prev_state, ])
                time_steps += 1

                # Check if we have returned; if not we will keep going until so
                if current_state == indexed_state:
                    returned == True
                    # For some reason the loop won't terminate even with the flag condition
                    # Adding a break below
                    break

            # Append our data once the simulation ends
            state = indexed_state + 1

            if state == 1:
                sim_paths_1.append(time_steps)
            if state == 2:
                sim_paths_2.append(time_steps)
            if state == 3:
                sim_paths_3.append(time_steps)
            if state == 4:
                sim_paths_4.append(time_steps)

            # Lastly increment count
            current_sim += 1
            if current_sim % 1000 == 0:
                print("Current sim is %d\n" % current_sim)
        

    # Calculate expected value of return time for each i in S
    exp_val_1 = sum(sim_paths_1) / len(sim_paths_1)
    exp_val_2 = sum(sim_paths_2) / len(sim_paths_2)
    exp_val_3 = sum(sim_paths_3) / len(sim_paths_3)
    exp_val_4 = sum(sim_paths_4) / len(sim_paths_4)

    # Print results
    print("The expected return time for i = 1 starting at i = 1 is: %.2f" % exp_val_1)
    print("The expected return time for i = 2 starting at i = 2 is: %.2f" % exp_val_2)
    print("The expected return time for i = 3 starting at i = 3 is: %.2f" % exp_val_3)
    print("The expected return time for i = 4 starting at i = 4 is: %.2f" % exp_val_4)
    
    inv_dist_1 = (1 / exp_val_1)
    inv_dist_2 = (1 / exp_val_2)
    inv_dist_3 = (1 / exp_val_3)
    inv_dist_4 = (1 / exp_val_4)

    # The sum of the individual invariant distributions for each state may not equal exactly 1
    # Due to round off error
    print("\nThis makes the invariant distribution the following:")
    print("Pi1 = %.2f" % inv_dist_1)
    print("Pi2 = %.2f" % inv_dist_2)
    print("Pi3 = %.2f" % inv_dist_3)
    print("Pi4 = %.2f" % inv_dist_4)
                    
def part_d():

    # Counters and lists    
    sim_paths_1 = []
    sim_paths_2 = []
    sim_paths_3 = []
    sim_paths_4 = []
    state_space = [1, 2, 3, 4]
    num_return_times = []
    # This state space below is for indexing purposes                                                                                                                              
    indexed_state_space = [0, 1, 2, 3]
    probs_1 = [1/3, 1/2, 1/6, 0]
    probs_2 = [1/2, 1/8, 1/4, 1/8]
    probs_3 = [1/4, 1/2, 1/8, 1/8]
    probs_4 = [0, 0, 1/2, 1/2]
    print("\nPart D: Running 100000 simulations of Xn from n = 0 to infinity")

    # Go through each state in state space and calculate expected value of returning to state                                                                                        
    # We will used an indexed state space in order to make it easier for Python                                                                                                      
    for indexed_state in indexed_state_space:
        print("\nCalculating for state %d" % (indexed_state + 1))
        num_sim = 100000
        current_sim = 0
        num_times_returned = 0

        while current_sim < num_sim:
            # Create counter 
            time_steps = 0
            # Declare that indexed state is current state                                                                                                                           
            current_state = indexed_state
            
            # Make a new counter to hold previous state                                                                                                                          
            prev_state = current_state
            
            # Make a choice                                                                                                                                                      
            current_state = np.random.choice(indexed_state_space, p = our_array[prev_state, ])
            time_steps += 1

            # Check if we have returned; if not we will keep going until so                                                                                                      
            if current_state == indexed_state:
                num_times_returned += 1

            # Append our data once the simulation ends                                                                                         
            current_sim += 1

        # Keep track of return times
        num_return_times.append(num_times_returned / 100000)
    # Print out results
    print("\nThe long term frequencies are as follows: {}".format(num_return_times))



# Run functions    
part_b()
part_c()
part_d()
