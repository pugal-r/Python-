
print("Hello python")

print(10+20)

# Keywords in python

import keyword
print(keyword.kwlist)

print(len(keyword.kwlist))

print(keyword.iskeyword("if"))  #True
print(keyword.iskeyword("iF"))  #False
print(keyword.iskeyword("while")) #True
print(keyword.iskeyword("true")) #False

print(keyword.iskeyword("False")) #True
print(keyword.iskeyword("else")) #True
print(keyword.iskeyword("Else")) #False

# Identifier
a=10
print(a)  #10

# 123a=20
# print(123a) #invalid syntax

name = "sam"
print(name.isidentifier())

# n@me="ram"
# print(n@me) #invalid syntax

#to check valid identifier or not

name1="saran"
print(name1.isidentifier()) #True

salary="6500"
print(salary.isidentifier()) #False

