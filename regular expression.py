import re
a = "python language easy to understand"
b = re.match ('is', a)
print ("on failure:", b)
c = re.match ('python', a)
print ("on success:", c)




import re
a = 'v.....e'

#a is a pattren 
#b is a test string we want to match. 
#c is the result. 

#^ indicates the pattern present at the begining of the string or not. 
#$ indicates the pattern present at the end of the string or not. 

"""b = 'vellore'
c = re.match(a, b)
if c:
 print("success")
else:
    print("failure")"""	



import re
a = "Vellore is good place to stay. But climate in the Vellore is hot during summer"
b = re.findall("is", a)
print(b)






import re
text = """ Python is good, VIT is IOE, Python is user friendly"""
a = re.findall('is', text)
print (a)



import re
a = 'Vellore 100 1001 VIT 2020 INIDA 7'
#a pattern

# \d+ string contains  digit.

b = '\d+'
c = re.findall(b, a) 
print(c)




import re
a = 'vellore1 2vit India_89 python2020'
b = '\s+'
c = re.split(b, a) 
print(c)




import re
a = 'vellore12 India_89 python2020'
b = '\d+'
c = re.split(b, a) 
print(c)=



import re
a = "VelloreInstituteofTechnology"
b = re.split("\s+", a)
print(b) 


import re
a = "Vellore Institute of Technology"
b = re.sub("\s", "7", a) 
#\s pattern, 7 - replace, a-string
print(b) 

import re
a = "Vellore Institute of Technology"
b = re.sub("\s+", "7", a, 0)
print(b) 
#can control the number of replacement  by specifying the count parameter
#\s - pattern, 7 -replace, a-string, count =2
#if count = 0 it replaces all occurences 


import re
a = "Vellore Institute of Technology"
b = re.search("Vi", a)
print(b)  

#it looks for the first location, if found return - match object, if not - none



import re
a = "Vellore Institute of Technology vit"
b = re.search('\d', a)
if b:
  print("pattern found")
else:
  print("pattern not found")


  
#\A - character at the begining of the string
#\B -character not at the begining or end of the word
#\d- string contains digit



import re
a = "Vellore Institute of Technology "
b = re.search(r"\bo\w+", a)
print(b.span())

# r is before the string " " - interpreter understand as a character. 

import re
a = "Vellore Institute of Technology "
b = re.search(r"\bV\w+", a)
print(b.string)

# \b matches the string at the begining of the word

import re
a = "Vellore Institute Tf Technology Technology"
b = re.search(r"\bT\w+", a)
print(b.group()) 


import re
a = '\n and \r escape sequences \n and \r.'
b = re.findall(r'[\n\r]', a) 
#b = re.findall(r'escape', a) 
print(b)




"""import re
str = 'vellore1 Vit-institute@technology.com python India'
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print ('Success')
else:
    print ('failure')"""
    
    
    
    
m = re.match(r"(\w+) (\w+)", "VIT INDIA")
m.group(0)       # The entire match
m.group(1)       # The first parenthesized subgroup.
m.group(2)       # The second parenthesized subgroup.
m.group(1, 2)    # Multiple arguments give us a tuple.








