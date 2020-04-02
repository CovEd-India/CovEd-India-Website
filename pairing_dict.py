# First read pairing.py to get a better understanding
# This is a one-time-run code
# This code will create a dictionary by reading match assignment spreadsheet
# And save it to a file called pairs.npy

import numpy as np

mentorOf = {}

# insert code here

np.save('pairs.npy', mentorOf)