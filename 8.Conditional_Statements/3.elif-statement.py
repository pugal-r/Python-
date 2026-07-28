'''
the elif statement in python used to check multiple condition sequencetually

elif statement also called else-if-statements 

when a if condition is true it will print TSB of if condition 

when a if condition is false it will be check the elif condition if an elif condition true it will print TSB of an elif statement

when a elif condition is false it will print the FSB in the else statement 

for one if condition we can use multiple elif condition 

else statement is optional 

'''


#Syntax

'''
if <condition> :
    TSB
elif <condition> :
    TSB
elif <condition> :
    TSB
else:
    FSB

'''

# Example Programs 
# 1.WAP to check the given number is positive , negative or zero

n=98
if n ==0:
    print("Number is Zero")
elif n>0:
    print("Number is Positive ")
elif n<0:
    print("Number is Negative ")
else:
    print("Program ended")


# 2. WAP to check the given number is odd ,even or zero

n=97
if n %2 ==0:
    print("Even")
elif n%2 !=0:
    print("Odd")
else:
    print("Zero")


# 3.WAP to calculate student grade using marks

mark=72
if mark >=85:
    print("Grade A")
elif mark >=75:
    print("Grade B")
elif mark >=65:
    print("Grade C")
elif mark >=35:
    print("Grade D")
else:
    print("Fail")


# 4.WAP to find the large number out of 3 Numbers 
a=98
b=128
c=59
if a>b and a>c:
    print("a is the largest")
elif b>a and b>c:
    print("a is the largest")
else:
    print("c is largest")


# 5.WAP to check given character is uppercase or lowercase or digit or special symbol
char=input("Enter the character:")
if "A" <= char <= "Z":
    print("Uppercase letter")
elif "a" <= char <= "z":
    print("Lowercase letter")
elif "0" <= char <= "9":
    print("it is a Digit")
else:
    print("it is Special Symbol")


#6.WAP to perform Simple calculator Operation

print("---simple calculator-----")
a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
print("Choice Operation")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("Enter the Operation:"))

if choice == 1:
    add=a+b
    print("Addition of 2 numbers:",add)
elif choice == 2:
    sub=a-b
    print("Substraction of 2 numbers:",sub)
elif choice == 3:
    mul=a*b
    print("Multiplication of 2 numbers:",mul)
elif choice == 4:
    div=a/b
    print("Division of 2 numbers:",div)
else:
    print("Invalid Choice ")