#Set datatype TypeCasting

#Possible to convert

ss={98,65,14,23,75}

print(bool(ss))     #True

print(str(ss))      #{65, 98, 23, 75, 14}

print(list(ss))     #[65, 98, 23, 75, 14]

print(tuple(ss))    #(65, 98, 23, 75, 14)




#cannot converted

print(int(ss))      #TypeError:

print(float(ss))    #TypeError:

print(complex(ss))  #TypeError:

print(dict(ss))     #TypeError: