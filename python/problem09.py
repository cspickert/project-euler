#!/usr/bin/python

# First attempt:
#
# def problem9():
#     for c in range(500):
#         for b in range(c):
#             for a in range(b):
#                 if a**2 + b**2 == c**2:
#                     if a + b + c == 1000:
#                         return a * b * c
#     return 0

# Better attempt (after browsing forum):
#
# a + b + c = 1000
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2
# m^2 - n^2 + 2mn + m^2 + n^2 = 1000
# 2m^2 + 2mn = 1000
# m(m + n) = 500

def pythagorean_triple(n):
    for m in range(n / 2):
        for n in range(m):
            if m * (m + n) == 500:
                return [m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2]

def problem9():
    n = 1000
    return reduce(lambda a, b: a * b, pythagorean_triple(n))

if __name__ == "__main__":
    print "9:", problem9()
