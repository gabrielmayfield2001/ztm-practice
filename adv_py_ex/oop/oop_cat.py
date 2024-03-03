#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('ruky', 18)
cat2 = Cat('lalo', 4)
cat3 = Cat('wawa', 7)

# 2 Create a function that finds the oldest cat

def oldest_cat(*ages):
    return(max(ages))


# 3 Print out: "The oldest cat is x years old.

print(f'The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old')