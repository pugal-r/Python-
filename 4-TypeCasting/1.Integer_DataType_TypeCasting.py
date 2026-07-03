#Integer Datatype type Casting 

# Possible to Convert 
a=100

print(float(a))     #100.0

print(complex(a))   #(100+0j)

print(bool(a))      #True

print(str(a))       #100


# cannot converted

b=200

print(list(b))      #TypeError: 'int' object is not iterable

print(tuple(b))     #TypeError: 'int' object is not iterable

print(set(b))        #TypeError: 'int' object is not iterable

print(dict(b))       #TypeError: 'int' object is not iterable