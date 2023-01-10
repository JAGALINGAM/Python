# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:20:26 2023

@author: Admin
"""

"""Lambda   - special type of function without a function name.


In general  to create a function -   use def keyword

but to create a lambda function - use lambda keyword


Syntax:
    
lambda arguments: expression    


arguments - value passed to the lambda function

expression - excecuted and returns"""



"""Example one:
    
    Multiple 5 to the arugument x, and return the output"""
    
#Defining the lambda function    
mul = lambda x: x * 5


#call the lambda function
mul(3)


    

#Lambda function can take any number of aruguments but only one expression

"""Perform addition of two numbers using lambda function"""

#def
add = lambda x, y: x+y

#call

output=add(5, 10)

print(output)




"""Multiple 3 numbers and return the output"""

mul = lambda x, y, z: x * y* z

output = mul(1, 2, 3)

print(output)

#To pass a string 

wel = lambda name: print('welcome to vit', name)

output = wel('python')

print(output)



#Lambda is anonymous function - why?   (Do you find a name of the function)


#Lambda function is a function without name.




#  normal function to find the square of a number

#function definition
def square(a):
    return a*a

#function call

result = square(2)

print(result)



#with lambda function

square = lambda x: x*x

output = square(5)

print(output)





#lambda function can be used insdie the function. 

def number(a):
  return lambda b : b * a    # Anonymous function

# the function number takes one argument, it is multiplied with unknown number

multiply = number(2)

print(multiply(10))



#Use lambda functions when an anonymous function is required for a short period of time
