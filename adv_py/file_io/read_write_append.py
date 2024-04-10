with open('test.txt', 'r+') as my_file:
    print(my_file.readlines())
    my_file.write('This is coming from read_write_buffer.py')
