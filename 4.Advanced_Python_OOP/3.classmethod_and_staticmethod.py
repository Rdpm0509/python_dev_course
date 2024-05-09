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

    def run(self):
        print('run')
        return 'done'

    # We use a decorator to create a class method
    # when using classmethod, we must use cls (instead of self)
    # cls stands for 'class'
    # we can use it even without instanciating the class
    # a class method can also be used to intanciate a class
    # for instance, one can instance by using 'cls('something', 'here')
    # in this example cls instance the class and it has two attributes, 'something' and 'here'. 
    # cls('something', 'here') will work as __init__(self, atr1, atr2)
    # in our example, we can instanciate and create a player by doing the following 
    # @classmethod
    # def adding_things(cls, num1, num2):
    # return cls('Teddy', num1+num2)
    # outside the class we call: 'player3 = PlayerCharacter.adding_things(2,3)
    # it will create a player with name 'Teddy' and age 'num1+num2'
    # PS: note that cls instanciation follows the constructor pattern, i.e., name, age. 
    # therefore you can print 'print(player3.name)' and it will show you 'Teddy'
    # or 'print(player3.age)' and it will print out 'num1+num2'
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    # we do not have access in our parameters to cls
    # @staticmethod is mostly used when we dont care about our class state
    # for instance, we dont care about the attributes (in this case age and name). 
    # we use @classmethod when we care about the attributes and maybe we want 
    # to change them (like if i want to update name or age attribute values for example)
    @staticmethod
    def adding_things2(num1, num2):
        return num1+num2


# Intanciate , i.e., create an instance , i.e., an object
# Instanciate: is the same as saying calling a class to create an object
player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 22)

print(player1.name)  # printning an attribute of the class
print(player1.age)   # printing an attribute of the class
print(player1.run()) # printing a method of thhe class
print(player1.shout())

# Lets use the class method 'adding_things' without instanciating it. 
# i.e., without creating an object before calling the function we want. 
# we are allowed to do so because of the decorator @classmethod
print(PlayerCharacter.adding_things(1,10))