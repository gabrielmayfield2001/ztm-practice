from functools import reduce


# map
def convert_to_farenheit(tempC):
    return tempC * (9/5) + 32


print(list(map(convert_to_farenheit, [0, 10, 20, 30, 40])))


# filter
def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


nums = [13, 14, 15, 29]

print(list(filter(is_prime, nums)))

# filter #2


def greater_than_10(num):
    if num > 10:
        return True
    else:
        False


nums2 = [10, 15, 4, 25, 100]

print(list(filter(greater_than_10, nums2)))


# zip
names = ['alice', 'bob', 'gabe', 'adam', 'gage']
ages = [24, 28, 18, 22, 25]

print(list(zip(names, ages)))


# reduce
def sum_numbers(acc, num):
    return acc + num


nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(reduce(sum_numbers, nums3, 0))
