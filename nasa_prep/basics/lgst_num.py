list1 = [3, 65, 12, 42, 10, 72, 81, 99, 80, 100, 70]

def find_largest(list):
    largest = list[0]
    for number in list:
        if number > largest:
            largest = number
    return largest

print(find_largest(list1))

# First TRY
# def find_largest(li):
#     lgst = [li[0]]
#     count = 0
#     for num in li:
#         if num > lgst[count]:
#             lgst.pop()
#             lgst.append(num)
#         else:
#             continue
#     return lgst


# largest = find_largest(list1)
# print(largest)
