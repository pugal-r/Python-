#list collection datatypes

#example-1
list=[10,20,30,40,50]
print(list)

print(type(list))

#example-2
list=[10,"smith",96,50,100.5,"analyst"]
print(list)

print(type(list))

##example-3 --> nested list
ns=[[10,20,30,"sam"],[40,"ram",60]]
print(ns)

print(type(ns))


#Indexing in list

list=[10,20,30,"smith",40,"sam",50,"kavi",70]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
print(list[6])
print(list[7])
print(list[8])

#negative Indexing
print(list[-1])
print(list[-3])
print(list[-5])
print(list[-2])
print(list[-8])
print(list[-6])


#slicing on list collection
list=[10,20,30,"smith",40,"sam",50,"kavi",70]

print(list[1:3])
print(list[0:4])
print(list[:2])
print(list[1:4])
print(list[0:5:3])
print(list[::5])
print(list[3:3])
print(list[4:5])
print(list[1:1])
print(list[5:2])