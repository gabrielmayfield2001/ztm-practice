# With a given integral number n, write a program to generate a dictionary 
# that contains (i, i x i) such that is an integral number between 1 and n 
# (both included). and then the program should print the dictionary.Suppose 
# the following input is supplied to the program: 8


# for loop 

dict_input = int(input('Enter a num: '))

dict = {}

for i in range(1, dict_input+1):
    dict[i] = i * i
    i +=1
print(dict)


# dict comprehension 

n = int(input('enter num'))
dict = {i: i*i for i in range(1, n+1)}
print(dict)


