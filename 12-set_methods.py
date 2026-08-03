#-------Set Methods in Python-------

# 1.add()
''' It is used to add a new element to the set collection'''
#Syntax:---> set_name.add(element)
#Example:
s={10,20,30}
s.add(40)
print(s)


# 2.update()
''' It is used to add multiple elements to the set collection'''
#Syntax:---> set_name.update([element1, element2, ...])
#Example:
s={10,20,30}
s.update([40,50,60])
print(s)


# 3.remove()
''' It is used to remove the specified element from the set collection. If the element is not present, it raises a KeyError'''
#Syntax:---> set_name.remove(element)
#Example:
s={10,20,30}
s.remove(20)
print(s)


# 4.discard()
''' It is used to remove the specified element from the set collection. If the element is not present, it does not raise any error'''
#Syntax:---> set_name.discard(element)
#Example:
s={10,20,30}
s.discard(20)
print(s)


# 5.pop()
''' It is used to remove and return an arbitrary element from the set collection. If the set is empty, it raises a KeyError'''
#Syntax:---> set_name.pop()
#Example:
s={10,20,30}
out=s.pop()
print(out)
print(s)


# 6.clear()
''' It is used to remove all elements from the set collection'''
#Syntax:---> set_name.clear()
#Example:
s={10,20,30}
s.clear()
print(s)


# 7.union()
''' It is used to return a new set that contains all unique elements from both sets'''
#Syntax:---> set_name.union(set2)
#Example:
s1={10,20,30}
s2={40,50,60}
s3=s1.union(s2)
print(s3)


# 8.intersection()
''' It is used to return a new set that contains only the elements that are present in both sets'''
#Syntax:---> set_name.intersection(set2)
#Example:
s1={10,20,30}
s2={20,30,40}
s3=s1.intersection(s2)
print(s3)


# 9.difference()
''' It is used to return a new set that contains the elements that are present in the first set but not in the second set'''
#Syntax:---> set_name.difference(set2)
#Example:
s1={10,20,30}
s2={20,30,40}
s3=s1.difference(s2)
print(s3)


# 10.symmetric_difference()
''' It is used to return a new set that contains the elements that are present in either of the sets but not in both'''
#Syntax:---> set_name.symmetric_difference(set2)
#Example:
s1={10,20,30}
s2={20,30,40}
s3=s1.symmetric_difference(s2)
print(s3)