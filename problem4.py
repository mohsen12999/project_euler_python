# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic(number):
    st = str(number) # convert to string 123=>'123'
    ist = st[::-1]   # inverse the string '123'=>'321'
    if st==ist:
        return True
    return False

answer = 0
for i in range(100,1000):
    for j in range(100,1000):
        num=i*j
        if is_palindromic(num) and num>answer:
            num1=i
            num2=j
            answer=num

print(num1,num2,answer)
#906609 913 993