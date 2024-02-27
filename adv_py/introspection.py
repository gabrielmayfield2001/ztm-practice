class User: 

    def __init__(self, email):
        self.email = email
        print('init Completed')
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super.__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
print(dir(wizard1.email))

