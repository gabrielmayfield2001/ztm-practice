
class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name  # attributes
        self._age = age # private when _ before attribute name 

    def speak(self):
        
        print(f'my name is {self._name}!')
        return 'done'

    def run(self):
        print(f'I can run fast and my name is {self._name} and I am {self._age} years old!')

player1 = PlayerCharacter(name = 'gabe', age = 23)
player1.run()


