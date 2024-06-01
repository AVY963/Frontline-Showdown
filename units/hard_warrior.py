import copy

from units.interfaces import Unit, Clonable, Healable

class HardWarrior(Unit, Clonable, Healable):
    def __init__(self):
        super().__init__(health=100, damage=60, armor=40, attack_range=1, dodge_chance=5, heal_percent= 20)

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