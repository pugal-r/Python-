#------While Loop in Python -----------

'''
while loop it is used to execute same set of instruction multiple times until the given condition is false.

in while loop initialization of loop variable and updation of loop statement is mandatory.

if do not initialize the looping variable then control will through an error.

if do not update the looping variable if will get execute like an infinite loop.
'''

#Syntax for while loop
'''
initialization
while condition:
    #block of code / statement
    updation
else:
    #statement
'''

#Example Programs:

#1.print number from 0 to 3
i=0
while i<= 3:
    print(i)
    i=i+1
print("--------------------------------------------------------------")

#2.numbers from 5 to 1
i=5
while i>=1:
    print(i)
    i=i-1
print("--------------------------------------------------------------")

#3.print hello world in 3 time 
i=1
while i<=3:
    print("Hello world")
    i+=1
print("--------------------------------------------------------------")

#4.print even numbers in 1 to 10
i=2
while i<=10:
    print(i)
    i=i+2
print("--------------------------------------------------------------")

#or using if 
i=0
while i<=10:
    if i%2==0:
        print(i)
    i=i+1
print("--------------------------------------------------------------")

#5.odd number in 1 to 10
i=1
while i<=10:
    print(i)
    i=i+2
# or using if 
i=0
while i<=10:
    if i%2!=0:
        print(i)
    i=i+1
print("--------------------------------------------------------------")

#6.print the 2 table upto 10
i=1
n=2
while i<=10:
    print(f'{i} * {n} = {i*n}')
    i+=1
print("--------------------------------------------------------------")

#7.sum of first 5 natural number
i=1
sum=0
while i<=5:
    sum=sum+i
    i+=1
print(sum)
print("--------------------------------------------------------------")

#8.sum of even numbers from 1 to 10
i=1
sum=0
while i<=10:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)
print("--------------------------------------------------------------")

#9.Sum of odd numbers from 1 to 20 while loop with if condition
i=1
sum=0
while i<=20:
    if i%2!=0:
        sum=sum+i
    i=i+1
print(sum)
print("--------------------------------------------------------------")

#10.no.of digit s present in a given number
n=23451
count=0
while n>0:
    count+=1
    n=n//10
print(count)
print("--------------------------------------------------------------")

#11.list of elements even or odd
l=[20,1,3,6,4,9,34]
i=0
while i< len(l):
    if l[i]% 2==0:
        print(f'{l[i]} is even')
    else:
        print(f'{l[i]} is odd')
    i+=1
print("--------------------------------------------------------------")

#12.sequence of numbers from 15 to 21
n=15
while n<=21:
    print(n)
    n+=1
print("--------------------------------------------------------------")

#13.print number divisible by 3 from 1 to 11
num=1
while num<=11:
    if num % 3==0:
        print(num)
    num+=1
print("--------------------------------------------------------------")

#14.print numbers divisible by 3 and 5 from 10 to 40 
n=10
while n<=40:
    if n%3==0 and n%5==0:
        print(n)
    n+=1
print("--------------------------------------------------------------")

#15.print last digits of number present b/w 6 to 9 from 25 t0 29
n=25
while n <=29:
    d=n%10
    if d >=6 and d <=9:
        print(d)
    n+=1
print("--------------------------------------------------------------")


#16.print the odd digit from the given number
n=8743
while n>0:
    d=n%10
    if d%2 !=0:
        print(f"odd number is {d}")
    n=n//10
print("--------------------------------------------------------------")

#17.print even digit from given number if the digit more than 4
num=8743
while num>0:
    d=num%10
    if d%2==0 and d>4:
        print(f"even digit more than 4 is {d}")
    num=num//10
print("--------------------------------------------------------------")

#18.print digit which are grater than 4
n=43876
while n>0:
    d=n%10
    if d>4:
        print(d)
    n=n//10
print("--------------------------------------------------------------")

#19.print sum of digits present in the number
num=48617
sum=0
while num>0:
    d=num%10
    sum+=d
    num=num//10
print(sum)
print("--------------------------------------------------------------")

#20.print sum of even digits in given number
num=48617
sum=0
while num>0:
    d=num%10
    if  d%2==0:
        sum+=d
    num=num//10
print(sum)
print("--------------------------------------------------------------")

#21.print product of odd digits in given number
num=4732
product=1
while num>0:
    d=num%10
    if d%2 !=0:
        product*=d
    num=num//10
print(product)
print("--------------------------------------------------------------")

#22.print product of odd digit and sum of even digits in given number
num=4732
product=1
sum=0
while num>0:
    d=num%10
    if d%2 !=0:
        product*=d
    elif d%2==0:
        sum+=d
    num=num//10
