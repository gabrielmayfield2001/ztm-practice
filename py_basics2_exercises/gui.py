#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# for row in picture:
  # for pixel in row:
    # if num == 0:
      # print ''
    # if num == 1:
      # print '*'
  # print()

fill = '*'
empty = ''
for row in picture:
  for pixel in row:
    if pixel == 1:
      print(fill, end='')
    else:
      print(empty, end=' ')
  print()