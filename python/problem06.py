#!/usr/bin/python

def sum_of_squares(n):
    def squares(n):
        for i in range(1, n + 1):
            yield i ** 2
    return sum(squares(n))

def square_of_sum(n):
    return sum(xrange(1, n + 1)) ** 2

def problem6():
    n = 100
    return abs(sum_of_squares(n) - square_of_sum(n))

if __name__ == "__main__":
    print "6:", problem6()
