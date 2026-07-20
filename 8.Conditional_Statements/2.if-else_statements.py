'''
if else statement is the decision making statement.

which are used to execute the one block of code if a condition is true and another block of code the condition is false.

we have two statements in one condition then we make use of if-else statement.

without if statement cannot use else statement.

for one if statement we can use only one else statement

'''

#Syntax
'''
if condition:
    #true statement block
else:
    #false statement block
'''

# Example Programs 

#1.WAP to check the given number is positive or negative
a=-98
if a>0:
    print("positive")
else:
    print("negative")


#2.WAP to check if a number is Even or Odd
a=97
if a%2==0:
    print("EVEN")
else:
    print("ODD")


#3.WAP to check the greater of 2 numbers
a=98
b=100
if a>b :
    print("a is greater")
else:
    print("b is greater") 


#4.WAP to check if a person eligible for vote  or not
age=17
if age>=18:
    print("Eligible")
else:
    print("Not Eligible")


#5.WAP to check the character is vowel or consonant
ch="d"
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonent")


#6.