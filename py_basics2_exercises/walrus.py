def stringInput():
  strings = [] 
  while string := input('give me a string or type stop to stop inputting: ') != 'stop':
    strings.append(string)
  print(f'you entered: {strings}')

stringInput()

