# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

num=20
answer=1

for i in range(2,num+1):
    for j in range(i,0,-1):
        if i%j==0 and answer%j==0:
            break
    # print(i,j,i/j)
    answer=answer*i/j

print(answer)
# 232792560