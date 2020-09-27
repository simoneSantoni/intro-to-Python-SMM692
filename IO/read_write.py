#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    read_write.py  |  IO operations
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    + reading and writing strings
    + reading and writing lists
    + reading and writing dictionaries

"""

# %% readng and and writing strings

# sample string
s = """This is a short sentence."""
# write string to file
my_file = 'short_sentence.txt'     # target file
with open(my_file, 'w') as pipe:   # we open a pipe to the target file
    pipe.write(s)                  # we write the data using the pipe
# read string from a file
with open(my_file, 'r') as pipe:   # we open a reading pipe to the target file
    and_back = pipe.read()         # we read the data using the pipe
and_back                           # display the newly create object
type(and_back)                     # ... and check its type

# %% reading and writing lists

# sample list
l = [0, 'a', 2.98]
# write list to file
my_file = 'sample_list.txt'
with open(my_file, 'w') as pipe:
    for item in l:                        # place items in different lines
        pipe.write('{} \n'.format(item))
# reading
and_back = []
with open(my_file, 'r') as pipe:
    for line in pipe.readlines():         # lines are read separately
        and_back.append(line.strip())     # append the lines
and_back                                  # check the outcome

# NOTE: the pickle library is an alternative to the above-displayed code
#       ― just keep in mind you can't open .pickle files in your text editor

import pickle
# write data
my_file = 'list_as_pickle.pkl'
with open(my_file, 'wb') as pipe:# pickles aren't strings - 'wb' = write bytes
    pickle.dump(l, pipe)         # 'dump' writes data
# read data
with open(my_file, 'rb') as pipe:
    andback = pickle.load(pipe)  # 'load' reads data
and_back                         # check the outcome

# %% reading and writing dictionaries

# NOTE: the json file format allows to preserve the structure of the
#       dictionary (see nested dictionaries and lists)
# so, let's use the json library
import json
# sample dictionary
d = {'a': 1, 'b': 4, 'c':{'c_0': 3, 'c_1': 2}}
# writing data
my_file = 'sample_dict.json'
# write data
with open(my_file, 'w') as pipe:
    json.dump(d, pipe)
# read data
with open(my_file, 'r') as pipe:
    and_back = json.load(pipe)
and_back                             # display dictionary
type(and_back)                       # check type
