# OOP


class PlayerCharacter:

    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age > 18:`fk`
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}!')
        return 'done'

    def run(self, hello):
        print(f'I can run fast and my name is {self.name}')

    @classmethod  # class method, can use without instantiating an object.
    def adding_things(cls, num1, num2):  # use cls instead of self
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('gabe', 23)
print(player1.name)
print(player1.age)
print(player1.shout())
print(player1.membership)
print(player1.run('hello'))
print(player1.adding_things(2, 3))
player3 = PlayerCharacter.adding_things(2, 3) # method on the actual class, doesn't need instantiation.
print(player3.age)
