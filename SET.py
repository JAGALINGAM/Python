
#Creation of SET 

a = {1, 'vit', 8.0}
print (a)
print(type(a))



a = {1, 'vit', 8.0, '1', 'vit', '8.0'}
print (a)

a = {1, 'vit', 8.0, [1,2,3] }
print (a)

a = {1, 'vit', 8.0, {1:1,2:2,3:2} }
print (a)

a = {1, 'vit', 8.0, {1,2,3} }
print (a)

a = {}
print (type(a))

a = set ()
print (type(a))


a = set ({1, 2, 8.0,'vit'})
print(a)
print (type(a))

#Acessing element of SET
a = {1, 'vit', 8.0}
print (a[0])


a= {1, 'vit', 8.0}
print (a[:])

#using for loop access the element of set
a= {1, 'vit', 8.0}
for i in a:
    print(i)

#To add the single element
a = {1, 'vit', 8.0}
a.add (7)
print (a)


#To add the multiple elements
a = {1, 'vit', 10}
a.update({7,8,9})
print (a)


a = {1, 'vit', 10}
a.update([7,8,9])
print (a)


a = {1, 'vit', 10}
a.update([7,8,1,10], {2,3,6,8})
print (a)

a = {1, 'vit', 10}
a.update([7,8,1], {2:9,3:3,6:6,8:5})
print (a)



#Removing the element from the set

a = {1, 'vit', 10, 7, 9}
a.discard(9)
print(a)

a = {1, 'vit', 10, 7, 9}
a.discard(11)
print (a)


a = {1, 'vit', 10, 7, 9}
a.remove(9)
print (a)


a = {1, 'vit', 10, 7, 9}
a.remove(11)
print (a)


#SET OPERATION 


#UNION()

a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 9, 10}
c = a|b
print (c)

a = {1, 2, 3, 4, 5,6}
b = {6, 7, 8, 9, 10}
c = a.union(b)
print (c)

a = {6, 7, 8, 9, 5}
b = {1, 2, 3, 4}
c = b.union(a)
print (c)


#Intersection
a = {1, 2, 3, 4, 5, 7}
b = {6, 7, 8, 9, 10}
c = a & b
print (c)


a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 6, 7, 8, 9, 10}
c = a & b
print (c)

a = {1, 2, 3, 4, 5}
b = {1, 2, 3,5, 6, 7, 8, 9, 10}
c = {1,2,3,5}
d = a.intersection(b,c)
print (d)

#Difference
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 6, 7, 8, 9, 10}
c = a - b   #set of elements that are only in A not in B)
print (c)

a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 6, 7, 8, 9, 10}
c = b - a   
print (c)


a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 6, 7, 8, 9, 10}
c = a.difference(b)
print (c)

a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 6, 7, 8, 9, 10}
c = b.difference(a)
print (c)

#Symmetric Difference

#Excluding Intersection
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 6, 7, 8, 9, 10}
c = a ^ b
print (c)

a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 6, 7, 8, 9, 10}
c = a.symmetric_difference (b)
print (c)


a = {1, 2, 3, 4, 5}
a.add(7)
print ('after adding element:', a)

a = {1, 2, 3, 4, 5}
a.add(1)
print ('after adding element:', a)


a = {1, 2, 3, 4, 5}
a.clear()
print ('after clearnig element:', a)


a = {1, 2, 3, 4, 5}
print ('The element of a is:', a)
b = a.copy ()
print ('The element of b is:', b)
b.add(8)
print ('after adding element:', b)
print ('after adding element:', a)


#difference of A and B  - set of elements that exists only in SET A but not in B

#C =b.difference_upadate(a)

#it changes the set which is calling difference_update

#return none - indicates object is changed.


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9}
c = b.difference_update(a)
print ('The element of a is:', a)
print ('The element of b is:', b)
print ('After set_difference:', c)


#update the set which is called the method intersection_update

#It return NONE
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9}
d = a.intersection_update(b)
print ('The element of a is:', a)
print ('The element of b is:', b)
print ('The element of d is :', d)


a = {1, 2, 3, 4, 5}
b = {1,2,3,4, 5, 6, 7, 8, 9}
c = {1, 2, 3, 4, 5, 10, 11}
d = a.intersection_update(b, c)
print ('The element of a is:', a)
print ('The element of b is:', b)
print ('The element of c is :', c)
print ('The element of d is :', d)


#Disjoint SET returns TRUE if two sets are disjoint, otherwise FALSE


#DISJOINT - Two sets are disjoint, if two sets do not have common elements


a = {12, 11}
b = {4, 5, 6, 7, 8, 9}
c = {1, 2, 3, 10, 11}
d = a.isdisjoint(b)
print ('The element of a is:', a)
print ('The element of b is:', b)
print ('The element of c is :', c)
print ('The element of d is :', d)



a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9}
c = {1, 2, 3, 4, 5}
d = a.isdisjoint(c)
print ('The element of a is:', a)
print ('The element of b is:', b)
print ('The element of c is :', c)
print ('The element of d is :', d)

a = {1, 2, 3, 4, 5}
b = { 6, 7, 8, 9}
c = {1, 2, 3, 4, 5}
d = a.isdisjoint(b)
print ('The element of a is:', a)
print ('The element of b is:', b)
print ('The element of c is :', c)
print ('The element of d is :', d)



#Subset - return TRUE, if all elements of a SET are present in another SET 
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9}
d = a.issubset(b)
print ('The element of a is:', a)
print ('The element of b is:', b)
print ('The element of d is :', d)


a = {1, 2, 3, 4, 5}
b = {1,2,3, 4, 5, 6, 7, 8, 9}
d = a.issubset(b)
print ('The element of a is:', a)
print ('The element of b is:', b)
print ('The element of d is :', d)


#Finds the symmetric difference b/w two sets

#The symmetric difference of two sets A and B is the set of elements that are either in A or B but not in their intersection
a = {1, 2, 3, 4, 5, 10, 11, 12}
b = {1,2,3, 4, 5, 6, 7, 8, 9}
c = {6, 7, 8, 9}
d = a.symmetric_difference_update(b)
print ('The element of a is:', a)
print ('The element of b is:', b)
print ('The element of d is :', d)





a = {10, 20, 30, 40, 50, 60}
#Find maximum value
print(max(a))
#Find minimum value
print(min(a))
