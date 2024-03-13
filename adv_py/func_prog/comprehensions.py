# list set dictionary comprehensions


# without comprehension
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)


# with comprehension

my_list2 = [char for char in 'hello']
print(my_list2)

mylist3 = [num for num in range(0, 100)]
print(mylist3)

mylist4 = [num*2 for num in range(0, 100)]
print(mylist4)

mylist5 = [num*2 for num in range(0, 100) if num % 2 == 0]
print(mylist5)


# sets

myset = {char for char in 'hello'}
print(myset)


# Dictionaries
simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items() if value %
           2 == 0}
print(my_dict)


my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)
