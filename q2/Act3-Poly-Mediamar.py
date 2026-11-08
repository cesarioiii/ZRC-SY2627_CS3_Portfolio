class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")

class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")

class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")


def perform_move(character):
    character.special_move()

class HealthPotion:
    def use(self):
        print("You regain 50 HP!")

class ManaPotion:
    def use(self):
        print("You restore 30 MP!")

class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")


def apply_item(item):
    item.use()

characters = [Warrior(), Mage(), Archer()]
for char in characters:
    perform_move(char)
print(" ")
potions = [HealthPotion(), ManaPotion(), SpeedBoost()]
for item in potions:
    apply_item(item)

# 1. They share the exact same method name and interface across different, 
#   unrelated classes, allowing them to be called interchangeably.
#
# 2. It allows different game entities like characters or items to execute 
#   their own unique actions through a single shared function/interface 
#   without needing explicit type checks or inheritance.
#
# 3. An attack() method where a Warrior does melee damage, a Mage inflicts 
#   magic damage, and an Archer deals ranged piercing damage.