#---------Dictionary Methods in Python--------------

# 1.get()
''' It is used to find the value of given key
    It key not found it will display none.
'''
#Syntax:---> dic.get(key)
#Example:
data={'bangalore':25,'Goa':35,'chennai':58}
print(data.get('chennai'))      #35

#Another Example:
data={'bangalore':25,'Goa':35,'chennai':58}
print(data.get('Delhi'))        #None



# 2.update()
'''This method it is used to obtain old value with new value
   If key not found it will add to existing to dictionary
'''
#Syntax:---> dic.update(value)
#Example:
data={'bangalore':25,'Goa':35,'chennai':58}
data.update({'pune':65})
print(data)

#Another Example:
data={'bangalore': 25, 'Goa': 35, 'chennai': 58, 'pune': 65}
data['pune']=120
print(data)


# 3.items()
''' This method it is used to return the key and value of dictionary in tuple format'''
#Syntax:---> dic.items()
#Example:
data={'bangalore':25,'Goa':35,'chennai':58}
print(data.items())


# 4.keys()
''' This method it is used to return the keys of dictionary in tuple format'''
#Syntax:---> dic.keys()
#Example:
data={'bangalore':25,'Goa':35,'chennai':58}
print(data.keys())



# 5.values()
''' This method it is used to return the values of dictionary in tuple format'''
#Syntax:---> dic.values()
#Example:
data={'bangalore':25,'Goa':35,'chennai':58}
print(data.values())

