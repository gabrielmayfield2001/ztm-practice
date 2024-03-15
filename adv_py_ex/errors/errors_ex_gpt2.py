while True:
    try:
        user_numer = input('Please enter a numerator (or quit to stop): ')
        if user_numer.lower() == 'quit':
            break
        user_denom = input('Please enter a denominator: ')
        quotient = float(user_numer)/float(user_denom)
        print(f'The quotient is {quotient}')
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a denominator higher than 0')
    finally:
        print('Attempt completed')