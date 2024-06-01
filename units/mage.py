
from units.interfaces import Unit, Healable, Ability


class Mage(Unit, Healable, Ability):
    def __init__(self):
        super().__init__(health=40, damage=10, armor=5, attack_range=3, dodge_chance=15, heal_percent=20)

    def attack(self, target):
        # Mages have low attack damage
        if isinstance(target, Unit) and self.is_in_range(target):
            target.take_damage(self.damage)

    def clone(self, target):
        # Clone logic here
        if isinstance(target, Unit) and not isinstance(target, Mage):
            # Placeholder for clone logic
            pass

    def use_ability(self, target):
        pass

    def heal(self):
        self.health *= self.health * self.heal_percent / 100
    def is_in_range(self, target):
        # Placeholder for range checking logic
        return True
