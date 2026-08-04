#---------For Loop In Python------------------

'''
A for loop in python it is use to iterate over a sequence , such as (list,tuple,string,set,dict)

a for loop in python it is used to execute the block of code repeatly for each element in the sequence.

it commonly used when the no.of iteration are known or finite.

In for loop initialization and updation of the looping variable is automatic.

'''

#Syntax for loop
'''
for variable in sequence :
    #block of code 
else:
    #statements

'''

#Example Programs:

#for loop 
for i in range(6):
    print(i)
else:
    print("Loop is over")   
print("---------------------------------------------")


#1.print 1 to 5
for i in range(1, 6):
    print(i)    
print("---------------------------------------------")


#2.print even numbers from  1 to 10
for i in range(1,10):
    if i % 2==0:
        print(i)
print("---------------------------------------------")  


#3.print odd numbers from 1 to 10
for i in range(1,10):
    if i % 2 !=0:
        print(i)
print("---------------------------------------------")


#4.print sum of 10 natural numbers
sum=0
for i in range(1,11):
    sum+=i
print("Sum is:",sum)
print("---------------------------------------------")


#5.print multiplication table of 5
n=5
for i in range (1,11):
    print(f"{i} * {n} = {i*n}")
print("---------------------------------------------")


#6.find count of an number from 1 to 10
count=0
for i in range(1,11):
    count+=1
print("Count is:",count)
print("---------------------------------------------")


#7.print square of numbers from 1 to 5
for i in range(1,6):
    print(i*i)
print("---------------------------------------------")


#8.print cube of numbers from 1 to 5
for i in range(1,6):
    print(i*i*i)
print("---------------------------------------------")


#9.print characters of an string
string="Python"
for ch in string:
    print(ch)
print("---------------------------------------------")


#10.print the count of the string
string ="Pugazhendhi"
count=0
for ch in string:
    count+=1
print("Count of string is:",count)
print("---------------------------------------------")


#11.print sum of even numbers from 1 to 20
sum=0
for i in range(1,21):
    if i %2 ==0:
        sum+=i
print("Sum of even numbers is:",sum)
print("---------------------------------------------")


#12.print sum of odd numbers from 1 to 20
sum=0
for i in range(1,21):
    if i %2 !=0:
        sum+=i
print("Sum of odd numbers is:",sum)
print("---------------------------------------------")


#13.print the numbers divisible by 4 from 1 to 30
for i in range(1,31):
    if i %4 ==0:
        print(i,end=" ")
print("---------------------------------------------")


#14.print factorial of a number 5
fact=1
for i in range(1,6):
    fact*=i
print("Factorial is:",fact)
print("---------------------------------------------")


#15.print reverse of a string
string="Pugazhendhi"
rev=""
for ch in string:
    rev=ch+rev
print("Reverse string is:",rev)
print("---------------------------------------------")


#16.count vowels in a string
string="Pugazhendhi"
count=0
for ch in string:
    if ch in "AEIOUaeiou":
        count+=1
print("Count of vowels is:",count)
print("---------------------------------------------")


#17.print the ASCII values of an characters
string="ABCD"
for ch in string:
    print(f"ASCII value of {ch} is : {ord(ch)}")
print("---------------------------------------------")


#18.print the elements from the list
a=[1,2,3,4,5]
for i in a:
    print(i)
print("---------------------------------------------")


#19.print count of the elements present in the list
a=[10,20,30,40,50]
count=0
for i in a:
    count+=1
print("count of elements:",count)
print("---------------------------------------------")


#20.find sum of list elements
a=[1,2,3,4,5]
sum=0
for i in a:
    sum+=i
print("Sum of list elements is:",sum)
print("---------------------------------------------")  


#21.find the highest value from the list    
a=[10,20,5,40,15]
high=a[0]
for i in a:
    if i > high:
        high=i
print("Highest value is:",high)
print("---------------------------------------------")


#22.find the lowest value from the list
a=[10,20,5,40,15]
low=a[0]
for i in a:
    if i < low:
        low=i
print("Lowest value is:",low)
print("---------------------------------------------")


#23.count even numbers from the list
a=[1,2,3,4,5,6,7,8,9,10]
count=0
for i in a:
    if i %2 ==0:
        count+=1
print("Count of even numbers is:",count)
print("---------------------------------------------")


#24.count of digits ina given numbers
n=34526
count=0
for i in str(n):
    count+=1
print("Count of digits is:",count)
print("---------------------------------------------")


#25.sum of digits in a given number
n=34526
sum=0
for i in str(n):
    sum+=int(i)
print("Sum of digits is:",sum)
print("---------------------------------------------")


#26.check given string palindrome or not
string="madam"
rev=""
for ch in string:
    rev=ch+rev
if rev==string:
    print("Palindrome")
else:
    print("not a palindrome")


