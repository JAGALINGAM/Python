# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:37:15 2022

@author: Admin
"""
3+2*2   # multiplication operator has higher precendence

(3+2)*2


#evaluate the following expressions

6*3 + 4**2 // 5-8   # //floor division 

4**2

6 * 3

16//5

""" 4 ** 2   =16

6 * 3 = 18

16 // 5 = 3

operation is left to right

18+3-8

21-8 

The answer is 13"""

(6*3 + 4**2) // 5-8



34//5

""" () higher precendence

4**2  = 16

6*3 = 18

18+16 =34

34//5 = 6

6-8 = -2"""

10>5 and 7>12 or not 18 > 3

#true and False or not True

#True and False or False

#False or False

#False


print(2+3-4/5//6*7%8)


"""4/5 - 0.8

0.8//6 - 0.0

0.0 * 7 - 0.0

0.0 % 8 - 0.0 

2+3 = 5

5-0.0  = 5.0"""


print(2**2**2)



print(2//3+4*2%3-1**9**8)   Right to left associative 


#9**8 = 43046721


#1**43046721 = 1

#slove from left to right

#2//3 = 0 

#4*2  =8

8 % 3 =2


# Try to solve the below expressions

#print(4/5//6*7%8)

#print(2%3-4+5//6*7%8)

#print(2*3-5//6*7%8+2)

#print(True and False or True)

#print(True and False or not True)

#print(2 and 3 or 1)

#print(3 and 2 or 9 or not 2 or 5)





#problem 1: write a python program to convert temperature from celsius to Fahrenheit


"""  1) Ask user to enter the temperature in celsius 

     2) Use the formula to convert the celsius to fahrenheit

     3) display the output

To have temperature in F = (multiply celsius with 1.8) and add 32

                         = If c is 0 (1 * 1.8) + 32
                         
                         for 0 degree Celsius =  32 degree Fahrenheit"""
                         
#ask the user to enter the temperature
          
c=float(input("Enter the temperature in celsius:")) 

F = (c * 18) + 32 

print(" %.2f c = %.2f F"  %(c, F))             
                         


# Find the area of the circle 

#area 3.14*r(square)


r = float(input("Enter the radius of the circle:"))

area_of_circle = 3.14*r*r

print("Area of the circle is:", area_of_circle)

# r use the math module





import math 
r = float(input("Enter the radius of the circle:"))
area_of_circle = math.pi *r*r
print("Area of the circle is:", area_of_circle)


print(math.pi)


                