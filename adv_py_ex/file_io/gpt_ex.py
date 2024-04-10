list1 = ['1', '2', '3', 'horsie']


def convert_to_integers(list_of_str):
    ints = []
    for str in list_of_str:
        try:
            new_int = int(str)
            ints.append(new_int)
        except ValueError:
            raise ValueError('All items in list must be ints')
    return ints

try:
    first_try = convert_to_integers(list1)
    print(first_try)
except ValueError as e:
    print(e)