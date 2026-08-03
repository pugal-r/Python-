#--------List Methods in Python--------

# 1.append()
''' This method it is used to add new element at the end of the list'''
#Syntax:---> list.append(element)
#example:
nums=[10,20,30]
nums.append(40)
print(nums)


# 2.Extend()
''' This method it is used to add multiple elements from another collection.(iterable)'''
#Syntax:---> list.extend(iterable)
#Example:
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)


# 3.insert()
''' This method it is used to add new element at the specified index of the list'''
#Syntax:---> list.insert(index, element)
#Example:
nums=[10,20,30]
nums.insert(1, 15)
print(nums)


# 4.remove()
''' This method it is used to remove the first occurrence of the specified element from the list'''
#Syntax:---> list.remove(element)
#Example:
nums=[10,20,30]
nums.remove(20)
print(nums)


# 5.pop()
''' This method it is used to remove and return the element at the specified index of the list. If index is not specified, it removes and returns the last element of the list'''
#Syntax:---> list.pop(index)
#Example:
nums=[10,20,30]
nums.pop(1)
print(nums)
#--(or)----
nums.pop()
print(nums)


# 6.clear()
''' This method it is used to remove all elements from the list'''
#Syntax:---> list.clear()
#Example:
nums=[10,20,30]
nums.clear()
print(nums)


# 7.index()
''' This method it is used to return the index of the first occurrence of the specified element in the list'''
#Syntax:---> list.index(element)
#Example:
nums=[10,20,30]
index=nums.index(20)
print(index)


# 8.count()
''' This method it is used to return the number of occurrences of the specified element in the list'''
#Syntax:---> list.count(element)
#Example:
nums=[10,20,30,20]
count=nums.count(20)
print(count)


# 9.sort()
''' This method it is used to sort the elements of the list in ascending order by default. It can also be used to sort in descending order by passing the reverse=True argument'''
#Syntax:---> list.sort(reverse=False)
#Example:
nums=[30,10,20]
nums.sort()
print(nums)

#Example: Sorting in descending order
nums=[30,10,20]
nums.sort(reverse=True)
print(nums)


# 10.reverse()
''' This method it is used to reverse the order of the elements in the list'''
#Syntax:---> list.reverse()
#Example:
nums=[10,20,30]
nums.reverse()
print(nums)