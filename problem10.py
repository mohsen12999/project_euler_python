# https://projecteuler.net/problem=10
# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

max=2000000

def isPrime(number):
    for i in range(2,int(number/2)+1):
        if number % i ==0:
            return False

    return True

sum=0
for i in range(2,max):
    if isPrime(i):
        # print(i)
        sum=sum+i

print(sum)
# 142913828922
