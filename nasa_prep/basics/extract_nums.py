def extract_numbers(string):
    nums = []
    parts = string.split()
    for item in parts:
        try:
            num = int(item)
            nums.append(num)
        except ValueError:
            pass

    sorted_nums = sorted(nums)
    return sorted_nums



print(extract_numbers('3 apples and 25 bananas 1 and 47 oranges'))


