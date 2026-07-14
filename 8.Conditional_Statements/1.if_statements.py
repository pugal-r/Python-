#one condition and only one statement.
#it allows to execute block of codes.
#if the condition is true it will print particular block of code ,it is called as true statement block

#syntax:
'''
if condition:
    #true Statement block
'''

#Examples:
#1.WAP to check if a number is positive
num=98
if num > 0:
    print(f'{num} is positive')



#2.WAP to check if a number is negative
num=-98
if num < 0:
    print(f'{num} is negative')


#3.WAP to check if a number is Even
num=98
if num % 2 ==0:
    print(f'{num} is Even')


#4.WAP to check if a number is odd
num=97
if num % 2 !=0:
    print(f'{num} is odd')


#5.WAP to check if a person eligible for vote 
age=25
if age >= 18:
    print("Eligible")


#6.WAP to check the number is greater than 100
num=198
if num > 100:
    print(f'{num} is greator than 100')


#7.WAP to check the character is vowel
ch='u'
if ch in "aeiouAEIOU":
    print(f'{ch} is vowel')


#8.WAP to check the character is consonent
ch='n'
if ch not in "aeiouAEIOU":
    print(f'{ch} is consonent')


#9.WAP to check the number is divisible by 3
num=27
if num % 3 ==0:
    print(f'{num} is divisible by 3')


#10.WAP to check the number is divisible by 5
num=25
if num % 5 ==0:
    print(f'{num} is divisible by 5')


#11.WAP to check the number is divisible by 3 and 5 ,if it is print FizzBuzz
num=15
if num % 3==0 and num % 5 ==0:
    print("FizzBuzz")


#12.WAP to check the given year is leap year
year=2024
if year%4==0 and (year%400==0 or year%100 !=0):
    print(f'{year} is leap year')


#13.