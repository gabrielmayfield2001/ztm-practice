def reverse_list(list):
    reversed = []
    for i in range(len(list) - 1, -1, -1):  # start (inclusive), stop(exclusive), step
        reversed.append(list[i])
    return reversed


original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(reversed_list)

