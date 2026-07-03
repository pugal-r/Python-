#user input 

a=input("Enter the value:")
print(a)        
print(type(a))     
#output:
# Enter the value:56
# 56
# <class 'str'>


#input statements always returns string type of data 
#example
n=input("Enter value 1:")
m=input("Enter value 2:")
print(n+m)
#output:
# Enter value 1:10
# Enter value 2:20
# 1020 ---> add 2 strings 10+20=1020



#So Typecasting is required for numeric operations
#Example:1

b=int(input("Enter the value:"))
print(b)
print(type(b))
#output:
# Enter the value:75
# 75
# <class 'int'>


#example:2
x=int(input("Enter value 1:"))
y=int(input("Enter value 2:"))
print(x+y)
# output:
# Enter value 1:10
# Enter value 2:20
# 30 