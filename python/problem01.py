#!/usr/bin/python

def problem1():
    return sum(filter(lambda i: i % 3 == 0 or i % 5 == 0, range(1000)))

if __name__ == "__main__":
    print "1:", problem1()
