#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def isPrime(number):
    for i in range(2,int(number/2)):
        if number % i ==0:
            return False
    
    return True

num = 600851475143

for i in range(int(num/2),2,-1):
    if num % i == 0:
        print("factor "+i)
        if(isPrime(i)):
            print("answer is: "+i)
            break
    
    if i%100000==0:
        print("*",end='')
    
    if i%10000000 ==0:
        print("\n@",i,":")