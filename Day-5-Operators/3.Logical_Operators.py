# Whenever we having multiple condition we have to use logical operaors 
# it consists of AND - OR - NOT

a=10
b=20
c=60
print(a==b and b==c)    #False

print(a!=b and b!=c)    #True

print(a==b or a<=b )    #True

print(a!=c or c>=a)     #True


a=90
b=80
c=50
d=40

print(a>b and b>c and c<a and d<b)      #True

print(a!=b and c!=d or b>c or a>c)      #True

print(a==c or b==c and c==d and d==b)   #False

print(a<d)      #False

print(a<d and b>d or c<a or d<a)        #True

print(b>=a or c>=d and c<=a or a>c)     #True 