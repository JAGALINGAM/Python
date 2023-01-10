# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 12:03:14 2023

@author: Admin
"""

"""What is modules?

library


set of many function - performs the specific task


code reusability. 



math
random
decimal
cmath
time"""



#math module is used to perform  mathematical tasks. 

import math

result = math.pi
print (result)

x = 4

result1 = math.sqrt(x)

print(result1) 


result2 = math.factorial(2)
print(result2)





from math import pi
print(pi)
 





from math import ceil
result3 = ceil(4.567)
print(result3)




from math import floor
result4 = floor(5.97)
print(result4)


#To print the random number b/w 0 to 5

import random
result5 = random.randint(0,5)

print(result5)



from random import randint
result5 = randint(0,5)
print(result5)


import time
print(time.ctime())


from time import ctime
result6 = ctime()
print(result6)


from time import localtime
result7 = localtime()
print(result7)









































