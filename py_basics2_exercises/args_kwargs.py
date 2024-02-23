def multiply_nums(*args):
  product = 1
  for number in args:
    product *= number
  return product

print(multiply_nums(1,2,3))
print()



def printInfo(**kwargs):
  for key, value in kwargs.items():
    print(f'{key}: {value}')

printInfo(name = 'gabe', age = '23', size = 'large')
print()




def createProfile(**kwargs):
  for attribute, value in kwargs.items():
    print(f'{attribute}: {value}')

createProfile(user = 'gabe', is_active = 'yes', blonde = 'yes')
print()


def sendInvitation(event_name, *guest_names, **details):
  print(event_name.upper())
  print('Guests Attending: ', end='')
  for name in guest_names:
    print(name, end = ', ')
  print()
  print('Details:')
  for Detail, Value in details.items():
    print(f'{Detail}: {Value}')


sendInvitation("Christmas Party", 'gabe', 'gabrielle', 'mom', 'dad', house = 'Mayfield House', address = '3691 County Road 326', time = '5:00pm')
sendInvitation("Party 2", "Gabriel", 'mateo', 'ezra', 'gabrielle', 'james', 'kathy', time = '5:00 pm')
