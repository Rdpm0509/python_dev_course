# Method: Similar to functions but they are owned by something
# Actions that are bond to something, e.g. Python Strings Methods. 
# It usually has a dot in front of it. 

quote = 'to be or not to be'
quote.upper()
quote.lower()
quote.capitalize()

# Is there a word 'be' on the string 'quote' ?
print(quote.find('be'))

# Remember that strings are immutable. It is not going to change it. 
# So even thought the following line is going to print you 'me' 
# instead of 'be', it isng going to substitute inside the string 'quote'. 
# so if you call 'print(quote)', you're going to still see the same thing. 
# only if you re-assign the variable it is going to change. Otherwise it wont
print(quote.replace('be', 'me'))


