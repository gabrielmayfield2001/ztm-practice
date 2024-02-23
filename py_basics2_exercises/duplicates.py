# Check for duplicates

# Only use conditionals and loops

list = [
    'a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'a', 'c', 'd', 'e', 'f', 'd', 'f',
    'd', 'e', 't', 't', 'v', 'v'
]

seen = []
duplicates = []

for value in list:
  if value in seen:  # Checking if value has been seen
    if value not in duplicates:
      duplicates.append(value)  #Add to dups if not seen
  else:  # If value has not been seen, append to seen
    seen.append(value)

print(duplicates)

# second version

# for value in list:
#   if list.count(value) > 1:
#     if value not in duplicates:
#       duplicates.append(value)

# print(duplicates)
