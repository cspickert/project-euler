#!/usr/bin/python

def problem2():
    limit = 4*10**6
    stack = [0, 1]
    total = 0
    while True:
        n = stack[0] + stack[1]
        if n > limit:
            break
        if n % 2 == 0:
            total += n
        stack[0] = stack[1]
        stack[1] = n
    return total

if __name__ == "__main__":
    print problem2()
