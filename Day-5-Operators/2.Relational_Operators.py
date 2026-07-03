#Relational operators are used to compare the values and check the conditions
#it will return output in the boolean format

print(98<100)   #True

print(98>100)   #False

print(98<=100)  #True

print(98>=98)   #True

print(98!=100)  #True

print(98==98)   #True


#Example using variable

a=45
b=30
print(a<b)

print(a>b)

print(a<=b)

print(a>=b)

print(a!=b)

print(a==b)

#1.Write a program to convert ASCII values into characters

value=97
print(chr(value))   #a

value=65
print(chr(value))   #A


#2.convert uppercase letter into lowercase letter

char="A"
print(chr(ord(char)+32))    #a


#3.convert lowercase letter into uppercase letter 

char="b"
print(chr(ord(char)-32))    #B