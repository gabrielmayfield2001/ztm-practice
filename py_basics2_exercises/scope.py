def a():
  message = 'A'

  def b():
      nonlocal message
      message = 'B'

      def c():
          global message
          message = 'C'
          print("Inside c:", message)

      c()
      print("Inside b:", message)

  b()
  print("Inside a:", message)

a()
print("Outside:", message)