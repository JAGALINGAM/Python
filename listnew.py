# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:52:13 2022

@author: Admin
"""

"""

LIST

Is a DATA STRUCTURE algorithm 


For every application - data to be stored for the process.

To store the data - need a structure?  why?

To access the data effectively 

List - predefined to structure the data(information)


Four collection type in python - LIST, TUPLE, SET AND DICTIONARY


LIST


1) what  is LIST?

List is an ordered collection 

In which ordered the elements are inserted

In the same order the elements were processed. 


How to represent the LIST?


x = [1, 2, 3, 4, 5]  elements are stored in the order 1 2 3 4 5 

print(x)    in same order the elements were printed




2) can we store the duplicate element in the list? 

list can store duplicate elements

list can store heterogeneous (dissimilar) element


does python support array?  No. why?

array is static, and collections are dynamic. 


why dynamic -  SIZE of the collections (LIST) grows or shrinks based on the insertion operation. 


List can store the different type of elements

x = [5, 4.8, 3, "VIT"]

print(x)



3) How to process the element of the list

using indexing and slicing 


what is indexing - can access only one element at a time. 


Does the python supports negative indexing? yes  (start with -1)


x = [1, 2, 3, 4, 5]  how the memory is allocated? 

positive indexing

indexing x[0] = 1

x[1] 2
x[2] = 3
x[3] = 4
x[4] = 5   


negative indexing

x[-1] = 5
x[-2] = 4
x[-3] = 3
x[-4] = 2
x[-5] = 1

Process the element of list using positive and negative indexing?


x = [1, 2, 3, 4, 5]

x[2]  o/p is 3

x[-1]  is 5


4) How to find the length of the list?

len function

len(x) -  5

what is the output of the following expression?

x[len(x)-1]


what happens when we try to access the element out of the bound?

x[len(x)]

len(x) is 5, x[5] list x has only five elements 

we can access the element with in the range. 


"""




"""

Can access the element in the list using indexing and slicing:

difference b/w indexing and slicing


indexing - process the only one element at a time.

cannot process multiple elements at a same time

 
LIST SLICING

syntax:  [lower_bound : upper_bound]


lower_bound = element of the lower bound is included 


upper_bound = element of upper bound is excluded


[1:5]

index[1] element is included and index[5] element is excluded.

the elements b/w 1 and 4 is processed. 


x = [1, 2, 3, 4, 5, 6, 7]

x[0:5]



If we do not specify the upper bound

x[1: ] it prints all the element in the list

x[ :3] it prints element from 0 to 2

x[:]  it prints all the element from the first index to the last index


x[0:len(x)]  prints all the element from 0 to last element (len(x) is length of the list)



To access the element postive, negative and mix of positive and negative were used 

x[-5:-1]

x[-5: 3]    Negative and positive index

-5 is the staring position and 3 is the ending position

"""


"""
LIST functionality (pre defined function)


Predefined function in LIST

LIST is a collection

LIST has a predefined  function



The each predefined function - used to modify the LIST


Modification on LIST

1) Insert 2)Delete, 3) sort, 4) Reverse 
    
    
    
Insert:
    
x = [1, 2, 3, 4, 5, 5, 3, 4]   (duplicate (elements are repeated)

print (x)


To the list x -  different ways to insert the element

1) append() - used to add the element at the end of the list

x.append(10) 

print(x)


2) To insert the element at the specified location 
    
    element index starts with 0
    
    in the list x, insert the element at the position 3
    
    x.insert(3, 20)

    3 is the position element to be inserted, element is 20 
    
    
3) Other way - check the length of the list 
    
    len(x)
    
   x.insert(11, 30)   No index 11 is present in the list x. It append 30 at the end of the list
   


DELETION   

pop() -  it removes the last element from the list

x = [1, 2, 3, 20, 4, 5, 5, 3, 4, 10, 30]

x.pop() 


x.pop(3)  function takes the index as an argument

deletes the specific element


REMOVE

x = [1, 2, 3, 20, 4, 5, 5, 3, 4, 10, 30]

x.remove(20)


difference between the remove and delete

x.remove(5)   5 is the duplicate

first occurence of 5 is deleted


How to delete all the elements of list

x.clear()   # it shows the empty list

How to remove the memory allocated to the the list x

del x

"""



"""
READING ELEMENTS INTO THE LIST

1) How to read elements to list
    
2)How to display all the elements (iteration)
    

    
    create a empty list
    
    1) x = []
    
    
    how to find x is a list or not
    
    type(x)
    
    
    2) x = list()  list is created using constructor (list)
  type(x)
    
    
    
    
How to read elements 

x = list()   # list is created

# how to read elemnts into the list


#range - starts with 0 to 4

#the loop repeats for five times

#every time the loop executes, it read elements 

x = list()
print("Enter five numbers:")

for i in range (5):   
    xelement = int(input())
    x.append(xelement)
    
print("The element of the list are:", x)
    
    

#case2:  Not sure how many elements to store  

# boundary condition is '0', if user enter the 0 stop adding the element to the list

