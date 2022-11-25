a = ('a', 'b', 'c')
print (a)

a = (7, 8, 9)
print (a)

a = (7,'vit', 8.0)
print (a)

a = (7, 'vit', 8.0, (5, 'vellore', 9.0), [1, 2, 3])
print (a)



#Tuple packing
a = 7,'vit', 8.0
print (a)


a = 7,'vit', 8.0
b, c, d = a
print (b)
print (c)
print (d)


#One element in tuple - tricky

a = ('VIT')
print (a)
print(type(a))


a = ('VIT',)
print (a)
print(type(a))


a = 'VIT',
print (a)
print(type(a))



#Accessing element

a =('vit', 'vellore', 'python', 2020, 10.0, 10.0)
print (a[4])


a =('vit', 'vellore', 'python', 2020, 10.0)
print (a[5.0])

a =('vit', 'vellore', 'python', 2020, 10.0)
print (a[6])


a = (7, 'vit', 8.0, (5, 'vellore', 9.0), [1, 2, 3])
print (a [3])


a = (7, 'vit', 8.0, (5, 'vellore', 9.0), [1, 2, 3])
print (a [4] [1])



a = (7, 'vit', 8.0, (5, 'vellore', 9.0), [1, 2, 3])
print (a [-3])


a = (7, 'vit', 8.0, (5, 'vellore', 9.0), [1, 2, 3])
print (a [-2][-1])



a =('vit', 'vellore', 'python', 2020, 10.0)
print (a[0:4])


a =('vit', 'vellore', 'python', 2020, 10.0)
print (a[:])

a =('vit', 'vellore', 'python', 2020, 10.0)
print (a[0:])

a =('vit', 'vellore', 'python', 2020, 10.0)
print (a[:5])

a =('vit', 'vellore', 'python', 2020, 10.0)
print (a[2:5])


a = (7, 'vit', 8.0, (5, 'vellore', 9.0), [1, 2, 3])
print (a [0:3:2])


a = (7, 'vit', 8.0, (5, 'vellore', 9.0), [1, 2, 3])
print (a)
a[0] = 1
print (a)


#If the element is mutable datatypes (list) then it is changable
a = (7, 'vit', 8.0, (5, 'vellore', 9.0), [1, 2, 3])
print (a)
a[4][0] = 7
print (a)

a[3][0] = 10
print (a)



a = (7, 'vit', 8.0, (5, 'vellore', 9.0), [1, 2, 3])
print (a)
a[3][0] = 7
print (a)


#Tuple can be reassigned.
a = (7, 'vit', 8.0, ('5:5', 'vellore', '9.0'), [1, 2, 3])
print (a)
a = (7, 'vellore', 'python', [3, 4, 5])
print (a)




#Operation on Tuple
a = (9, 'vellore', [1,2, 3])
b = ('Python', 'INDIA')
c = a+b
print (c) 



a = (9, 'vellore', [1,2, 3])
print ('Repeat the elements of a by three times:', a * 3) 


a = ('1', '2', 2.0, 'vit')
del a[0]
print (a)

a = ('1', '2', 2.0, 'vit')
del a
print (a)


a  = ('vit', 'vellore', '1', '2', '3', 'vit', '1')
print (a.count ('vit'))

a  = ('vit', 'vellore', '1', '2', '3', 'vit', '1')
print (a.index ('1'))


a  = ('vit', 'vellore', '1', '2', '3', 'vit', '1')
print (a.remove('vit'))



a  = ('vit', 'vellore', '1', '2', '3', 'vit', '1')
print ('vit' in a)




a  = ('vit', 'vellore', '1', '2', '3', 'vit', '1')
print ('python' in a)


for a in ('vit', 'IOE', 'INDIA'):
    print ('great', a)
    
#To convert the tuple to string
a = ('v', 'i', 't', 'v', 'e')
b = ''.join(a)
print (b) 
    
a = ('v', 'i', 't', 'v', 'i', 't')
print ('The elements in the tuple are:', a)
b = a.count ('i')
print ('The number of elements in the tuple is:', b) 


# a = [('v', 'i', 't'), ('v', 'i', 't')]
# for t in a:
#     print ([t[:-1] + ('T',) for t in a])
    

a = ('v', 'i', 't', 'v', 'i', 't')
print ('The elements in the tuple are:', a)
b = a [2]
print ('The  elements in the tuple is:', b) 
c = a [-2]
print ('The  second last element in the tuple is:', c) 


a = tuple("Vellore")
print(a)
print(len(a))


a = ("Vellore", "VIT")
b = reversed(a)
print(tuple(b))


#create another tuple

a = (1, 2,3, 'vit', 'vellore')
b = reversed(a)
print(tuple(b))
   