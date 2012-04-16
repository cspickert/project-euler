#!/usr/bin/python

def reverse_str(s):
    return reduce(lambda a, b: b + a, s)

def is_palindrome(n):
    return str(n) == reverse_str(str(n))

def problem4():
    palindromes = []
    for i in xrange(10**2, 10**3):
        for j in xrange(10**2, i + 1):
            n = i * j
            if is_palindrome(n):
                palindromes.append(n)
    return max(palindromes)

if __name__ == "__main__":
    print "4:", problem4()
