from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def cap_list(item):
    return item.capitalize()


print(list(map(cap_list, my_pets)))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over_50(score):
    return score > 50


print(list(filter(over_50, scores)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(sorted(list(zip(my_numbers, my_strings))))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def combine(acc, item):
    return acc + item


print(reduce(combine, scores + my_numbers))
