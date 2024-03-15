# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single
# line.Suppose the following input is supplied to the program: 8 
# Then, the output should be:40320

# While loop 
n = int(input('Enter a number you want to factorial: '))

i = 1
fact = 1
while i <= n:
    fact = fact * i
    i+=1
print(fact)


# For loop 

n = int(input('Enter num to factorial: '))

fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)


fact_num = int(input('Enter number to fact'))

def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
print(shortFact(fact_num))



