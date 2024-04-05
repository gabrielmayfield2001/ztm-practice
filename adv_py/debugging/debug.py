# debugging

# linting - shows us errors before we run code
# num + 4

# ide/editor

# read errors
# 4 + ';lkjadf'


import pdb
# pdb
def add(num1, num2):
    pdb.set_trace()
    t = 4*5
    return num1 + num2

add(4, 'a;lkj')