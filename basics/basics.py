import random
import sys
import os

print("Hello World")

#A comment

'''
Multiline comment
'''

name = "Juan"
print('hey ' + name)

#Arithmetic
print("5+2 =", 5+2)
print("5-2 =", 5-2)
print("5*2 =", 5*2)
print("5/2 =", 5/2)
print("5%2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)

#Strings
print("%s %s %s"%("hey","you","yes"))
print("don't repeat yourself\n"*3)

#Lists
a_list = ['first','second','third','fourth']
print(a_list)
print(a_list[1])

sublist = a_list[0:2]
print(sublist)

list_of_lists = [a_list, sublist]
print(list_of_lists)

list_of_lists.append('some other thing')
print(list_of_lists)
list_of_lists.remove('some other thing')

list_of_lists.insert(1, 'inserted item')
print(list_of_lists)
list_of_lists.remove('inserted item')

list_of_lists.insert(0,['a'])
list_of_lists.insert(0,['x'])

list_of_lists.sort()
print('sorted list:',list_of_lists)

del list_of_lists[1]
print(list_of_lists)

list_of_lists.reverse()
list_of_lists[1].reverse()
print(list_of_lists)

print(len(list_of_lists))


