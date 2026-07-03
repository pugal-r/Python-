
#set collection datatypes

s1={10,20,30,40,50}
print(s1)
print(type(s1))

s2={10,20,10,30,30,40,50,50,40}
print(s2)

s3={10,20,30,"smith",(1,2,3,4)}
print(s3)
print(type(s3))

#in set datatype we can't store list data's
s={10,20,[30,40,50],70}
print(s)    #TypeError: unhashable type: 'list'

#and we cannot using indexing
ss={10,20,30,40}
print(ss[0])  # TypeError