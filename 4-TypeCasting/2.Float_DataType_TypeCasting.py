#Float Datatype type Casting 

#Possible to Convert 
a=10.6

print(int(a))       #10

print(complex(a))   #(10.6+0j)

print(bool(a))      #true

print(str(a))       #10.6


#cannot Converted

b=54.32

print(list(b))      #TypeError: 'float' object is not iterable

print(tuple(b))     #TypeError: 'float' object is not iterable

print(set(b))       #TypeError: 'float' object is not iterable

print(dict(b))      #TypeError: 'float' object is not iterable