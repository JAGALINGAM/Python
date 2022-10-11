# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:24:25 2022

@author: Admin
"""

#Variables - are container to hold any data

#variables -used to store numeric data or text data and so on...

#Problem - Determine the monthly expenses of you 

#store every expenses in a unique variable and sum it.

#create the variable to store the expenses

food  = 3000  #(asignement operator)
travel = 5000 #(petrol, disel, public transport)
dress = 1000 

# to print i can print individual variable

print(food)
print(travel)
print(dress)

# to get total monthly expenses

total = food+travel+dress
print(total)

# why it is named as variable - value in the variable can vary

# for the varible food - i change the value to 8000. (used the same varibale but value assigned is different)

# how the variable store the text data

item1 ="food"
item2 = "travel"
item3 = "dress"
print("Expenses item for this month:", item1, item2, item3)


#variable name cannot be a predefind keyword (if, else, True, False)


#numbers:
#Mathmatical operations

12+34

34-12

10/2

10//2
 
10 * 10

10%2
 
10 ** 5

2 ** 8

#problem 2: You are driving from chennai to vellore and then going to coimbatore. You want to know how much total distance you will be travelling?  

chennai_vellore = 250
vellore_coimbatore = 400

total_distance = chennai_vellore+ vellore_coimbatore

#print(total_distance)
#print("The distance from chevellcbe is:",total_distance, "km")
total_distance
 

#Problem 3: You are driving the car 120kmph, calculate the time of the travel 

kmph = 120
time = total_distance /kmph
print(time)

# need to reduce the numbers after the point 

round(time, 2 )


20+4*2

#Priority on mathmatical operation 

(20+4)*2

5-4.7  # this is 0.3 but output is0.29

#numbers are store in binary form

# In any PL, to store float numbers (no precise way to store the floating numbers) 

round(5-4.7, 2)

