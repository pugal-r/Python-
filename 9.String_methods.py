#-----String Methods --------

#1. dir():
'''It is used to print all the methods and files present in a perticular datatype (or) folder'''
#   Syntax:--> dir(datatype/folder)


#2.upper()
'''It is used to convert all characters present in a string to uppercase '''
#Syntax:--> string.upper()


#3.lower()
'''It is used to convert all characters present in a string to lowercase '''
#Syntax:--> string.lower()


#4.capitalize()
'''It is used to convert the first character of a string to uppercase and all other characters to lowercase '''
#Syntax:--> string.capitalize()


#5.title()
'''It is used to convert the first character of each word in a string to uppercase and all other characters to lowercase '''
#Syntax:--> string.title()


#6.swapcase()
'''It is used to convert uppercase characters to lowercase and vice versa '''
#Syntax:--> string.swapcase()


#7.casefold()
'''It is used to convert all characters in a string to lowercase 

    It will convert the special symbols of different languages like 'german ß and latin characters' to English.
'''
#Syntax:--> string.casefold()


#8.strip()
'''It is used to remove leading and trailing whitespace from a string '''
#Syntax:--> string.strip()


#9.lstrip()
'''It is used to remove leading whitespace from a string '''
#Syntax:--> string.lstrip()


#10.rstrip()
'''It is used to remove trailing whitespace from a string '''
#Syntax:--> string.rstrip()


#11.index()
'''It is used to find the index of a substring in a string. If the substring is not found, it raises a ValueError.'''
#Syntax:--> string.index(substring)


#12.rindex()
'''It is used to find the last index of a substring in a string. If the substring is not found, it raises a ValueError.'''
#Syntax:--> string.rindex(substring)


#13.find()
'''It is used to find the index of a substring in a string. If the substring is not found, it returns -1.'''
#Syntax:--> string.find(substring)


#14.rfind()
'''It is used to find the last index of a substring in a string. If the substring is not found, it returns -1.'''
#Syntax:--> string.rfind(substring)


#15.replace()
'''It is used to replace a substring in a string with another substring.'''
#Syntax:--> string.replace(old_substring, new_substring)


#16.split()
'''It is used to split a string into a list of substrings based on a specified delimiter. If no delimiter is specified, it splits on whitespace by default.'''
#Syntax:--> string.split(delimiter)


#17.rsplit()
'''It is used to split a string into a list of substrings based on a specified delimiter, starting from the right. If no delimiter is specified, it splits on whitespace by default.'''
#Syntax:--> string.rsplit(delimiter)


#18.splitlines()
'''It is used to split a string into a list of lines, breaking at line boundaries.'''
#Syntax:--> string.splitlines()


#19.count()
'''It is used to count the number of occurrences of a substring in a string.'''
#Syntax:--> string.count(substring)


#20.startswith()
'''It is used to check if a string starts with a specified substring. It returns True if the string starts with the substring, otherwise it returns False.'''
#Syntax:--> string.startswith(substring)


#21.endswith()
'''It is used to check if a string ends with a specified substring. It returns True if the string ends with the substring, otherwise it returns False.'''
#Syntax:--> string.endswith(substring)


#22.join()
'''It is used to join a list of strings into a single string, with a specified separator.'''
#Syntax:--> separator.join(list_of_strings)


#23.center()
'''It is used to center a string within a specified width, padding it with a specified character (default is space) on both sides.'''
#Syntax:--> string.center(width, fillchar)


#24.isalpha()
'''It is used to check if all characters in a string are alphabetic. It returns True if all characters are alphabetic, otherwise it returns False.'''
#Syntax:--> string.isalpha()


#25.isdigit()
'''It is used to check if all characters in a string are digits. It returns True if all characters are digits, otherwise it returns False.'''
#Syntax:--> string.isdigit()


#26.isalnum()
'''It is used to check if all characters in a string are alphanumeric (letters and numbers). It returns True if all characters are alphanumeric, otherwise it returns False.'''
#Syntax:--> string.isalnum()


#27.islower()
'''It is used to check if all characters in a string are lowercase. It returns True if all characters are lowercase, otherwise it returns False.'''
#Syntax:--> string.islower()


#28.isupper()
'''It is used to check if all characters in a string are uppercase. It returns True if all characters are uppercase, otherwise it returns False.'''
#Syntax:--> string.isupper()


#29.isspace()
'''It is used to check if all characters in a string are whitespace. It returns True if all characters are whitespace, otherwise it returns False.'''
#Syntax:--> string.isspace()


#30.isnumeric()
'''It is used to check if all characters in a string are numeric. It returns True if all characters are numeric, otherwise it returns False.'''
#Syntax:--> string.isnumeric()


#---Example programs for string methods---

#1.print even index characters of a string
s="python programming"
print(s[::2])  # Output: pto rgamn


#2.print every alternate character of a string in reverse order
s="python programming"
print(s[::-2])  # Output: gmrpnhy


#3.print the string in reverse order
s="python programming"
print(s[::-1])  # Output: gnimmargorp nohtyp


#4.print extension of a filename
filename="example.txt"
b=filename.split(".")
print(b[-1])  # Output: txt


#5.print the first and last character of a string
s="python programming"
print(s[0], s[-1])  # Output: p g


#6.printing only protocol of a url
url="https://www.example.com"
b=url.split(":")
print(b[0])  # Output: https


#7.print the position of character which present in a character 2nd time of position
s="python programming"
b=s.index("o")
print(b)  # Output: 4
b1=s.index("o",b+1)
print(b1)  # Output: 14
b2=s.index("o",b1+1)
print(b2)  # Output: 14 (if there is no third occurrence, it will raise a ValueError)

