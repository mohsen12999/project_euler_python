# https://projecteuler.net/problem=3
# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

num = 600851475143


def isPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False

    return True


number = num
i = 2
while i <= number:
    if(number % i == 0):
        number = number/i
        # print("find i: ",i," ,new number is: ",number)
    else:
        i = i+1

print("answer is: ", i)
