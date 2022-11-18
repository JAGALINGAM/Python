# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 08:01:14 2022

@author: Admin
"""

gender = input("Enter the gender (male, female, m, f:)")


age = int(input("Enter the age:"))

if(gender.lower() in("female", "f") ):
    if(age>=18):
        print("Eligible for marriage")
    else:
        print("Not eligible for marriage")     

elif(gender.lower() in("male", "m")):
    if(age>=21):
        print("Eligible for marriage")
    else:
        print("Not Eligible for marriage")
else:
    print("Wrong input")
        


number = int(input("Enter the number:"))

factorial =1

if(number < 0):
    print("Factorial cannot be calculated")
elif(number < 2):
    print("{}! ={}".format(number, factorial))
else:
    for i in range(number, 1, -1):
        factorial = factorial*i
        print("{}! = {}".format(number, factorial))





for i in range(1001):
    num = i
    result = 0
    n = len(str(i))
    while(i!=0):
        digit = i%10
        result = result+digit**n
        i = i//10
    if(result == num):
        print(num)
        
        
            
print('#') 
print('#')  
print('#')
print('#')  


print('#', end="")                 
print('#', end="") 
print('#', end="") 
print('#', end="")

print('#', end="")                 
print('#', end="") 
print('#', end="") 
print('#', end="") 

for i in range(4):
    print("#", end="")
print()
for i in range(4):
    print("#", end="")
print()
for i in range(4):
    print("#", end="")
    
for i in range(4):
    for j in range(4):
        print("#", end="")
    print()
    
    
for i in range(5):
    for j in range(5-i):
        print("#", end="")
    print()  
    
    
    
n=5
for i in range(n):
    for j in range(i,n):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()
    
    
n = int(input("Enter the number"))

m = n

while m != 0:
    d = m%10
    print(d, end=" ")
    m = m//10
    
    
        















n = int(input("Enter the number:"))

m=n

sum =0

while m !=0:
    d = m%10
    sum = sum *10 + d
    m = m//10
if sum == n:
    print('yes')
else:
    print('no')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

n = int(input("Enter the number:"))
m = n
sum = 0; product=1
while m != 0:
    d = m%10
    sum = sum+d
    product = product*d
    m = m//10
if(sum==product):
    print('SPY NUMBER')
else:
    print('N0')

    
    