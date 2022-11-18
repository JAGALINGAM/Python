#creation of dictonary

a = {5: 'VIT', '7': 'VELLORE'}
print (a)


a = {5:[1,2,3], 'V': 'VELLORE'}
print (a)

#value is repeated
a = {5:'Vellore', 'V': 'VELLORE'}
print (a)


#key is same
a = {5:'Vellore', 5: 'VELLORE'}
print (a)


#mixed key
a = {'vit' : 'vellore', 5:['p','y','t','h','o','n']}
print (a)


#dict is created using dict function
a = dict({'vit':'vellore', 2020: 2021})
print (a)

a = dict([('vit', 'vellore'), (2020, 2021)])
print (a)



#Acessing the element from the dictionary

a = {5: 'VIT', '7': 'VELLORE'}
print (a[5])

#Kay error is raised
a = {5: 'VIT', '7': 'VELLORE'}
print (a[4])

a = {5: 'VIT', '7': 'VELLORE'}
print (a.get ('7') )


#If the key is not found get function return none
a = {5: 'VIT', '7': 'VELLORE'}
print (a.get (4) )


a = dict([('vit', 'vellore'), ('2020', 2021)])
print (a['2020'])


#Changing and adding dictionary element
#if the key is already present, then updation happens on the key
#if the key is not present, add to the dictionary
a = {5: 'VIT', '7': 'VELLORE'}
print (a)
a[7] = 'IOE'
print (a)


a = {5: 'VIT', '7': 'VELLORE'}
print (a)
a['I'] = 'Institute'
print (a)



#Mehod clear
a = {5: 'VIT', '7': 'VELLORE'}
a.clear (5)   # no parameter to be passed
print (a)



#Copy
a = {5: 'VIT', '7': 'VELLORE'}
b = a.copy ()
print ('The original dictionary is:',a)
print ('The new dictionary is:',b)


a = {5: 'VIT', '7': 'VELLORE'}
b = a.copy ()
a.clear ()
print ('The original dictionary is:',a)
print ('The new dictionary is:',b)



a = {5: 'VIT', '7': 'VELLORE'}
b = a
a.clear ()
print ('The original dictionary is:',a)
print ('The new dictionary is:',b)


#dict.fromkeys

a = {'v', 'e', 'l', 'l', 'o', 'r', 'e'}
b = dict.fromkeys (a)
print (b)


a = {'v', 'e', 'l', 'l', 'o', 'r', 'e'}
b = 'vit'
c = dict.fromkeys (a, b)
print (c)

a = {'v', 'e', 'l', 'o', 'r'}
b = ['vit']
c = dict.fromkeys (a, b)
print (c)
b.append(5)
print (c)


a = {n: n*n for n in range(10)}
print(a)


a = {n: n*n for n in range(1,10)}
print(a)


a = {n: n*n for n in range(1, 10, 2)}
print(a)


a = {n: n*n for n in range(1,20) if n % 2 == 0}
print(a)



#get -  return the value for the specified key 
a = {5: 'VIT', '7': 'VELLORE'}
b = a.get(5)
print (b)



a = {5: 'VIT', '7': 'VELLORE'}
b = a.get(6, ['python'])
print (b)


a = {5: 'VIT', '7': 'VELLORE'}
b = a.get(6)
print (b)


a = {5: 'VIT', '7': 'VELLORE'}
b = a.get(6)
print (b)
print (a['6'])

#items
a = {5: 'VIT', '7': 'VELLORE'}
b = a.items()
print (b)


a = {5: 'VIT', '7': 'VELLORE'}
b = a.items()
print ("The elements of a:", b)
del[a[5]]
print ("The elements after delete:", b)

a = {5: 'VIT', '7': 'VELLORE'}
b = a.keys()
print ("The key of dictionary a is:", b)


a = {5: 'VIT', '7': 'VELLORE'}
b = a.keys()
print ("The key of dictionary a is:", b)
a.update({10:'Python'})
b = a.keys()
print ("The updated key of dictionary a is:", b)


a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = a.pop(10)
print ("The element poped from the dictionary a is:", b)
print ("The element of dictionary a is:", a)


a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = a.pop(11, ['India'])
print ("The key is not found and returns value is:", b)


a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = a.pop(11)
print ("The key is found and returns value is:", b)


a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = a.popitem()
print ("The last element of the dictionary a is:", b)
print ("The elements in the dictionary are:", a)


a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
a[12] = ['India']
print ("The elements in the dictionary are:", a)
b = a.popitem()
print ("The last element of the dictionary a is:", b)
print ("The elements in the dictionary are:", a)

a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = a.setdefault(5)
print ("The value of the key is:", b)


a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = a.setdefault(6, ['India'])
print ("The value of the key is:", b)
print ("The value of the key is:", a)

a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = a.setdefault(6)
print ("The value of the key is:", b)



a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = {20: 'India', 21: 'PAT', 22:'IPS'}
a.update(b)
print ("The updated dictionary of a is:", a)


a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = {5: 'India'}
a.update(b)
print ("The updated dictionary of a is:", a)



a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = a.values()
print ("The value of the dictionary  a is:", b)

a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = a.values()
print ("The value of the dictionary  a is:", b)
del[a[5]]
print ('The value of the dictionary after deletion is:', b)


a = {0: 'False', 1: 'False'}
print(all(a))

a = {1: 'True', 2: 'True'}
print(all(a))

a = {}
print(all(a))

a = {False:0,  1: 'True'}
print(all(a))


a = {1: 'False', 0: 'False'}
print(any(a))

a = {1: 'True', 0: 'False'}
print(any(a))

a = {}
print(any(a))



a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = len(a)
print ("The length of the dictionary a is:", b)


a = {5: 'VIT', '7': 'VELLORE', 10:'Python'}
b = len()
print ("The length of the dictionary a is:", b)


a = {'p','y','t','h','o','n'}
b = sorted(a, reverse=True)
print (b)

a = {'p': 5,'y':4,'t':3,'h':2,'o':1,'n':6}
b = sorted(a, reverse=True)
print (b)

a = {2: 5, 6:4, 8:3, 10:2, 11:1, 12:6}
b = sorted(a, reverse=True)
print (b)


def take_two(elem):
    return elem[1]
a = [(3, 2), (3, 4), (2, 2), (1, 3)]
b = sorted(a, key=take_two)
print('Sorted list:', b)




d = {'a': 100, 'b': 200, 'c': 300} 
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)
    
    
d = {'a': 100, 'b': 200, 'c': 300} 
d1 = {'a': 10, 'b': 20, 'c': 30}
for dict_key, dict_value in d.items():
   for dict_key, dict_value in d1.items():
       print(dict_key,'->',dict_value)
     #  print(dict_key1,'->',dict_value1)
	