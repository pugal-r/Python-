#Boolean datatype TypeCasting

#Possible to convert

a=True

print(int(a))       #1

print(float(a))     #1.0

print(complex(a))   #(1+0j)

print(str(a))       #True

#cannot Converted

b=True

print(list(b))      #TypeError: 

print(tuple(b))     #TypeError: 

print(set(b))       #TypeError: 

print(dict(b))      #TypeError: 