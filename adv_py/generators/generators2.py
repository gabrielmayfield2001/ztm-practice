def generator_func(num):
    for i in range(num):
        yield i*2



for item in generator_func(1000):
    print(item)
