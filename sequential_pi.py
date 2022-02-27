#!/bin/env python3

# from
# https://www.literateprograms.org/pi_with_the_bbp_formula__python_.html

import sys
from time import sleep
from gmpy import mpq, mpz

def mod1(x):
    return x-mpz(x)

def pi():
    x = 0
    n = 1
    while 1:
        p = mpq((120*n-89)*n+16, (((512*n-1024)*n+712)*n-206)*n+21)
        x = mod1(16*x + p)
        n += 1
        yield int(16*x)

def allpi():
    sys.stdout.write("3.")
    for p in pi():
        sys.stdout.write("%x" % p)
        sys.stdout.flush()
        sleep(0.1)


if __name__ == "__main__":
    allpi()
