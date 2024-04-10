username = str(input('Inform an user name: '))
password = str(input('Type your password: '))
passwordlength = len(password)

password = password.replace(password, '*'*passwordlength)


print(f'Hey {username} password {password} is {passwordlength} letters long')
