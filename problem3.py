#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def isPrime(number):
    for i in range(2,int(number/2)):
        if number % i ==0:
            return False
    
    return True

num = 600851475143

# for i in range(int(num/2),2,-1):
#     if num % i == 0:
#         factor = i
#         print("factor "+i)
#         if(isPrime(i)):
#             print("answer is: "+i)
#             break

number = num
i = 2
while i<=number:
    if(number%i==0):
        number = number/i
        print("find i: ",i," ,new number is: ",number)
    else:
        i=i+1

print("answer is: ",i)
#6857