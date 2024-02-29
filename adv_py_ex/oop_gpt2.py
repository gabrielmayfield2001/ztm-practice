class Adventurer():
    def __init__(self, age, health = 100, inventory = None, name = 'anonymous', level = 1):
        self.age = age if age >= 18 else 0
        self.health = health
        self.inventory = inventory
        self.name = name
        self.level = level 
    



