
#collection datatypes 

s="Hii Buddy"
print(s)        #Hii Buddy
print(type(s))  #<class 'str'>


s1='How Are you?'
print(type(s1)) #<class 'str'>


s2='''I am good'''
print(type(s2)) #<class 'str'>


s3="""What about you ?"""
print(type(s3)) #<class 'str'>


#String Indexing
s="Python"
print(s[0])     #P
print(s[1])     #y
print(s[2])     #t
print(s[3])     #h
print(s[4])     #o
print(s[5])     #n
print(s[6])     #IndexError: string index out of range


s="Welcome to python"
print(s[1])
print(s[9])
print(s[0])
print(s[3])
print(s[4])
print(s[7])
print(s[8])
print(s[2])
print(s[14])
print(s[10])



# String Slicing
'''
p   y   t   h   o   n   p   r   o   g   r   a   m
0   1   2   3   4   5   6   7   8   9   10  11  12

'''
str="PythonProgram"
print(str[::])      #PythonProgram
print(str[2::])     #thonProgram
print(str[3:8:1])   #honPr
print(str[::2])     #PtoPorm
print(str[::3])     #PhPgm
print(str[0:9:2])   #PtoPo
print(str[12::])    #m

a="welcome to python class"

print(a[0:7:1])     #welcome
print(a[3:10:1])    #come to
print(a[11:17:1])   #python
print(a[0:24:2])    #wloet yhncas
print(a[0:24:3])    #wceoyocs
print(a[8:10:1])    #to
print(a[18:23:1])   #class
print(a[2:15:2])    #loet yh
print(a[5:20:3])    #mtph
print(a[0:24:1])    #welcome to python class
print(a[0:34:1])    #welcome to python class

# Reverse the string slicing

ss="python program"
print(ss[::-1])     #margorp nohtyp
print(ss[-2::-2])   #agr otp
print(ss[-1::-2])   #mropnhy

# Another example reverse the string

sss="Happy New Year 2026"

print(sss[-1::-1])          #6202 raeY weN yppaH
print(sss[-6::-1])          #raeY weN yppaH
print(sss[-5:-15:-1])       # raeY weN
print(sss[-4:-16:-2])       #2re e
print(sss[:-27:-1])         #6202 raeY weN yppaH
print(sss[::-1])            #6202 raeY weN yppaH
print(sss[::-4])            #6 YNp

print(sss[-9:-6:1])