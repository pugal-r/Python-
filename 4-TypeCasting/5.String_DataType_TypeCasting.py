#String datatype TypeCasting

#Possible to convert

s1="Python"

print(bool(s1))      #True

print(list(s1))      # ['P', 'y', 't', 'h', 'o', 'n']

print(tuple(s1))     # ('P', 'y', 't', 'h', 'o', 'n')

print(set(s1))       #{'t', 'P', 'h', 'o', 'y', 'n'}



#cannot converted

s2="Django"

print(int(s2))      #ValueError;

print(float(s2))    #ValueError;

print(complex(s2))  #ValueError;

print(dict(s1))     #ValueError;