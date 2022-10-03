#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python code to demonstrate the working of
# del and pop()

# initializing list
lis = [2, 1, 3, 5, 4, 3, 8]

# using del to delete elements from pos. 2 to 5
# deletes 3,5,4
del lis[2 : 5]

# displaying list after deleting
print ("List elements after deleting are : ",end="")
for i in range(0, len(lis)):
	print(lis[i], end=" ")
	
print("\r")

# using pop() to delete element at pos 2
# deletes 3
lis.pop(2)

# displaying list after popping
print ("List elements after popping are : ", end="")
for i in range(0, len(lis)):
	print(lis[i], end=" ")


# In[2]:


# Python code to demonstrate the working of
# insert() and remove()

# initializing list
lis = [2, 1, 3, 5, 3, 8]

# using insert() to insert 4 at 3rd pos
lis.insert(3, 4)

# displaying list after inserting
print("List elements after inserting 4 are : ", end="")
for i in range(0, len(lis)):
	print(lis[i], end=" ")
	
print("\r")

# using remove() to remove first occurrence of 3
# removes 3 at pos 2
lis.remove(3)

# displaying list after removing
print ("List elements after removing are : ", end="")
for i in range(0, len(lis)):
	print(lis[i], end=" ")


# In[3]:


# Python code to demonstrate the working of
# sort() and reverse()

# initializing list
lis = [2, 1, 3, 5, 3, 8]

# using sort() to sort the list
lis.sort()

# displaying list after sorting
print ("List elements after sorting are : ", end="")
for i in range(0, len(lis)):
	print(lis[i], end=" ")
	
print("\r")

# using reverse() to reverse the list
lis.reverse()

# displaying list after reversing
print ("List elements after reversing are : ", end="")
for i in range(0, len(lis)):
	print(lis[i], end=" ")


# In[4]:


# Python code to demonstrate the working of
# extend() and clear()

# initializing list 1
lis1 = [2, 1, 3, 5]

# initializing list 1
lis2 = [6, 4, 3]

# using extend() to add elements of lis2 in lis1
lis1.extend(lis2)

# displaying list after sorting
print ("List elements after extending are : ", end="")
for i in range(0, len(lis1)):
	print(lis1[i], end=" ")
	
print ("\r")

# using clear() to delete all lis1 contents
lis1.clear()

# displaying list after clearing
print ("List elements after clearing are : ", end="")
for i in range(0, len(lis1)):
	print(lis1[i], end=" ")


# In[5]:


# Python code to demonstrate
# return the sum of values of dictionary
# with same keys in list of dictionary

import collections, functools, operator

# Initialising list of dictionary
ini_dict = [{'a':5, 'b':10, 'c':90},
			{'a':45, 'b':78},
			{'a':90, 'c':10}]


# printing initial dictionary
print ("initial dictionary", str(ini_dict))

# sum the values with same keys
result = dict(functools.reduce(operator.add,
		map(collections.Counter, ini_dict)))

print("resultant dictionary : ", str(result))


# In[6]:


s ="Medha"

li = []
l = len(s)
for i in range (0,l):
	li.append(s[i])


for i in range(0,l):
	for j in range(0,l):
		if li[i]<li[j]:
			li[i],li[j]=li[j],li[i]
j=""

for i in range(0,l):
	j = j+li[i]

print(j)


# In[7]:


amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))


# In[8]:


def double(integer):
	return integer*2


# driver code
integer_list = [1, 2, 3]

# Map method returns a map object
# so we cast it into list using list()
output_list = list(map(double, integer_list))

print(output_list)


# In[ ]:




