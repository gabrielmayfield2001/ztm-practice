import random

class Adventurer():
    def __init__(self, age, health=100, inventory=None, name='anonymous', level=1):
        self.age = age if age >= 18 else 0
        self.health = health
        if inventory is None:
            self.inventory = []
        elif isinstance(inventory, list):
            self.inventory = inventory
        else:
            print('Inventory must be a list, creating empty list.')
            self.inventory = []
        self.name = name
        self.level = level

    @classmethod
    def create_thief(cls, age, name='Thief'):
        return cls(age=age, health=80, inventory=['dagger'], name=name, level=1)

    @staticmethod
    def is_valid_item(items):
        valid_items = ['armor', 'healing potion',
                       'boots', 'cape', 'sword', 'dagger']
        if all(each_item in valid_items for each_item in items):
            print('The items in inventory are valid')
        else:
            print('Those items are not valid')

    @staticmethod
    def trade_items(adventurer1, adventurer2, item1, item2):
        if item1 in adventurer1.inventory and item2 in adventurer2.inventory:
            adventurer1.remove_item(item1)
            adventurer2.remove_item(item2)
            adventurer1.add_item(item2)
            adventurer2.add_item(item1)
            print(f'Trade successful {adventurer1.name} traded {
                  item1} to {adventurer2.name} for {item2}')
        else:
            print('Trade failed, one or both items not in the respective inventories')
    
    @staticmethod
    def simulate_battle(adventurer1, adventurer2):
        while adventurer1.health and adventurer2.health > 0:
            action1 = random.choice(['heal', 'attack'])
            action2 = random.choice(['heal', 'attack'])

            if action1 == 'attack':
                dmg = random.randint(1, 20)
                adventurer2.take_damage(dmg)
            else:
                hp = random.randint(1, 20)
                adventurer1.heal(hp)
            
            if adventurer2.health <= 0: 
                break 

            if action2 == 'attack':
                dmg = random.randint(1, 20)
                adventurer1.take_damage(dmg)
            else:
                hp = random.randint(1, 20)
                adventurer2.heal(hp)
            
            if adventurer1.health <= 0:
                break 

        if adventurer1.health <=0:
            print(f'{adventurer2.name} wins the battle with {adventurer2.health} HP left!')
        else: 
            print(f'{adventurer1.name} wins the battle with {adventurer1.health} HP left!')
                  

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item not in self.inventory:
            print('Item not in inventory!')
        else:
            self.inventory.remove(item)

    def show_inventory(self):
        print('Your inventory is:', ', '.join(self.inventory))

    def heal(self, HP):
        if self.health + HP <= 100:
            self.health += HP
            print(f'{self.name} has healed for {HP} HP!')
        else:
            print('Healing can\'t exceed your health by 100!')

    def take_damage(self, dmg_taken):
        self.health -= dmg_taken
        print(f'{self.name} has taken {dmg_taken} HP of damage!')
        if self.health < 0:
            self.health = 0
            print('You are at minimum health!')


class Rogue(Adventurer):
    def __init__(self, age, health=100, inventory=None, name='anonymous', level=1, stealth_level=1):
        super().__init__(age, health, inventory, name, level)
        self.stealth_level = stealth_level

    def show_inventory(self):
        print(f'Stealth level is: {self.stealth_level}')
        return super().show_inventory()
    
    def stealth_attack(self):
        if self.stealth_level >= 10:
            dmg = 25
        else:
            dmg = 10
        return dmg

    def dodge(self):
        chance = random.randint(1, 5)
        if chance >= 3: 
            print('You dodged an attack')
        else:
            print('Failed to dodge an attack')



adv1 = Adventurer(18, 47, ['armor', 'healing potion'], 'Gabe', 24)
adv2 = Adventurer(25, 65, ['armor', 'healing potion', 'sword'], 'Adam', 37)

Adventurer.simulate_battle(adv1, adv2)


# adv1.show_inventory()
# adv2.show_inventory()
# adv1.trade_items(adv1, adv2, 'armor', 'healing potion')


# adv1.add_item('boots')
# adv1.add_item('cape')
# adv1.add_item('sword')
# adv1.show_inventory()
# adv1.is_valid_item(adv1.inventory)

# adv1.heal(100)
# adv1.take_damage(50)
# adv1.heal(25)


# rog1 = Rogue(18, 70, ['armor', 'dagger'], 'Aregorn', 5, 3)
# rog1.show_inventory()

# thief = Adventurer.create_thief(16, 'Glave')

# print(thief.name)
# print(thief.inventory)
