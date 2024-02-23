def passValidation():
  global password 
  password = []
  while True: 
    string = input('Enter a password of 8+ characters and one number or \'stop\' to cancel: ')
    if string.lower() == 'stop':
      break
    if len(string) >= 8 and any(char.isdigit() for char in string): 
      password.append(string)
      break
    else:
      print('The password does not meet the criteria, try again')
  print('valid password entered: ', password)
  return password


def passInfo(password):
  pass_length = len(password[0])
  count = 0
  for string in password:
    for char in string:
      if char.isdigit():
        count += 1
  pass_nums = count
  print(f'The password you entered has {pass_length} characters and {pass_nums} numbers containted in it.')

passValidation()
passInfo(password)

