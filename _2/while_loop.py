#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    while_loop.py  |  Control flow, iterators/loops
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    + what's a while loop?

"""

# %% what's a while loop?

"""
Whereas a for loop is established for a fixed number of iterations, statements
within the block of a while loop execute only and as long as some condition
holds (Hill, 2015).

Possible application of the while loop:

    - computer simulation of social and economic systems
      - in fact, analysts are frequently interested in appreciating the
        convergence of a system toward some equilibrium
      - once the equilibrium has been achieved, the analyst wants to stop the
        computer simulation
"""

# backbone of a while loop
# --+ starting state
i = 0
# --+ while loop
while i < 10:
    i +=1                  # we update the starting state
    print('The current state is {}'.format(i))
