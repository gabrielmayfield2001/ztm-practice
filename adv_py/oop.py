# OOP


class PlayerCharacter:

    # Class Object Attribute
    membership = True

    def __init__(self, name = 'anonymous', age = 0):
        if age > 18:
            self.name = name # attributes 
            self.age = age

    def shout(self):
        print(f'my name is {self.name}!')
        return 'done'

    def run(self, hello):
        print(f'I can run fast and my name is {self.name}')


player1 = PlayerCharacter('gabe', 23)

print(player1.name)
print(player1.age)
print(player1.shout())
print(player1.membership)
print(player1.run('hello'))
