

while True:
    try:
        user_input = input('Please enter a number (or quit to exit): ')
        if user_input.lower() == 'quit':
            print('exiting program')
            break
        num = int(user_input)
        print(f'{num*num} is the square of the number gien')
    except ValueError:
        print('Please enter a valid number.')
    finally: 
        print('Finished with this attempt!')