print("product od odd is:",product)
print("sum of even is:",sum)
print("--------------------------------------------------------------")

#23.print sum of all digit and product of all digit
num=4732
sum=0
product=1
while num>0:
    d=num%10
    sum+=d
    product*=d
    num=num//10
print("sum of all digit:",sum)
print("product of all digit:",product)
print("--------------------------------------------------------------")


#24. to reverse a number
num=12345
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10
print(rev)
print("--------------------------------------------------------------")

#25.to check given number is palindrome or not
num=121
rev=0
temp=num
while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10
if temp==rev:
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")
print("--------------------------------------------------------------")


#26.to print highest digit from the given numbers
num=586
high=0
while num>0:
    d=num%10
    if d>high:
        high=d
    num=num//10
print(high)
print("--------------------------------------------------------------")


#27. to print sum of digit from given number is the number is odd or even 
num=1234
sum=0
while num >0:
    d=num%10
    sum+=d
    num=num//10
if sum %2==0:
    print("Sum is even number, the sum is:",sum)
else:
    print("Sum is odd number , the Sum is:",sum)
print("--------------------------------------------------------------")


#28.To print fibonacci sequence upto n terms
n=6
a,b=0,1
count=0
while count < n:
    print(a ,end="")
    a,b=b,a+b
    count+=1
print("--------------------------------------------------------------")


#29.sum of all numbers in given list
list=[20,41,36,87,55]
sum=0
i=0
while i < len(list):
    sum+=list[i]
    i+=1
print("sum of all numbers",sum)
print("--------------------------------------------------------------")


# 30.Extract vowels and digit from the string
s="education@1234"
i=0
while i < len(s):
    if s[i] in "AEIOUaeiou" or (s[i]>="0" and s[i]<="9"):
        print(s[i],end="")
    i+=1
print("--------------------------------------------------------------")

#31. print the factors of an number
n=6
i=1
while i<=n:
    if n%i==0:
        print(i)
    i+=1
print("--------------------------------------------------------------")


#32.to print sum of factors
n=6
i=1
sum=0
while i<=n:
    if n%i==0:
        sum+=i
    i+=1
print(sum)
print("--------------------------------------------------------------")


#33.find factorial of an number
n=5
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(fact)
print("--------------------------------------------------------------")

#34.reverse a string
s="kavi"
rev=""
i=len(s)-1
while i>=0:
    rev=rev+s[i]
    i-=1
print(rev)
print("--------------------------------------------------------------")


#35.strong number -->Sum of factorial of digits equal to given number
n=145
temp=n
sum=0
while n>0:
    d=n%10
    fact=1
    i=1
    while i<=d:
        fact*=i
        i+=1
    sum+=fact
    n=n//10
if temp==sum:
    print("It is a strong number ")
else:
    print("It is not a strong number")
print("--------------------------------------------------------------")

#36.perfect number ----> sum of divisors equal to the given number
n=6
i=1
sum=0
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print("Perfect number")
else:
    print("Not a perfect number")
print("--------------------------------------------------------------")


#37.spy number ----> a given number of sum of digit equal to product of digit
n=1124
sum=0
product=1
while n>0:
    d=n%10
    sum+=d
    product*=d
    n=n//10
if sum==product:
    print("Spy number ")
else:
    print("not a spy umber")
print("--------------------------------------------------------------")


#38.Neon Number --> sum of digits of square ,equal to the given number
n=9
sq=n*n
sum=0
while sq>0:
    d=sq%10
    sum+=d
    sq=sq//10
if sum==n:
    print("neon number")
else:
    print("not a neon number")
print("--------------------------------------------------------------")

#39.Harshad number ---> sum of digits divisible by given number 
n=12
temp=n
sum=0
while n>0:
    sum=sum+(n%10)
    n=n//10
if temp%sum==0:
    print("Harshad number")
else:
    print("not a harshad number")
print("--------------------------------------------------------------")

#40.prime number---> a given number divisible by 1 and itself 
n=7
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print("Prime number ")
else:
    print("Not a prime number")
print("--------------------------------------------------------------")


#41.Armstrong number---> a set of given number that sum of each number cubes equal to the given number
n=153
temp=n
cube=0
length=len(str(n))
while n>0:
    d=n%10
    cube=cube+d**length
    n=n//10
if temp==cube:
    print("Armstrong number")
else:
    print("not a Armstrong number")
print("--------------------------------------------------------------")

#42.validate username and password
un="Pugal"
p="1234"
i=0
while i<3:
    user=input("Enter username:")
    password=(input("Enter password:"))
    if un==user and p==password:
        print("login Successfully")
        break
    else:
        print("Invalid")
    i+=1
else:
    print("Account Locked")