# display all the elemnts of the list. 

   
    
x = list()  
print("Enter elements (enter 0 to stop):")

while True:
    xelement = int(input())  # read the element
    if xelement==0:
        break
    else:
        x.append(xelement)
print("The element of the list are:", x)
    
"""


""" IS LIST IS MUTABLE OR IMMUTABLE?

IMMUTABLE - After the creation of object, it cannot be modified

MUTABLE -After the creation of object, it can be modified

LIST IS MUTABLE  - therefore we can modify the list after creation


After the creation of list, following operations were performed

append, insert, pop, remove, clear, sort, reverse.....

after the modification of list, the address of the list remains same 


 x = [1, 2, 3, 4, 5]   list is created
 
 id(x)
 
 x.append(8)
 
 id(x)
 
 
 x.remove(2)
 print(x)
 id(x)
 
 
 x.reverse()
 print(x)
 
 AFfer the modification of list, check the id of the list, remains same
 
 Therfore LIST IS MUTABLE, it is not constant.
 
 
 
 Python is object oriented programming language, no primitive datatype.
 
 every data is stored in the form of object
 
 
 x = 10   x is a object (not a datatype)
 print(x)
 
 id(x)
 
 x = x+10
 print(x)

After modifcation, check the id, the address is changed. 

Integer is immutable object. object created in the line 407, we cannot modify 


x = "vit" 
id(x)
   

y =" Vellore"
id(y)

x = x+y    concatenation   

id(x)

string is immutable object, cannot modify, but we are able to modify S1?

new object S1 is created at the another location and address is copied 


Mutable - After some operation, if the address of the obejct remains same


immuatble - after some operation, if the address of the object changes"""


""" What are the elements can be stored in the list

LIST IS MUTABLE

LIST elemts either Mutable or Immutable 


Immutable object: Int, string  (when we modify the location changes)

Mutable:  List (when we modify the location remians same)


x = [1, 2, "vit", [3, 4]]
id(x)


[3,4]  = index is 3
Modify the list

x.append(10)

print(x)

id(x)   address remains same

x[3]

id(x[3])   Modify the list [3,4]

x[3].append(80)

print(x)

id(x[3])


x[3].remove(3)


After modification check the id of list, it remains the same. 


when the modification is done on the immutable objects the address changes


x= [1, 2]

x[0] 

id(x[0])


x[0] = x[0] +4
print(x)

id(x[0])


LIST IS MUTABLE - IT ALLOWS TO STORE MUTABLE AND IMMUTABLE OBJECTS


Storing Immutable objects

How the duplicate element stored inside the list

List -  immutable and mutable objects

Memory allocation for Immutable obejcts - different

Both x and y has the same string.

does x and y have same or different memory?

x = 5
id(x)

y = 5

x = x+5

id(x)


address is same for x and y.

One object is created (stores 5), x and y points to the address of the same objects

When the element is same, separate memory is not created 


modify the x, does it affect the y.  No

because object (5) is immuatble (i.e. constant object)

when the object is created, it cannot be modified

when we modify the content of the object

new object is created at the different location 


a = "VIT"

b = "VIT"

a = a+"Vellore"

x = [1, 2, 3, 4, 5]

id(x)

y = x.copy()

id(y)

Both x and y points to the same object, but x and y has different id?

list is a mutable object - therefore  x and y points to the same object, the address is different


for Imutable object (int, str) when the object is same, it points to the same id



Nested list - How to access the element of nested list

List is mutable - allows to store mutable and immutable objects

allows to store mutable (one more List - nested list)


x = [1, 2, 3, 4,[5, 6, 7]]

how the memory is allocated?

x[0] = 1, x[1] = 2, x[2] = 3, x[3] =4

x[4] = [5,6,7]   How it is stored

separate list is created 0 to 2 - this address point to the index[4]

len(x) = 5

x will store the address of the list


How the memory is allocated? 

we have index 0 to 4

negative index  = -1 to -4

In general, elements are stored in object.

but for this case, elements are stored as a reference.

How to access the element of the list 

x = [1, 2, 3, 4,[5, 6, 7]]

x[0] = 1
x[1] = 2
x[2] = 3
x[3] = 4 

x[4] 0 is 5
x[4] 1 is 6
x[4] 2 is 7

negative indexing is also possible

x[4] - 1 is 7
x[4] - 2 is 6
x[4] - 3 is 5

x = [1, 2, 3, 4,[5, 6, 7, 8, 9]]
 
len(x)

len(x[4])

len(x[-1])

both positive and negative index used to access the element

x[len(x)-1]

Access the element of list in different ways


How to access the element of the sublist

x[4][0]

x[4][1]

x[4][-1]

x[4][:]

x[4][1:5]

Print the alternative element of the list

x[4] [ : : ]

x[4] [ : : 2]

 :(lower bound) : (upper bound) all the elements in the list
 
 2 - step
 
 
 
 x = [[10, 20, 30],[40, 50, 60],[70, 80, 90],[100, 110, 120]]
 x[0]