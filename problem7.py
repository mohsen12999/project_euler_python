# https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def isPrime(number):
    for i in range(2,int(number/2)+1):
        if number % i ==0:
            return False

    return True

number=10001
count=0
i=1

while count<=number:
    i=i+1
    if isPrime(i):
        # print('prime',count,i)
        count=count+1

print(i)
# 104759