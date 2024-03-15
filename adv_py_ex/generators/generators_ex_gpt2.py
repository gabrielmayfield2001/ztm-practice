def filter_evens(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num


for num in filter_evens([10, 11, 13, 14, 15]):
    print(num)
