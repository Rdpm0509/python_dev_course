is_old = False 
is_licenced = False 

if is_old: 
    print("you're old enough to drive!")
elif is_licenced: 
    print("you can drive now!")
else: 
    print("you're not of age!")

print('okay okay')

# Maybe a more appropriate way of write the code above is 
# This is because what comes after 'if' is an expression and not a variable. 
# Therefore, one can simply rewrite the condition to be like below. 

print('')

is_old = False 
is_licenced = False 
if is_old and is_licenced: 
    print("you're old enough to drive!")
    print("you can drive now!")
else: 
    print("you're not of age!")

print('okay okay')
