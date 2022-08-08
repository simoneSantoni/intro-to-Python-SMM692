# %%
# load modules
import numpy as np

# %%
# get data from a text file
# --+ create a string with the data and some qualitative comments on them
S = """
# Below are some demographic data about Michael J. Jordan (basketball player)
# from Wikipedia.
# 
# Data labels are:
# 
# NAME, BORN, NBA CHAMPIONSHIPS, AVERAGE POINT PER GAME
"Jordan, Michael Jeffrey","February 17, 1963",6,30.1
"""
# --+ write the data to a file
with open("my_data", "w") as pipe:
    pipe.write(S)
pipe.close()

np.loadtxt(
    open("my_data", "r"),
    dtype={
        "labels": ("NAME", "BORN", "NBA CHAMPIONSHIPS", "AVERAGE POINT PER GAME"),
        "formats": ("S1", "S1", "i4", "i4"),
    },
    comments="#",
    delimiter=',',
    quotechar='"'
)

