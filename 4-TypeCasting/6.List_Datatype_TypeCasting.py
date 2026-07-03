#List datatype TypeCasting

#Possible to convert

l=[1,2,3,"a","b"]

print(bool(l))      #True

print(str(l))       #[1, 2, 3, 'a', 'b']

print(tuple(l))     #(1, 2, 3, 'a', 'b')

print(set(l))       #{1, 2, 3, 'a', 'b'}


#cannot converted

print(int(l))       #TypeError:

print(float(l))     #TypeError:

print(complex(l))   #TypeError:      

print(dict(l))      #TypeError:

