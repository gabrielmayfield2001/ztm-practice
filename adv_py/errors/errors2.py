# Error handling


while True:
    try:
        age = int(input('What is your age? '))
        print(age)
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than zero ')
    else:
        print('thank you ')
        break
