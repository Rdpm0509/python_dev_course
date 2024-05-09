#OOP 

# ideally in singular, not in plural.
class PlayerCharacter: 
    
    # class object attribute (or attribute of the class)
    # It is static and belongs to the class. It is global
    # It is different from the attribute informed in the constructor.
    # All object created will have access to the same variable and it wont change. 
    membership = True

    # Special method: __ means dunder method. 
    # __init__ is a constructor method. 
    # __init__ is automaticaly called when the class is instaciated.  
    # the word self refers to the PlayerCharacter. 
    # In this example we call assign PlayerCharacter to player1
    # player1 then is the 'self' (because player1 = PlayerCharacter)
    # When the class is instanciated, it calls the constructor first
    # It checks who is self, and what self needs as a parameter of the function so this function can run
    def __init__(self, name='anonymous', age=0):
        
        # Both usage may work
        # if (PlayerCharacter.membership): 
        # if (self.membership):
        if (age > 18):

        # Attribute is something dynamic. 
        # This means when a class is instanciated, the attribute will be unique 
        # To that instace/object. In our example, attributes from player1 belongs only to player1
        # It doesnt mix up with player2. player2 has its own attribute
        # this is different from the 'class object attribute'
            self.name = name # attribute name
            self.age = age # attribute age

    def shout(self):
        
        # It doesnt work: Because it is not possible to identify what name is
        # print(f'my name is {name}')
        # It doesnt work: Because name is an attribute of the constructure. It doesnt belongs to the class object attribute
        # it is 'private' to the constructor. 
        # print(f'my name is {PlayerCharacter.name}')
        print(f'my name is {self.name}')

    # a method 
    def run(self):
        print('run')
        # if return isnt inform, a function returns 'None'
        return 'done'

# Intanciate , i.e., create an instance , i.e., an object
# Instanciate: is the same as saying calling a class to create an object
player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 22)

print(player1.name)  # printning an attribute of the class
print(player1.age)   # printing an attribute of the class
print(player1.run()) # printing a method of thhe class
print(player1.shout())

# print(player2.name)
# print(player2.age)
# print(player2.run())

# ps: you can always type help(player1), so it shows what's inside the class... 
# another example is help(list)