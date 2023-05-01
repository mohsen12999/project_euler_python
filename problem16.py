# https://projecteuler.net/problem=16
# Power digit sum
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

pow = 1000
number = 1

for i in range(pow):
    number = number*2


def number_sum(num):
    sum = 0
    while num > 0:
        sum = sum+num % 10
        num = int(num/10)

    return sum


print(number, number_sum(number))
