# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 10:22:18 2022

@author: Admin
"""

#numpy - popular module used in scientic computing 

"""To install numpy - pip install numpy

used to work with n dimentional array"""

import numpy as np 

#to create a array object

x = np.array ( [5,6,7] )

print(x)


#list 
l = [5,6,7]
print(l)

#this operation is similar to the list

# why array is needed? 

#Less memory, 2) Fast, 3) Convinient 


import numpy as np
import time
import sys

l = range(1000)  # created a list which has a 1000 elements
print(sys.getsizeof(1)*len(l))

#size of the list (size of each element)

# create an array 

array = np.arange(1000)

#arange  - creates a array with an element 0 to 499 

print(array.size*array.itemsize)

#array.size - gives the size of array  (total length of array)

#array.itemsize  - size of one element

#python list takes 28000 bytes but the numpy array takes 4000 bytes 

#size of one pyhton object is 28 

# size of one numpy object is 4 bytes


#numpy array - points to the  contiguous location of memory, each element occupy 4 bytes of memory 
#In python - a first list contains a list of pointers first, then each pointer points to another location in the memory
#size of one object is 28 bytes

# numpy is fast and convinient

#create two list l1 and l2 and create two array a1 and a2.

# measure the time b/w list and array 

import numpy as np
import time
import sys

SIZE  = 500000

l1 = range(SIZE)

l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# measure the time b/w list and array 

start = time.time()

# add two list l1 and l2

result = [ (x+y) for x,y in zip(l1,l2)] 

#take the first element from l1 and second element from l2, add it and store in the variable result.

print('time taken by python list is:', (time.time() -start) * 1000)

print('time taken by python list is:', (time.time() -start))

#multiply with 1000 beacuse time.time() is in seconds multiply with 1000 gives milliseconds


#for numpy array 
start = time.time() # i capture the time again
result = a1 + a2

print("Time taken by numpy array", (time.time() -start) * 1000 )

print("Time taken by numpy array", (time.time() -start))

# for the data of 500000 (to add) the python list taken 92 milliseconds
#for the data of 500000 (to add) the numpy array taken only 10 miliseconds