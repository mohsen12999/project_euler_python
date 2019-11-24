# https://projecteuler.net/problem=6
# Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

max=100

sumofsquares=0
for i in range(max+1):
    sumofsquares = sumofsquares + i*i

sum=0
for i in range(max+1):
    sum = sum+i

squareofsum=sum*sum

answer = squareofsum-sumofsquares
print(answer)

