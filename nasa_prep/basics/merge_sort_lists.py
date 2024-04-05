li1 = [3,6,1,9]
li2 = [2,8,4,7]


def merge_and_sort_lists(list1, list2):
    return sorted(list1 + list2)

sorted_combination = merge_and_sort_lists(li1,li2)
print(sorted_combination)

