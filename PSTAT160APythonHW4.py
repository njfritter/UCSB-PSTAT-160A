"""
This is Python HW #4
By: Nathan Fritter                                                                                                                                                                  Professor Hohn                                                                                                                                                                      Section: W 10:00 - 10:50 am                                                                                                                                                         TA: Mousavi
"""

from __future__ import division
import numpy as np
import math

def part_c():
    # Taken from HW 3
    num_sim = 10000
    current_sim = 0
    sim_paths = []
    print("\nRunning 10000 simulations of Xn from n = 0 to infinity")
    while current_sim < num_sim:

        # Taken from Part B                                                                                                                                                          
        # Create necessary lists and counters for part c                                                                                                                             
        state_space = [0, 1, 2, 3, 4, 5]
        song_list = [1, 2, 3, 4, 5]
        songs_listened_to = []
        num_unique_songs = 0
        time_steps = 0

        # Begin while loop                                                                                                                                                           
        while num_unique_songs < 5:
            current_song = np.random.choice(song_list)
            time_steps += 1

            # To take care of initial conditions                                                                                                                                     
            if num_unique_songs == 0:
                num_unique_songs += 1
                songs_listened_to.append(current_song)
            # If we have already heard the song, increment and move on                                                                                                               
            if current_song in songs_listened_to:
                continue
            # Or else append song number to list                                                                                                                                     
            else:
                songs_listened_to.append(current_song)
                num_unique_songs += 1

        # After each simulation finishes                                                                                                                                             
        current_sim += 1

        # Add number of time steps to the list                                                                                                                                       
        sim_paths.append(time_steps)


    # Taken from HW 3
    print("\nEstimating probabilities that all songs are heard at time n = 5, 6, 7, .... using values generated from Part C\n")
    # Now to find probabilities                                                                                                                                                      
    exp_val = 0
    num_sim = 10000
    n = 5
    probs = []
    while n < 21:
        num_times_correct = sim_paths.count(n)
        prob = num_times_correct / num_sim
        print("The probability of playing the last unique song on time step number %d is: %.2f" % (n, prob))
        probs.append(prob)
        exp_val += (n * prob)
        n += 1

    print("/nPart C: My estimate of the expected number of times steps to get to 5 unique songs from 0 is: %.2f" % exp_val)

def part_d():
    # Taken from HW 3                                                                                                                                                                
    num_sim = 10000
    current_sim = 0
    sim_paths01 = []
    sim_paths02 = []
    sim_paths03 = []
    sim_paths04 = []
    while current_sim < num_sim:

        # Taken from Part B
        # Create necessary lists and counters for part c
        
        state_space = [0, 1, 2, 3, 4, 5]
        song_list = [1, 2, 3, 4, 5]
        songs_listened_to = []
        num_unique_songs = 0
        time_steps = 0

        # Begin while loop
        while num_unique_songs < 5:
            current_song = np.random.choice(song_list)
            time_steps += 1

            # If we've already listened to the song
            if current_song in songs_listened_to:
                continue
            # Or else append song number to list
            else:
                songs_listened_to.append(current_song)
                num_unique_songs += 1
                
                # Add time step number to appropriate list
                if num_unique_songs == 1:
                    sim_paths01.append(time_steps)
                if num_unique_songs == 2:
                    sim_paths02.append(time_steps)
                if num_unique_songs == 3:
                    sim_paths03.append(time_steps)
                if num_unique_songs == 4:
                    sim_paths04.append(time_steps)

        # Increment count
        current_sim += 1
    
    # Print out estimates of E0[Tk] for k = 1, 2, 3, 4
    
    # k = 1
    avg01 = (sum(sim_paths01) / float(len(sim_paths01)))
    print("Our estimated expected value for E0[T1] is: %.2f" % avg01)

    # k = 2
    avg02 = (sum(sim_paths02) / float(len(sim_paths02)))
    print("Our estimated expected value for E0[T2] is: %.2f" % avg02)

    # k = 3
    avg03 = (sum(sim_paths03) / float(len(sim_paths03)))
    print("Our estimated expected value for E0[T3] is: %.2f" % avg03)
    
    # k = 4
    avg04 = (sum(sim_paths04) / float(len(sim_paths04)))
    print("Our estimated expected value for E0[T4] is: %.2f" % avg04)


part_c()
part_d()
