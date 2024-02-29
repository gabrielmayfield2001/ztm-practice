# OOP

import random as rd

class PlayerCharacter:

    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0, level=1):
        self.name = name
        if age > 18:
            self.age = age  # attributes
        else:
            self.age = 0
        self.level = level

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

    def level_up(self):
        self.level += 1

    def shout(self):
        print(f'my name is {self.name} and my level is {self.level}!')
        return 'done'

    def run(self, hello):
        print(f'I can run fast and my name is {self.name}')

    def create_random_char(self):
        names = ['alice', 'bob', 'merlin', 'groot', 'robby']
        rand_name = rd.choice(names)
        rand_age =  rd.randint(1, 100)
        return rand_name, rand_age


    @classmethod  # class method, can use without instantiating an object.
    def adding_things(cls, num1, num2):  # use cls instead of self
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2
    
    @staticmethod
    def is_valid_age(age):
        if age >= 0 and age in range(0, 100):
            return True
        else:
            return False


class Wizard(PlayerCharacter):
    power_source = 'magic'

    def cast_spell(self):
        print('A spell is being cast!')

    def shout(self):
        print(f'My name is {self.name}, my level is {self.level}, and my power source is {self.power_source}!')


player1 = PlayerCharacter('gabe', 23, 5)
print(player1.level)
player1.level_up()
print(player1.level)
print(player1.is_adult())
player1.shout()

wiz1 = Wizard('oz', 64, 112)
wiz1.cast_spell()
wiz1.shout()

char = PlayerCharacter()
name, age = char.create_random_char()
print(f'Random character name: {name}, age: {age}')
print(char.is_valid_age(age))

