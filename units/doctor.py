import copy

from units.interfaces import Unit, Clonable, Ability

class Doctor(Unit, Clonable, Ability):
    def __init__(self):
        super().__init__(health=50, damage=10, armor=5, attack_range=2, dodge_chance=15)

    def attack(self, target):
        # Healers have low attack damage
        if isinstance(target, Unit) and self.is_in_range(target):
            target.take_damage(self.damage)

    def heal(self, target):
        if isinstance(target, Unit) and self.is_in_range(target):
            target.health += 20  # Example healing amount

    def is_in_range(self, target):
        # Placeholder for range checking logic
        return True

    def clone(self) -> Unit:
        return copy.deepcopy(self)

