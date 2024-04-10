print(type('hi there'))
username = 'supercoder'
password = 'supersecret'
long_string = '''
WOW
O O
---
'''
print(long_string)

first_name = 'Renan'
last_name = 'Maciel'
full_name = first_name + ' ' + last_name
print(full_name)

# String concatenation 
# Adding strings together

print('hello' + 'Renan')

# Escape sequence 
weather = "\t It\'s \"Kind of\" sunny \n hope you have a good day!"
print(weather)

# Strings: An ordered sequence of characters
# Formatted strings
name = 'Renan'
age = 55
print('hi' + name + '.You are' + str(age) + ' years old')

# Using formatted strings
print(f'hi {name}.You are {age} years old')

# Strings: An ordered sequence of characters
# This is how the sequence below is stored
# 'me me me'
#  01234567 <- think about it as a book shelve
selfish = 'me me me'
print(selfish)

# String slicing (because we slice)
# [start:stop:stepover]
print(selfish[0:2])
print(selfish[1:3])

# Reversed order
print(selfish[-1])
print(selfish[-2])

# Immutability 
# Strings in python are immutable 
# I can reassign a variable that is a string
# But I cannot change the value of a string once it is created

# This is gonna work:
selfish = '01234567' 
selfish = selfish + '8' # = 012345678

# Reassignment:
selfish = '8'

# This isn't:
selfish[0]=8
