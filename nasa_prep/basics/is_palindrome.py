def is_palindrome(string):
    reversed = []
    for i in range(len(string) -1, -1, -1):
        reversed.append(string[i])
    list_string = list(string)
    if reversed == list_string:
        return True
    else:
        return False
    
is_it_reversed1 = is_palindrome('hello')
is_it_reversed2 = is_palindrome('racecar')

print(is_it_reversed1)
print(is_it_reversed2)
