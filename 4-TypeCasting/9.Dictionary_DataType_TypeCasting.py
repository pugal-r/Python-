#Dictionary datatype TypeCasting

#Possible to convert

d1={"name":"Sam","age":23}

print(bool(d1))     #True

print(str(d1))      #{'name': 'Sam', 'age': 23}

print(list(d1))     #['name', 'age']

print(tuple(d1))    #('name', 'age')

print(set(d1))      #{'age', 'name'}


#cannot converted

print(int(d1))          #TypeError:

print(float(d1))        #TypeError:

print(complex(d1))      #TypeError: