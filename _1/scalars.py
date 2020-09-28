#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    scalars.py  |  Python objects
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    + scalar objects
      - integers
      - floats
      - Boolean values
      - None

"""

# %% examples of scalar objects

# example of integer
I = 2

# example of float
F = 0.5

# example of Boolean
'''
!! Don't forget !!: Capitalize the first letter of a Boolean value expression, True or False. Don't include the text between parentheses – that makes the object a string
'''
B = True

# ... and the 'None' type
None

# %% operators involving scalar objects

# operators on objects of type 'int' and 'float'? There we go:
# --+ sum; it returns an int if addends are int, float otherwise
I + F
# --+ product; ibidem - it returns an int if both objects are of type int
I * F
# --+ division; ibidem - it gives an error if F = 0;
#     it returns an int if both objects are of type int
I/F
# --+ integer division; it gives an error if F = 0
I//F
# --+ modulo
I%F
# --+ raising to the power
F**I

# %%  variables and assignments
'''
In the previous cells, we have associated objects with names:

+ we call this task 'assignment'
+ the outcome of the task is variable

**WARNING:** some names are reserved for Python keywords!! Don't use those
 keywords to name your variables
'''
# e.g.:
variable = I + F
