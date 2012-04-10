#!/usr/bin/python

import math

def primes_less_than(n):
    """http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes"""
    if n == 1:
        return [1]
    marked = [False, False] + [True] * (n - 2)
    for i in xrange(2, n / 2):
        if marked[i]:
            for j in xrange(2 * i, n, i):
                marked[j] = False
    primes = []
    for i, ele in enumerate(marked):
        if ele:
            primes.append(i)
    return primes

def problem3():
    n = 600851475143
    primes = primes_less_than(int(math.sqrt(n)) + 1)
    prime_factors = []
    
    for p in primes:
        if pow(p, 2) > n:
            break
        while n % p == 0:
            prime_factors.append(p)
            n /= p
    if n > 1:
        prime_factors.append(n)
    
    return max(prime_factors)

if __name__ == "__main__":
    print problem3()
