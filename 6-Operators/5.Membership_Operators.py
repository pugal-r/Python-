#Membership opearors are used to check whether a value is present inside the sequense or not.

#types of membership operators 
#---> 1. in 
#---> 2.not in

#examples 
#String
s="python"
print('p' in s)     #True
print('j' in s)     #False


s1="python"
print('p' not in s)     #False
print('j'  not in s)     #true


#List
list=[10,20,30]
print(20 in list)    #True
print(98 in list)   #False

print(20 not in list)   
print(98 not in list)


#Tuple
tuple=(1,2,3,4,5)
print(3 in tuple)
print(7 in tuple)

print(3 not in tuple)
print(7 not in tuple)


#Set
set={10,20,30,40}
print(20 in set)
print(50 in set)

print(20 not in set)
print(50 not in set)



#Dictionary
dict={
    'name':'sam',
    'age':23
}

print('name' in dict)
print('sal' in dict)

print('name' not in dict)
print('sal' not in dict)