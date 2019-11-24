# https://projecteuler.net/problem=9
# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

sum=1000
answer = False

for b in range(1000):
    for a in range(b):
        c2 = a*a + b*b
        c = math.sqrt(c2)
        if a+b+c == 1000:
            answer=True
            break
    if answer:
        break

print(a,b,c)
print(a*b*c)
