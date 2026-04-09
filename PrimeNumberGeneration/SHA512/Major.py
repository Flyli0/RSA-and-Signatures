def maj(x, y, z):
    major = (x & y) ^ (x & z) ^ (y & z)  # function that majors bits (if 0 s are in majority -> answer = 0)
    return major 
