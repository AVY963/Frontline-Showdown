from abc import ABC, abstractmethod

class Unit(ABC):
    def __init__(self, health, damage, armor, attack_range, dodge_chance, heal_percent):
        self.health = health
        self.damage = damage
        self.armor = armor
        self.attack_range = attack_range
        self.dodge_chance = dodge_chance
        self.heal_percent = heal_percent

    @abstractmethod
    def attack(self, target):
        pass

    def take_damage(self, damage):
        # Calculate damage after armor reduction

        reduced_damage = max(damage - self.armor, 0)
        print(self.__class__.__name__, "take_damage", reduced_damage)
        self.health -= reduced_damage

        return reduced_damage

    def is_alive(self):
        return self.health > 0
