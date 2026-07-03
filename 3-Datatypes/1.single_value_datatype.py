# data types in python
# single value datatype 


# int

a=10
print(a) #10
print(type(a)) #<class 'int'>

a=-21
print(a) #-21
print(type(a)) #<class 'int'>

a=0
print(a) #0
print(type(a)) #<class 'int'>


# find ascii value of a character

a=65
print(chr(a)) #A

a=97
print(chr(a)) #a

b=122
print(chr(int(b))) #z

b=108
print(chr(b)) #l


# float

a=98.5
print(a) #98.5
print(type(a)) #<class 'float'>

a=-78.36
print(a) #-78.36
print(type(a)) #<class 'float'>


a=0.0
print(a) #0.0
print(type(a)) #<class 'float'>

# complex

value=5+3j
print(value) #(5+3j)
print(type(value)) #<class 'complex'>

print(value.real) #5.0
print(value.imag) #3.0

value1=10+5j
value2=11+4j
print(value1+value2) #(21+9j)


#Boolean

value=True
print(value)    #True
print(type(value))  #<class 'bool'>


value=False
print(value)    #False
print(type(value))  #<class 'bool'>

#ex
a=98
b=57
print(a>b)  #True
