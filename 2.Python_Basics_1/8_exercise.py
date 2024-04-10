import datetime 

name = 'Renan Maciel'
age = '30'
relationship_status = 'married'
relationship_status = 'It\'s not complicated'

# Let's create a program that 'guess your age'
birth_year = input('What year were you born ?: ')

today = datetime.date.today()
current_year  = today.year

age = int(current_year) - int(birth_year)

print('Your age is:', age)