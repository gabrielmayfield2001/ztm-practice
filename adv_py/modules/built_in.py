import random

print(random.randint(0, 10))

print(random.choice([1,2,3,4,5]))

my_list = [6,7,8,9,10]
random.shuffle(my_list)
print(my_list)
