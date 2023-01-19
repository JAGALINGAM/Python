# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 09:47:03 2023

@author: Admin
"""


""" 
What is Numpy?

Numpy -  Numerical Python

Numpy and pandas -  fundamental python packages for scientific compuation/programming


Scientific computation - deals with solving scientific or mathematical problems with the help of computers.


 
Why is numpy?

Basic scientific programming operations are:
    
    1) arrays, 2)matrices 3) Integration 4) Differential Equation solver, 5)Statistics
    
  
    
What are the features of numpy
use of numpy 


numpy - stands for numerical python


Fundamental Python package for scientific computing 


Tools and technique to solve mathematical problems

Numpy is wriiten in C and Python

Numpy is a library in python - it contains precompiled function for mathmatical and numerical routines.



History of numpy

numeric:  Jim Hugunin + other contributors 

In 2005, Travis oliphant developed Numpy 

it is open source - contains many contributors



Many functions in Numpy 

1)  Arrays - create array and apply many functions on array
    
    using numpy we can apply many operation on the array. 
    
    main feature of numpy is array 
    
    
    array are similar to list 
    
    if both array and list are same - then what is the difference. 
    
    
    
Python stores data in different way, the most popular one is list and dictionaries 
    
    
1) Similarities between list and numpy array:

     
both are used for storing data 

mutable (can add and remove element)

both can indexed 

slicing operation can be done on both


2) Diff b/w the list and numpy
    
List:  Different datatypes

[1, 3.4, "a", 5]

Array: Similar Datatypes  

[1, 2, 3, 4] contains only integer value

[1.1, 1.5, 1.7, 1.9] contains only float value 



Operation  - 

divide an array (apply the division operation on the array)

but in list - we get error"""

import numpy
a = numpy.array([1, 2, 3, 4, 5])
print (a)

b=a/2

print(b)


#List

list = [2, 4, 6, 8]
list1 = list/2


"""

Diff - to work with Numpy array - need to install Numpy libraries 


list - Built-in 


Advantages - numpy

1) Less Memory 
    
2) Fast
    
3) More Convenient -  Mathematical operations 
    
    
Array -  collection of elements of same types 


How to create a array?

1) From array module [python arrays]
    
2) Using numpy library [numpy arrays]  - it has many function to perform some task 

    
    
numpy array  - it also called as nd (n dimensional array)"""


#How to create a array  - using numpy lib

#Different function to create numpy  array 


# 1) Array(),  2)Arange(), 3) Zeros(), Ones(),  Linspace(), Eye(), Random() 



#Array:
    
    #create array from lists or tuples 



#import numpy   #array function belong to numpy lib

import numpy as np

#help(np.array)
    
a = np.array([1, 2, 3,4])

print (a)


#For 2D

np.array([[1,2], [3,4]])

np.array([1, 2, 3, 4, 5, 6], ndmin=3)
   

np.array([[1,2], [3,4], [5,6]])

#To change the dataype

np.array([1, 2, 3], "complex")
 
np.array([1, 2, 3], dtype="complex")

np.array([1, 2, 3], dtype="int8")

#create the array using tuple

np.array((1, 2, 3)).







# Arange()   = array range

# creates array of evenly spaced values. 

#help(np.arange)
 
import numpy as np
np.arange(1, 10)   #start is 1 and stop is 10



np.arange(3.0)   # stop is 3.0

# by default stop value is 0 


np.arange(1, 10, 2)  # step is the space between the values 


np.arange(20, dtype = "complex")  # 20 is stopping value 

np.arange(20, dtype = "int") 



np.arange(1, 10, 2, dtype="float" )



#Numpy Zeros function 

#creats array filled with zeros

import numpy as np
#help(np.zeros)

np.zeros(6)   #default datatype is float 


np.zeros(3, dtype="int")


np.zeros((2, 3))   #tuple 

np.zeros([4, 3]) 

np.zeros(4, order="F")


np.zeros(4, order="C")



#Ones()

help(np.ones)

import numpy as np

np.ones(5)


np.ones(5, dtype = "int8")

np.ones((3, 4))


#empty function

help(np.empty)



import numpy as np

np.empty(6)

np.empty([2, 2])

np.empty([3,4], dtype="int")



#linespace function:
    
#linspace() and range() function are similar

#creates Array filled evenly spaced values


#diff is in range - specify the step value, in linspace() - specify break 



import numpy as np 
help(np.linspace)   


np.linspace(2.0, 3.0, num=6)   #start is 2.0 and end is 3.0, o/p includes end,  endpoint is true


np.linspace(2.0, 3.0, num=5, endpoint=False)  #3.0 is excluded 

#we do not specify the space b/w the values (step), we specify num=5, i.e how many values we need b/w 2.0 to 3.0

np.linspace(2.0, 3.0, num=5, retstep=True)



np.linspace(1, 100, num=10)


np.linspace(1, 100, num=4, retstep=True, dtype=int)



np.linspace(1, 10,  retstep=True, dtype=int)



#Eye() 

#Returns array filled with zeros except in the K-th diagonal, whose values are equal to 1.

help(np.eye)

np.eye(5) #number of rows, column number is not mentioned (therefore row number is same as column)

np.eye(2, 3)

np.eye(4, k=-1)   #k=-1 lower part of the diagonal is one. 


np.eye(4, k=2)  


np.eye(5, dtype=int)


#Idenity function is similar to the eye function 

help(np.identity)

np.identity(3)   #n=3 and m=3 it creates the squrae matrix

np.identity(3, dtype="int8")


#random numbers

help(np.random)

""" IN random function we have the following

rand - uniformly distributed values

randn - Normally distributed vlaues

ranf - Uniformly distributed floating point numbers

randint - uniformly distributed integers in a given range"""

help(np.random.rand)


np.random.rand(3)
np.random.rand()

np.random.rand(3,2)


help(np.random.randn)

np.random.rand(3)


np.random.randn(3,2)


np.random.ranf(2)

np.random.randint(3)
help(np.random.randint)

np.random.randint(2, size=10)