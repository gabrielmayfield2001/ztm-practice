try:
    with open('happy.txt', 'r+') as my_file:
        my_file.write('This is being added')
except FileNotFoundError as err:
    print('file does not exist')
    raise err
