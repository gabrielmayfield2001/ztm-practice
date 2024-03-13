some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([val for val in some_list if some_list.count(val) > 1]))


print(duplicates)

