a = 1
if a > 0:
   print("The number positive")
   print("END")

grade = int(input('enter the grade'))
if grade >= 70:
    print ('pass')
    print('fail')
    


a = -1
if a > 0:
    print("The number positive")
print("END")




grade = int(input('enter the grade'))
if grade >= 70:
   print('pass')
else:
   print('fail')
    
   
a = int(input('enter the number'))
if a >= 0:
    print ("The number is positive")
else:
   print ("The number is negative")


a = int(input('enter the number'))
if a > 0:
   print ("The number is positive")
elif a == 0:
   print ("The number is zero")
else:
   print ("The number is negative")


a = int(input('enter the number'))
if a > -1:
	if a == 1:
        
        
		print ("The number is zero") 
	else: 
		print ("The number is positive")
else:
	print ("The number is negative") 



a = int(input("enter the Grade:"))
if a >= 95:
   print ('Grade of S')
elif a >= 90:
    print ('Grade of A')
elif a >= 80:
    print ('Grade of B')
elif a >= 70:
   print ('Grade of c')
elif a >= 60:
   print ('Grade of D')
else:
    print ('Grade of F')
    
    
mark1 = int(input("Enter the mark one:"))
mark2 = int(input("Enter the mark two:"))
if (mark1 >= 90 or mark2 >= 90):
    print ("GOOD")
    if (mark1 >= 90 and mark2 >= 90):
        print ("EXCELLENT")
else:
    print ("NEED TO IMPROVE")
  



""" Write a python code to print the batsman 
is eligible for the man of the series
Total number of match is 5, if the average 
score is greater than or equal to 90, 
then award man of match"""

run1 = int(input("Enter first match run"))
run2 = int(input("Enter second match run"))
run3 = int(input("Enter third match run"))
run4 = int(input("Enter fourth match run"))
run5 = int(input("Enter fifth match run"))

total  =run1+run2+run3+run4+run5
avg = total/5

if(avg>=90):
    print("Man of the series")
else:
    print("No")






""" Write a python program 
to print the man of series, 
eligible for man of the series is:
in total of 5 match, player 
to be scored average of 90 runs 
and player to be wicket holder 
of 10 and above."""

run1 = int(input("Enter first match run"))
run2 = int(input("Enter second match run"))
run3 = int(input("Enter third match run"))
run4 = int(input("Enter fourth match run"))
run5 = int(input("Enter fifth match run"))
wicket = int(input("Enter the number of wickets in the series"))
total  =run1+run2+run3+run4+run5
avg = total/5

if(avg>=90 and wicket>=10):
    print("Man of the series")
else:
    print("NO")


a = int(input("Enter the number for a:"))
b = int(input("Enter the number for b:"))
c = int(input("Enter the number for c:"))

if(a>b):
    if(a>c):
        print("A is greater")
    else:
        print("C is greater")
elif(b>c):
    print("B is greater") 
else:
     print("C is greater")
     
     
a = int(input("Enter the number for a:"))
b = int(input("Enter the number for b:"))
c = int(input("Enter the number for c:"))

if(a>b):
    if(a>c):
        print("A is greater")
    else:
        print("C  is greater")
elif(b>c):
      print("B is greater")
else:
     print("C is greater")   
  
first_grad = int(input("If you are FG enter 1 else 0:"))
math = int(input("Enter the math mark"))
phy = int(input("Enter the phy mark"))                
che = int(input("Enter the che mark"))  

if(math<=0 or phy<=0 or che<=0):
    print("invalid input")
else:
    total = math+phy+che
    avg = total/3
if(first_grad and avg>=90):
    print("The student is eligible for scholarship")
else:
    print("The student is not eligible ")
    
               
    
    

        




 
    
















    
    
    
first_graduate = int(input("Are you first graduate, enter 1 for yes, 0 for no"))
phy = int(input("Enter the physics mark:"))
che = int(input("Enter the chemistry mark:"))
mat = int(input("Enter the math mark:"))
total = phy+che+mat
avg = total/3

if(phy==0 or che==0 or mat==0):
    print("Invalid")
elif(first_graduate == 1 and avg >=90):
    print("The candidate is eligible for scholarship")
else:
    print("The candidate is not eligible for scholarship")
    
    

            






first = int(input("Are you the first garduate: type 1 for Yes and 0 for No"))
print ('The graduate info', first)
phy_mark = float(input("Enter the physics mark"))
print ("Physics mark", phy_mark)
che_mark = float(input("Enter the chemistry mark"))
print ("Chemistry mark", che_mark)
mat_mark = float(input("Enter the Mathematics mark"))
print ("Mathematics mark", mat_mark)
total_mark = phy_mark + che_mark + mat_mark
print ("The total marks", total_mark)
if phy_mark <0 or che_mark <0 or mat_mark <0:
    print ('Input is not valid')
else:
    average = total_mark/3
    print ("The average marks", average)
    if (first == 1 and average >= 98):
        print ('candidate is qualified for the scholarship')
    else:
        print ('candidate is not qualified for the scholarship')


x = int(input("Enter the number of x"))
y = int(input("Enter the number of y"))
z = int(input("Enter the number of z"))
if(x==0 or y==0 or z==0):
    print("Invalid input")
elif x>y and x>z: 
    print ("x is greatest")  
elif y>z:
    print ("y is greatest")                             
else:
    print ("z is greatest")
        
#a = int(input("Enter a number A:"))
#b = int(input("Enter a number B:"))
#c = int(input("Enter a number C:"))
#if a/b >1 and a/c >1 :
#    print("A is greater")
#elif b/c >1 and b/c >1 :
#    print("B is greater")
#else :
#    print("C is greater")




    

    
    
    