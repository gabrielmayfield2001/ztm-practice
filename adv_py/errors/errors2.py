# Error handling


while True:
    try:
        age = int(input('What is your age? '))
        10/age
        raise ValueError('hey cut it out')
    except ZeroDivisionError:
        print('please enter age higher than zero ')
        break
    else:
        print('thank you ')
    finally:
        print('finally done')
    print('can you hear me?')