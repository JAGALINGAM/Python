# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:59:04 2022

@author: Admin
"""


"""  To solve any number program

1) Duck number
2) Spy number
3) Special number
4) Neon Number
5) Harshad number
6) Palindrome number 



Step1:

How to break the number to digits:"""


#1) Program to break the number to the digits: 
n = int(input("Enter the number:"))

m = n     # Why you store n to m?  m get iterated multiple times, and become 0
while m!=0:
    d=m%10
    print(d, end = "")
    m=m//10
    
    
    
    
#  2) Write a python program to check the given number is  palindrome or not:


"""What is palindrome number:

write a number from front to back  (or) from back to front 

the number remains same:

example:

Number is 121

from front to back:  1  2  1

from back to front:  1  2  1


example 2:

number is 246

from front to back:  2 4 6

from back to front:  6 4 2


example 3:

Number is 268

from front to back:  2 6 8

from back to front:  8 6 2"""


n=int(input("Enter the number:"))

m = n

sum = 0

while m!=0:
    d=m%10
    sum =sum*10+d
    m=m//10
if(sum==n):
    print('yes')
else:
    print('No')
    
    

""" what is the procedure to slove any number program

step1:
    initialization
    m=n

step2:
    while m!=0:
        d=m%10
        

step3: 
    logic (as per the given questions)
    
    
step4:
    if(check the condition)"""
    
    
#3) Write a python program to check the given number is spy number or not:
    
    
    #what is spy number: sum of digits =  product of digits
    
    
""" Example:1
    
    number =  153
    
    sum of digits is  =  1 + 5 + 3 = 9
    
    Product of digits =  1 * 5 * 3 = 15
    
    153 is not spy number:
        
        
        eaxmple 2:

            number = 123
            
            sum of digits = 1+2+3  = 6
            
            product of digits =  1 * 2 * 3 = 6
            
            123 is spy number"""
            

n = int(input("Enter the number"))

m = n

sum = 0; product = 1

while m != 0:
    d= m%10
    sum = sum + d; 
    product = product * d
    m = m // 10
if sum== product:
    print('yes')
else:
    print('No')
    
    
    
    
#4) Write a python program to check the given number is special number or not:
    
""" What is special number:
    
    sum of digits + product of digits  = given number
    
    
    given number  is 59
    
    sum of given number is 5+9 = 14
    
    product of given number is  5*9 = 45
    
    14+ 45 = 59 (equal to the given number)"""
    
n = int(input("Enter the number:"))

m=n

sum = 0; prod = 1

while m!= 0:
    d = m%10
    sum = sum + d
    prod = prod * d
    m = m//10
if(sum + prod) == n:
    print('yes')
else:
    print('No')
    
    
    
#4) Write a python program to check the given number is duck number or not:
    
    
    
    