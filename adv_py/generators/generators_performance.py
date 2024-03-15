from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, *kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

def gen_func(num):
    for i in range(num):
        yield i

for item in gen_func(100):
    print(item)



@performance
def long_time():
    print('1')
    for i in range(1000000):  # it finishes after.
        i*5


long_time()
print()


@performance
def long_time2():
    print('2')
    for i in list(range(1000000)):  # it took longer.
        i*5


long_time2()
print()
