#Dictionary collection datatype

emp={
    "empno":1234,
    "ename":"smith",
    "salary":98000
}
print(emp)      #{'empno': 1234, 'ename': 'smith', 'salary': 98000}
print(type(emp))    #<class 'dict'>


print(emp["ename"])     #smith
print(emp["salary"])    #98000
print(emp["empno"])     #1234


#print for keys and values separate using keywords

print(emp.keys())  
 #dict_keys(['empno', 'ename', 'salary'])


print(emp.values())
#dict_values([1234, 'smith', 98000])


print(emp.items())
#dict_items([('empno', 1234), ('ename', 'smith'), ('salary', 98000)])
