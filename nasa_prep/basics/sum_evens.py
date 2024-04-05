def sum_of_evens(list):
    evens = []
    for num in list:
        if num % 2 == 0:
            evens.append(num)
        else:
            pass
    sum = 0
    for num in evens:
        sum += num
    return sum


print(sum_of_evens([1, 2, 3, 4, 5, 6]))
