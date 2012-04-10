#!/usr/bin/python

import itertools
from problem03 import gen_primes

def problem7():
    gen = enumerate(gen_primes())
    gen = itertools.dropwhile(lambda e: e[0] < 10001, gen)
    gen = itertools.imap(lambda e: e[1], gen)
    return gen.next()

if __name__ == "__main__":
    print problem7()
