try:
    with open('happy.txt', 'r+') as my_file:
        my_file.write('hello last ')
except FileNotFoundError as err:
    print('file does not exist')
