def filter_and_square(list):
    over_10 = []
    for num in list:
        if num >= 10:
            over_10.append(num)
        else:
            pass
    squares = []
    for num in over_10:
        square = num*num
        squares.append(square)
    return squares


squared_list = filter_and_square([3, 5, 7, 10, 15, 20])
print(squared_list)


li1 = [3, 5, 7, 10, 15, 20]


squared_list_comp = [num*num for num in li1 if num >= 10]
print(squared_list_comp)