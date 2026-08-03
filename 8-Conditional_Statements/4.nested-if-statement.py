# Nested If Statement

'''
Nested if statement means using one if statement inside another if statement 

it is used when first condition is depended on another condition 

when the if condition is true it check nested if condition 

'''

#Examples 
# 1.WAP to check given number is +ve,-ve or zero ,if it is positive check the number is even or odd

n=90
if n>0:
    print("postive")
    if n % 2==0:
        print("even")
    else:
        print("odd")
elif n<0:
    print("negative")
else:
    print("zero")


# 2.WAP to find the second greatest number using 3 numbers

a,b,c=56,34,89
if a>b and a>c:
    if b>c:
        print("b is second greatest number")
    else:
        print("c is second greatest number")
elif b>a and  b>c:
    if a>c:
        print("a is second greatest number")
    else:
        print("c is second greatest number")
else:
    if a>b:
        print("a is second greatest number")
    else:
        print("b is second greatest number")