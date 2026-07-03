
t1=(10,20,30,40)
print(t1)       #(10, 20, 30, 40)
print(type(t1)) #<class 'tuple'>


t2=(100)
print(type(t2)) #<class 'int'>

t3=(50,)
print(type(t3)) #<class 'tuple'>

t4=(10,20,90,"sam",(40,2,4),8,"kamal")
print(t4)           #(10, 20, 90, 'sam', (40, 2, 4), 8, 'kamal')
print(type(t4))     #<class 'tuple'>



#indexing On tuple
t5=(1,3,5,7,"sam",30,40,(2,"sara"),60)
print(t5[0])    #1
print(t5[6])    #40
print(t5[2])    #5
print(t5[5])    #30
print(t5[1])    #3
print(t5[4])    #sam
print(t5[3])    #7
print(t5[7])    #(2,'sara')
print(t5[7][1]) #sara


#slicing on tuple
t6=(90,30,50,30,70,60,40,10,80,20)

print(t6[::])           #(90, 30, 50, 30, 70, 60, 40, 10, 80, 20)
print(t6[0:5:1])        #(90, 30, 50, 30, 70)
print(t6[2:6:1])        #(50, 30, 70, 60)
print(t6[7:1:1])        #()
print(t6[10:1:1])       #()
print(t6[10:1:1])       #()
print(t6[0::2])         #(90, 50, 70, 40, 80)
print(t6[1::2])         #(30, 30, 60, 10, 20)
print(t6[::-2])         #(20, 10, 60, 30, 30)
print(t6[-2::-2])       #(80, 40, 70, 50, 90)
print(t6[-1::-2])       #(20, 10, 60, 30, 30)