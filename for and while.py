a = [1,2,3,4,5] 
for b in a:
    print('The square of numbers', b**2)
    

a = 'Welcome to VIT' 
for b in a:
    print('The characters', b)


for a in range(10): 
    print('The number', a) 
#print(a, end =" ") 
    

#a = [45, 60, 90, 110] 
#for b in range(len(a)): 
#    print(a[b], end =" ") 
#print() 


a = 0
for b in range(1, 5): 
    a = a + b 
print("Sum of number :", a) 


for a in range(5, 40): 
    print(a, end =" ") 
 

for a in range(0, 20, 2): 
   print(a, end = " ") 
    
for i in range(10, 20, 0): 
    print(i, end =" ") 
 
    
for a in range(50, 10, -2): 
    print(a, end =" ") 

for a in range(0.50, 0.10, 0.2): 
    print(a, end =" ") 


	
 
a=int(input('Enter the number'))
b=0
for c in range(1,a+1):
   b=b+c
print(b)


	
     
        
               
a = int (input("Enter the number of rows"))
for b in range(a):
    for i in range(b):
       print(b, end=" ")  
    print(" ")
    
    
    
a = int (input("Enter the number of rows"))
for b in range(a):
    for i in range(b):
       print("$", end=" ")  
    print(" ") 
    
    
    
    
for num in range(4):
    print(num)
else:
    print("Iteration is completed")



a=int(input("Enter the number")) 
b=0 
while b<10: 
    b = b + 1 
    c=a*b   
    print(a,'*',b,'=',c)


a = 1
while a<=5:
    print("INDIA")
    a=a+1
    
    


	
 
a=0
while a<10:
    print("INDIA")
    
    
a = 1
while a<6:
    print(a)
    a = a+1
else:
   print("terminated")


for a in "INDIA":
    if a == "D":
        break
    print(a)
print("The end")
    


a = 5                    
while a > 0:              
   print ('Curren value :', a)
   a = a-1
   if a == 2:
     break
print ("The end")



for a in "INDIA":
    if a == "D":
        continue
    print(a)
print("The end")





a = 5                    
while a > 0:              
  a = a -1
  if a == 2:
      continue
  print ('Current value :', a)
print ("The end")


for a in 'INDIA': 
   if a == 'D':
       pass
       print ('pass block')
   print ('Current a :', a)
print ("END")