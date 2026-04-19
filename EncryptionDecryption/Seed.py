from time import time_ns
from os import getpid

# function for computing seed using system time and process ID
def seed():
    seed = time_ns() ^ getpid()
    return seed