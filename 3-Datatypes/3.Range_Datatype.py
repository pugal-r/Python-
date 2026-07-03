
#Range datatypes
n=range(100)
print(n)        #range(0, 100)

n=range(11)
print(len(n))   #11

n=range(11)
print(list(n))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n=range(5,11)
print(list(n))  #[5, 6, 7, 8, 9, 10]

n=range(4,16,2)
print(list(n))  #[4, 6, 8, 10, 12, 14]

n=range(3,21,3)
print(list(n))  #[3, 6, 9, 12, 15, 18]


n=range(11,0)
print(list(n))  #[]


n=range(11,0,-1)
print(list(n))  #[11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


n=range(11,-1,-2)
print(list(n))  #[11, 9, 7, 5, 3, 1]


n=range(21,-1,-4)
print(list(n))  #[21, 17, 13, 9, 5, 1]


n=range(-5,0)
print(list(n))  #[-5, -4, -3, -2, -1]


n=range(-11,-1,2)
print(list(n))  #[-11, -9, -7, -5, -3]


n=range(0)
print(list(n))  #[]


n=range(5,5)
print(list(n))  #[]


#indexing for range datatype
n=range(100,210,10)
print(list(n))      #[100, 110, 120, 130, 140, 150, 160, 170, 180, 190,200]


n=range(100,200,10)
print(n[0])         #100
print(n[1])         #110
print(n[3])         #130
print(n[-1])        #190       
print(n[-4])        #160  
print(n[-3])        #170
print(n[2])         #120



#slicing for range datatypes


n=range(100,210,10)
s=list(n)
print(s)            #[100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

n=range(100,210,10)
s=list(n)
print(s[1:7:1])     #[110, 120, 130, 140, 150, 160]
print(s[2::2])      #[120, 140, 160, 180, 200]
print(s[:5:2])      #[100, 120, 140]
print(s[1:4:3])     #[110]
print(s[-1:-6:1])   #[]
print(s[-4::2])     #[170, 190]
print(s[-6:5:1])    #[]
print(s[-4:7:2])    #[]
print(s[-7::1])     #[140, 150, 160, 170, 180, 190, 200]
print(s[-8:-1:3])   #[130, 160, 190]
print(s[-2:-8:-2])  #[190, 170, 150]







