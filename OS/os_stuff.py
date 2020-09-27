#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    os_stuff.py  |  OS operations
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    -   check/change the working directory
    -   list files stored locally
    -   read multiple files

"""

# %% check and change the working dir

# NOTE: the os library is our Swiss army knife
# let's import it
import os
# get getcwd
print(os.getcwd())
# change it
os.chdir('/home/simon')     # adjust your path here
print(os.getcwd())          # and check again

# %% list files stored locally

# NOTE: the glob library goes well with os
# let's import it
import glob
# get files in the clone of the `smm692' repo
# --+ set the wd
os.chdir('/home/simon/githubRepos/intro-to-Python-SMM692')
# --+ list all directories and files irrespective of the format
my_files = glob.glob(os.path.join('.', '*')) # '*' = we don't care the format
my_files
# --+ list all directories and files in a target directory
my_files = glob.glob(os.path.join('_1/', '*'))
my_files
# --+ list files with '.md' extension only, that is, Markdown stuff
my_md_files = glob.glob(os.path.join('_1/', '*.md'), recursive=True)
my_md_files

# %% read multiple files

# list files to read
my_txt_files = glob.glob(os.path.join('.', '*.txt'))
my_txt_files
# read these files and store them in the same list
txt_stuff = []
for item in my_txt_files:
    with open(item, 'r') as pipe:
        to_append = pipe.read()
        txt_stuff.append([to_append])
txt_stuff
