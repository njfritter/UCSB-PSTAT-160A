# UCSB-PSTAT-160A
## Stochastic Processes w/ Discrete Variables (a.k.a. Markov chains)
This repo is dedicated to showing the coding assignments/reports I completed during the class PSTAT 160A taught in Fall 2016 by Professor Hohn at UCSB.
I will also be including the pdf documents of the assignments where I was asked to extracted specific answers from the problem in question.
All credit goes to UCSB and its affiliates.

## What are Stochastic Processes (and Random Variables, too)?

Stochastic processes are collections of things called random variables (RV's) indexed by time.
A random variable is something that takes on certain values with varying probabilities;
the collection of the variables values and their corresponding probabilities are known as "probability distributions". 

RV's are divided mainly into two categories: discrete and continuous. This repo is dedicated to the properties and results of stochastic processes using discrete random variables. I have another repo dedicated to the properties/results of continuous stochastic processes.

Discrete random variables take on discrete values (big surprise) that have various probabilities of occurring. 

The simplest example of a discrete RV would be 1 fair coin flip; we have to say fair in order for P(heads) = P(tails) = 0.5. Here the two possible outcomes of the random variable are "Heads" and "Tails", each with probabilities of 0.5 that they occur.

There can be more complicated examples of RVs such as:
-The number of heads flipped in 10 fair coin flips
-The number of people entering a store per hour
-The number of trials until the first desired outcome

## Classifying Discrete Stochastic Processes
We can divide up the different types of stochastic processes based on their:
-State space
-Time indexing (which can be discrete or continuous)

For discrete stochastic processes, the possible states (values) of the process are contained within  a finite "state space"; and the probability of moving from one state to another is constant throughout the process. 

These types of situations are excellent for modeling repetitive processes in real life scenarios (see below)

## Real Life Applications
There are many real life applications with respect to Markov chains:
-Weather ("Sunny", "Rainy", "Cloudy", etc.)
-Number of customers entering/leaving a store
-Tracking clicking patterns of online customers ("Main Page", "About Us", "Purchase", etc.)
-Etc. 

## Putting it All into Context

For example, if we wanted to model the number of customers at the liquor store you own at time t, we the state space would consist of the natural number set (0, 1, 2, ... infinity); realistically the process has a very low probability of reaching extremely high numbers, but they are included in the process nonetheless. Let Xt represent the number of customers in the store at any time t. 
Every stochastic process has an initial state (represented by X0) as well.  

Starting at the beginning of the day our process takes the value of zero. Let's say that we have different probabilities depending on whether the day will be expected to be busy, normal, or slow. 

Now let us declare the probabilities of this process: 

For a slow day:
-P(increase by 1) = 0.2
-P(decrease by 1) = 0.5
-P(stay the same) = 0.3

For a normal day:
-P(increase by 1) = (1/3)
-P(decrease by 1) = (1/3)
-P(stay the same) = (1/3)

For a busy day:
-P(increase by 1) = 0.5
-P(decrease by 1) = 0.2
-P(stay the same) = 0.3

These probabilties are likely not realistic but still serve to illustrate the process. Now beginning at zero, we can model how the process/day will unfold progressing through different time units. 

Another example: If we had a fair coin and wanted to model the difference between the number of heads tossed and tails tossed at any time t, we could have a state space that consisted of the natural number set (0, 1, 2, ... infinity); realistically the process has a very low probability of reaching extremely high numbers, but they are included in the process nonetheless. Let Xt represent (number of heads tossed) - (number of tails tossed) at any time t. 

Now let us declare the probabilities of this process: 
-P(increase by 1) = 0.5
-P(decrease by 1) = 0.5

This example may be a bit more complicated to get, but is certainly much more realistic and can be modeled easily. 

Also, in general we are not restricted to simply moving sequentially between states; a process could move from state 1 to state 4, from state 2 to state 10, depending on how the process is defined.  

Through the concepts learned in this class, we were able to answer various questions such as:
-What is the long run probabilities of being in each state?
-What is the probability of being in state 1 at time 1 and state 2 at time 5?
-What is the probability that the process goes to state 4 before state 2?

More will be added on these subjects later.

## Types of Stochastic Processes
In PSTAT 160A, we covered two types of general stochastic processes:

### Markov Chains

Markov Chains are stochastic processes which have discrete time indices & discrete state spaces.
Each state of a Markov Chain depends only on the previous state (e.g. X2 only depends on X1, etc.)

For every current state, we define a probability the random process moves into a different state (for every possible resultant state) by the next unit of time. 

We call these probabilities transition probabilities. For every initial state, the sum of transition probabilities must equal 1 (the probability of going to all possible different states.

### Poisson Process

A Poisson Process is a stochastic process with continuous time indices & discrete state space.
This is a type of counting process; a Poisson Process counts the number of events that have occurred at time t.

Ex) The number of earthquakes in California

By the nature of a counting process, a Poisson Process can only increase in value.
The number of events in any time interval is a Poisson RV. 
The number of events in any time intervals of similar length are identically and independently distributed Poisson random variables.
The time between any two events (called the waiting times or interval arrival times) are identical and independent Exponential RVs.