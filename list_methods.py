''' 
      #Accessing List Elements

list=[1,2,3,4,5,6,70,0,0,1,11,2,2]
print(list[2])  #3
print(list[6])  #70

  #Changing List Values
list=[1,2,3,3,2,1]
list[3]=4
print(list)

#list slicing
list=[1,2,2,2,2]
print(list[:5])



# Adds item at the end.

# #append

list=[1,1,1,1,2,2,2]
list.append(3)
print(list)

# short :Adds item at the end.
list=[3,1,2,5,7,8,6]
list.sort()
print(list)

#reverse()

# Reverses the list
list=[9,8,7,6,5,4,3,2,1]
list.reverse()
print(list)   

#insert

list=[1,2,4,5,6]
list.insert(2,3)   #list.insert(index, value)
print(list)

#pop(3)
list=[1,2,3,4,5]
list.pop(4)
print(list)


#remove()  Removes a specific value.

list=[1,1,2,3,4]
list.remove(1)
print(list)


# clear() Removes all items.

list =[1,2,3,4]
list.clear()
print(list)


# count count the number you give
list=[1,2,3,4,5,6,7,8,9]
print(list.count(7))



# index
list=[1,2,3,4]
print(list.index(1)) # it return index value

#extend

a=[1,4,7]
b=[8,5,2]
b.extend(a) # add one list to another
print(b)
print(a)
'''


