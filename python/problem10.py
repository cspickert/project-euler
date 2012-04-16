#!/usr/bin/python

import itertools
from problem03 import gen_primes

def problem10():
    n = 2000000
    primes_below_n = itertools.takewhile(lambda p: p < n, gen_primes())
    return sum(primes_below_n)

if __name__ == "__main__":
    print "10:", problem10()
