import copy

from units.interfaces import Unit, Ability, Clonable, Healable

class Archer(Unit, Ability, Clonable, Healable):
    def __init__(self):
        super().__init__(health=50, damage=30, armor=10, attack_range=5, dodge_chance=20, heal_percent=20)

    def attack(self, target):
        if isinstance(target, Unit) and self.is_in_range(target):
            target.take_damage(self.damage)

    def is_in_range(self, target):
        # Placeholder for range checking logic
        return True

    def heal(self):
        self.health *= self.health * self.heal_percent / 100

    def clone(self) -> Unit:
        return copy.deepcopy(self)

    def use_ability(self, target):
        # выстрел
        pass
