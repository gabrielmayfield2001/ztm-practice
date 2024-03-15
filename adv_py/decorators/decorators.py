from time import time


def helloooo(func):
    func()


def greet():
    print('still here')


a = helloooo(greet)

print(a)

# Higher order function HOC examples


def hoc(func):
    func()


def hoc2():
    def func():
        return 5
    return func

# Decorators 2


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')
    return wrap_func


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


hello('hi')


# Decorator application


def logging(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} ms')
        return result
    return wrapper


@logging
def long_time():
    for i in range(0, 1000000000):
        i * 5


long_time()
