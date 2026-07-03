##Float Datatype type Casting 

#Possible to Convert 

a=10+5j

print(bool(a))      #True

print(str(a))       #(10+5j)

#cannot Converted

b=20+4j

print(int(b))       #TypeError:

print(float(b))     #TypeError:

print(list(b))      #TypeError: 

print(tuple(b))     #TypeError: 

print(set(b))       #TypeError: 

print(dict(b))      #TypeError: 