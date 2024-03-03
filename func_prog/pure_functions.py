
from functools import reduce

# map, filter, zip, reduce


# function without map

# def multiply_by2(li1):
#     new_list = []
#     for item in li1:
#         new_list.append(item*2)
#     return new_list

my_list = [1, 2, 3]
your_list = [10,20,30]

# function with map
def multiple_by2(item):
    return item*2


# function with filter
def only_odd(item):
    return item % 2 != 0

# reduce function 
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(list(map(multiple_by2, my_list)))
print(list(filter(only_odd, my_list)))
print(list(zip(my_list, your_list))) # zip function takes two pairs and zips each item together in a tupple
print(reduce(accumulator, my_list, 1)) # acc function call 
