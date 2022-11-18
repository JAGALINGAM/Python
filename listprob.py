# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:17:11 2022

@author: Admin
"""

"""
Problem 1:
    
    List is a class
    How to create object to the class
    
    steps to be followed:
        1) create list object by calling the constructor of list class
            
    Note: List is predefined function
    
        2) Store ten elements to the list using append() method
    
        3) Display all the elements (while, for) of the list.

"""

"""
Problem 2:  Deleting the element from the list
    
different function to remove the element

1) remove()  - Remove the specified element- for duplicate (first occurence is deleted)

2)pop() - last element is deleted
    
3) pop(index) - removes the specified index 
    
4) clear - all the elements but not the list object
    
    
 5)del  - remove the object
    
    
    1) Create a list using constructor
    
    2) Store some element
    
    3) Implement all the above functions.

"""


""" 
Problem 3:
    
    Implement the following procedure using LIST
    
    1) create a list
    2) read a input from the user (minimum 10 names)
    3) Print the list
    4) Apply sorting (alphabetical) on the list
    3) Print the names in the list after sorting
"""


name = []

for i in range (3):
    n = input("Enter the name:")
    name.append(n)

print("Enter names are", name)


name.sort()
print("Sorted names are", name)



"""
Problem  4:  Write a program to read name and marks of 10 students.

print the name of the highest score  student

print the mark of the highest score  student


print the name of the lowest score student

print the name of the lowest score student

1) Create two list  (name, mark)
    
2) define the for loop to read mark and name from the user
    
3) append the name to the list name
    
4)append the mark to the list mark
    
5) Use max function to find the maximum mark
    
6) Use the min function to find the minimum mark
    
    
7) Print the name of the lowest score
    
    
 8) print the name of the highest score
    
    
 9) print the lowest mark
    
 
 10) print the highest mark
    
    
    

"""


name = []
mark = []

for i in range(5):
    n = input("Enter student name:")
    m=int(input("Enter the mark of the student"))
    name.append(n)
    mark.append(m)
highest= max(mark)
lowest = min(mark)

print("Highest mark is:", highest)
print("Lowest mark is:", lowest)






#How do i print the name of the students scored higher marks and lowest marks

for i in range(5):
    if highest == mark[i]:
        print("Student having highest marks is:", name[i])
    if lowest == mark[i]:
        print("Student having lowest marks is:", name[i])
        
        
        
        
"""Problem 5:
    
#read the value from the user and insert the element in the middle of the list

create the list add some element to the list

read the number from the user to enter

read the index position to be inserted

use insert function

print the modified list


"""


x = [1, 2, 3, 4, 5]

print("The list is:", x)

middle =int(input("Enter number to be inserted in the list"))

position = int(input("Enter the index number to insert the number:"))

x.insert(position, middle)

print("The modified list is:", x)

