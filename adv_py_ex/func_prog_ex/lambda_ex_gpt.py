# map with lambda

li1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list(map(lambda item: item ** 2, li1)))


# filter with lambda 

print(list(filter(lambda num: num % 2 == 0, li1)))

