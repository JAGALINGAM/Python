# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:19:46 2022

@author: Admin
"""

#data types:
    
#What type of data  to store in a variable 

#Python is an object oriented programming language

#data types are considered as a classes .

#Varibles are called as instance of object of class

vit = 3.3; # data type of variable is int

print(type(vit))

#the data type int, float, char are class

#vit is the object or instance of the class int

 # different datatypes are - int, float, string, boolean 
 
 #int - holds the Positive number and negative number 
 
vit = 3.3 #(this is int)

""" What is prefix to the number

Int- binary type, octal type and hexadecimal type

0b and 0B -  binary

0o and 0O - octal

0x and oX - hexa decimal"""

print(0b10)  # complier know this is binary number 

#binary 10 - in decimal it print 10

print(0x10)
print(0o10)

# 0 is prefix, it is octal number 

var = 0b10
print(var)
print(type(var))
 
 
 
 
 
 #string: "is a sequence of character"
 
 #boolean: True and  false
 
vit = 5898989888989 #long value, no limit in the range of numbers 

print(vit) 


vit=10
vit1=5.1
print(vit + vit1)   # concatenation (string)
print(type(vit))
print(type(vit1))

vit=0o10
vit1=0x11
vit2= 789
print(vit + vit1)   # concatenation (string)
print(type(vit))
print(type(vit1))

print(vit2)



#string
vit = "Vellore Institute of Technology"
print(type(vit))

print(vit[8])


vit = "Vellore"
vit1 = "vit"
print(vit+vit1)

#what is the output for the following program 

vit = "Vellore"
vit1 = "vit"
vit2 =7
print(vit+vit2)



vit = "567"
vit1= "234"
print(vit+vit1)

print("Vit's' best university")

#i want  to print the output with the double or single quotes 

print("Vit\'s' best university")

      
# escape sequence (backslash)

print("vit's" "University")

#i want ot print single quotes and double quotes
print("vit\'s \"university\"")

print("vit\'s  \n \"university\"")

print("vit\'s  \\n \"university\"")

#boolean

vit = False
print(vit)

print(type(vit))


#diff b/w print and input function

print("VIT")

input("Enter your name:")


print("VIT" + " " + "FRESHERS")


print("vit" + " " +input("Are you fresher:") )



#problem:

"""output - Are you fresher/senior?  fresher

Hey fresher, vit welcomes you"""

print("Hey" + " " + input("Are you fresher/senior:?") + "," + "vit welcomes you")



#how to check the type o data
#Type casting or type conversion

#Conversion of one datatype to another  (int to float)


#to calculate the lenth of the string

#len is used to find the length of the string. 

print(len("Vit "))

vit = len("123")
print(vit)

print(len(vit)) # type error
#len is used only for the string


#What is the output for the following code
vit = len("123")
print("The length of vit is" + vit + "characters")

#vit is int, int cannot be concatenated with string. How do we solve this problem 

#convert the int datatype to string

vit = len("123")
print("The length of vit is" +" " + str(vit) + " " + "characters")

#vit has integer value, this is converted to string

print(type(vit))  # vit is int

new_type = str(vit)
print(type(new_type))

#conversion of datatypes
"""int()
float()
str()"""

print(5+5)  # addition of 5 and 5

print('5'+'5') # this is str, convert to int

print(int('5')+int('5'))


print(10+ "10")  #type error

print(5+ float("5"))  


# what is the output of the following code:
vit = "Vellore"
print(2022 + int(vit))

vit = "123"
print(2022 + int(vit))  # 123 has base 10 but "vellore" do not have base 10



"""problem 2:  Read two integer numbers from the user and do the addition operation.

then convert to the float."""

number1 = input("Enter the first integer number:")

number2 = input("Enter the second integer number:")

add = number1 + number2

print(add)  # furst number 5 and second number 5 : output is 55

#why?  when the user enter the  and second number, it is considered as a string


number1 = int(input("Enter the first integer number:"))

number2 = int(input("Enter the second integer number:"))

add = number1 + number2

print(add)


#other way is

number1 = input("Enter the first integer number:")

number2 = input("Enter the second integer number:")

add = int(number1) + int(number2)

print(add)



"""Problem 3: Write a python program to add digits of a number

read the digit from the user: 34

output: 7"""

two_digit_number = input("Enter two digit number:")  #the user enter number is string

# if user enter 23, then it is string, then 0 is 2 and 1 is 3
first_digit=two_digit_number[0]     # digit 2 is stored
second_digit=two_digit_number[1]    # digit 3 is stored
print(first_digit+second_digit)

# the output is 23, the numbers are in string only. convert to int

two_digit_number = input("Enter two digit number:")  #the user enter number is string

# if user enter 23, then it is string, then 0 is 2 and 1 is 3
first_digit=two_digit_number[0]    # digit 2 is stored
second_digit=two_digit_number[1]  # digit 3 is stored
print(int(first_digit)+int(second_digit))

    
""" Problem 4: Swap two numbers"

x=5
y=4

after swap x=4 and y=5"""


x =input("Enter the integer value of x:")

y = input("Enter the integer value of y:")

#to swap i need a temp variable

temp = x  # in temp store the value of a

x = y # b value is stored in a

y = temp # temp value is stored in b

print("the value of x is:", x)
print("the value of y is:" + y)  #concatenation, the value y is string





