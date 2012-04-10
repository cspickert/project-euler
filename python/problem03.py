#!/usr/bin/python

import math
import itertools

def gen_primes():
    """http://stackoverflow.com/questions/567222/simple-prime-generator-in-python"""
    d = {}
    q = 2
    while True:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1

def primes_less_than(n):
    return itertools.takewhile(lambda p: p < n, gen_primes())

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
