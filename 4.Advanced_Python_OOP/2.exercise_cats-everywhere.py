# Given the below class: 
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name 
        self.age = age




# 1. Instantiate the Cat object with 3 cats
cat1 = Cat('a', 8)
cat2 = Cat('b', 8)
cat3 = Cat('c', 4)

# 2. Create a function that finds the oldest cat
def oldest(a,b,c):
    if (a > b and b > c) or (a > b and b < c): 
        print(a)
    elif (a < b and b > c):
        print(b) 
    elif (a < b and b < c): 
        print(c) 
    else: 
        print('error, maybe two cats have the same age!') 
        
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {oldest(cat1.age,cat2.age,cat3.age)} years old.')


# A smarter/cleaner way of solving the problem above is as follows: 
def oldest_cat(*args): 
    return max(args)

print(f'Oldest Cat is {oldest(cat1.age,cat2.age,cat3.age)} years old.')
