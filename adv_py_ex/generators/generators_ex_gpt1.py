def even_numbers(max):
    count = 2
    while count <= max:
        yield count 
        count += 2

for number in even_numbers(10):
    print(number)

