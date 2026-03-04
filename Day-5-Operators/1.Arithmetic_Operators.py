#Arithmetic Operators 

#1.ADDITION

print(100+500)          #600

print("siva"+"ram")     #sivaram

print(10+True)          #11

# print(200+"sam")        #TypeError:


#examples
a=10
b=20
print(a+b)              #30
print("----------------------------------")

s1="David"
s2="Billa"
print(s1+s2)            #DavidBilla
print("----------------------------------")

a=[5,9]
b=[6,8]
print(a+b)          #[5, 9, 6, 8]
print("----------------------------------")

a=(1,2)
b=(3,4)
print(a+b)          #(1, 2, 3, 4)
print("----------------------------------")

a=100
b=10+5j
print(a+b)          #(110+5j)
print("----------------------------------")

x=45
y=55.80
print(x+y)          #100.8
print("----------------------------------")



#2.SUBTRACTION


print(500-400)          #100

#   print("smith"-"king")       #TypeError


#Examples:
a=125
b=87
print(a-b)          #38
print("----------------------------------")

a=55.68
b=45
print(a-b)          #10.68
print("----------------------------------")

a=10+4j
b=5+2j
print(a-b)          #(5+2j)
print("----------------------------------")

a={10,20}
b={1,2}
print(a-b)          #{10, 20}
print(b-a)          #{1, 2}

print("----------------------------------")

a={5,10}
b={5,10}
print(a-b)          #set()
print("----------------------------------")

a={10,20,30}
b={10,30}
print(a-b)          #{20}
print("----------------------------------")



#3.MULTIPLICATION


#Examples:
print(3*2)          #6

print(3*"python")   #pythonpythonpython

print(2*[1,2])      #[1, 2, 1, 2]

print(3*(1,9))      #(1, 9, 1, 9, 1, 9)

print(2*10+2j)      #(20+2j)

#   print(2*{1,2})          #TypeError:

#   print(2*{"name":"sam"}) #TypeError:



#4.TRUE DIVISION

#EXAMPLES:
a=93
b=3
print(a/b)      #31.0




#5.FLOOR DIVISION

#Examples :
a=93
b=3
print(a//b)         #31

#To Remove last digit
a=123458
print(a//10)        #12345

#To remove Last 2 Digit 
a=7894561
print(a//100)       #78945

#To Remove Last 3 Digit 
a=45796125
print(a//1000)      #45796



#6.MODULUS:
#Examples:
a=987
b=3
print(a%b)      #0


#To Get Last element of the given numbers
a=8954571
print(a%10)     #1

#To Get Last 2 element of the given numbers
a=56479942
print(a%100)    #42

#To Get Last 3 element of the given numbers
a=13456987
print(a%1000)   #987




#7.EXPONENTIAL

#Examples:

print(2**3)     #8

print(5**4)     #625



