import sys

import random 

input_1 = int(sys.argv[1])
input_2 = int(sys.argv[2])

random_int = random.randint(input_1, input_2)

while True:
    user_input = int(input("Enter the number you wish to guess between the range of input: "))
    if user_input == random_int: 
        print('You guessed right! Great  job')
        break
    else:
        print('incorrect, try again: ')
    

print('program finished!')