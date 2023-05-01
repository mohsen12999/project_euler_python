# https://projecteuler.net/problem=12
# Highly divisible triangular number
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

def count_divisors(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count = count+1
    return count


i = 0
triangle = 0

while True:
    i = i+1
    triangle = triangle+i
    count = count_divisors(triangle)
    print(triangle, count)
    if count >= 500:
        break

print(triangle)
