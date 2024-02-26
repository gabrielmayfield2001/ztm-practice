# abstraction 


class PlayerCharacter:

    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age > 18:
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

player1.shout() 


player1.name = '11!' # without making these attributes private, then can be overriden NOT GOOD 
player1.shout = 'BBOOOOO'

print(player1.shout)