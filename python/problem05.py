#!/usr/bin/python

import math
from problem03 import primes_less_than

def product_of_primes_less_than(n):
    return reduce(lambda a, b: a * b, primes_less_than(n))

def problem5():
    n = product_of_primes_less_than(20)
    while True:
        done = True
        for i in range(1, 20 + 1):
            if n % i == 0:
                continue
            done = False
            n *= int(float(i) / math.fmod(n, i))
            break
        if done:
            break
    return n

if __name__ == "__main__":
    print problem5()
