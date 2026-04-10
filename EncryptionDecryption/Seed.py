from time import time_ns
from os import getpid

def seed():
    seed = time_ns() ^ getpid()
    return seed