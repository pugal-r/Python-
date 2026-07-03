#Tuple datatype TypeCasting

#Possible to convert

t=(0,1,6,9,87,56,70)

print(bool(t))      #True

print(str(t))       #(0, 1, 6, 9, 87, 56, 70)

print(list(t))      #[0, 1, 6, 9, 87, 56, 70]

print(set(t))       #{0, 1, 6, 70, 9, 87, 56}


#cannot converted

print(int(t))       #TypeError: 

print(float(t))     #TypeError: 

print(complex(t))   #TypeError: 

print(dict(t))      #TypeError: 