#27.store characters from one string to another string
s="Good Evening"
s1=""
for ch in s:
    s1=s1+ch
print(s1)


#28.store alphabets from one string to another string
string="python123.com"
str1=""
for ch in string:
    if ch.isalpha():
        str1=str1+ch
print(str1)


#29.store and print the alphabets and digits from the given string
string="python1234.com"
str=""
num=""
for ch in string:
    if ch.isalpha():
        str+=ch
    elif ch.isdigit():
        num+=ch
print("alphabets:",str)
print("digits:",num)


#30.convert uppercase character to lowercase 
str="Hello Python"
out=""
for ch in str:
    if "A"<=ch <="Z":
        low=ch.lower()
        out=out+low
    else:
        out=out+ch
print(out)


#31.to extract vowels , consonant, digits from the string
string="HelloPython12345"
vow=""
con=""
num=" "
for ch in string:
    if ch in "AEIOUaeiou":
        vow=vow+ch
    elif ch not in "AEIOUaeiou" and not ch.isdigit():
        con=con+ch
    elif ch.isdigit():
        num=num+ch

print("vowels:",vow)
print("consonants:",con)
print("Digits:", num)


#32.to remove duplicate values in the list
list=[1,2,3,2,4,2,3,5,4]
seen=[]
for i in list:
    if i not in seen:
        seen=seen+[i]
print(seen)


#33.to get following output:-->a4b6c2d1
string="aaaabbbbbbccd"
out=""
for i in string:
    if i not in out :
        out=out+i+ str(string.count(i))
print(out)


#34.to print even and odd numbers in different list
list=[1,6,3,7,9,1,12,45,63]
even=[]
odd=[]
for i in list:
    if i % 2==0:
        even.append(i)
    else:
        odd.append(i)
print("even list:",even)
print("odd list:",odd)


#35.to reverse a list given below
#i/p:--> ["Hii","How","are","you"]
#o/p:--> ["uoY","era","woH","iiH"]

list=["Hii","How","are","you"]
rev=[]
for i in list[::-1]:
    rev.append(i[::-1])
print(rev)


#36.extract the string starting with vowels
list=["apple","grapes","mango","orange"]
vow=[]
for i in list:
    if i[0] in "AEIOUaeiou":
        vow.append(i)
print(vow)


#37.to print the given number is prime number or not
num=7
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("Prime number")
else:
    print("not a prime number")


#38.print the prime numbers from 1 to 30
for n in range(1,31):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print(n)


#39.palindrome numbers from 11 to 100
for num in range(11,101):
    a=num
    r=0
    temp=a
    while a!=0:
        d=a%10
        r=r*10+d
        a//=10
    if temp==r:
        print(num ,end=",")


#40.check the number is armstrong number or not
num=153
cube=0
length=len(str(num))
for i in str(num):
    cube=cube+int(i)**length
if cube==num:
    print("it is a armstrong")
else:
    print("it is not a armstrong")


#41.strong number---> Sum of factorial of digits equal to given number
n=145
temp=n
sum=0
while n>0:
    d=n%10
    fact=1
    for i in range(1,d+1):
        fact*=i
    sum+=fact
    n//=10
if sum==temp:
    print("Strong number")
else:
    print("not a Strong number")



#42.Strong Number using nested for loop
num=145
sum=0
for i in str(num):
    fact=1
    for j in range(1,int(i)+1):
        fact*=j
    sum=sum+fact
if sum==num:
    print("Strong number")
else:
    print("not a Strong number")


#43.Find the second largest number in the list
list=[10,20,5,40,15]
large=list[0]
second=list[0]
for i in list:
    if i > large:
        second=large
        large=i
    elif i > second and i!=large:
        second=i
print("Second largest number is:",second)



#44.check the given number is perfect number or not
num=6
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("Perfect number")
else:
    print("not a Perfect number")


#45.check the given number is spy number or not
num=123
sum=0
product=1
for i in str(num):
    sum=sum+int(i)
    product=product*int(i)
if sum==product:
    print("Spy number")
else:
    print("not a Spy number")


#46. print the Fibonacci series up to 10 terms
a,b=0,1
n=10
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b


#47. check the given number is a neon number or not
num=9
sq=num*num
sum=0
for i in str(num):
    sum=sum+int(i)  
if sum==num:
    print("Neon number")
else:
    print("not a Neon number")


#48. print the count frequency of each character in the string
txt="Pyspiders"
for ch in txt:
    count=0
    for i in txt:
        if ch==i:
            count+=1
    print(ch,count)
#another way
txt="Pyspiders"
repeat=""
for ch in txt:
    if ch not in repeat:
        count=0
        for i in txt:
            if ch==i:
                count+=1
        print(ch,count)
        repeat=repeat+ch


#49.count of prime numbers from 1 to 31
countp=0
for n in range(1,32):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        countp+=1
        print(n,end=" ")
print("No of Prime Numbers:",countp)