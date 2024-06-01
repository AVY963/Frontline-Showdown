from abc import ABC, abstractmethod

class BattleStrategy(ABC):
    @abstractmethod
    def perform_action(self, unit, enemy_unit):
        pass

    @abstractmethod
    def reform_armies(self, army1, army2):
        pass

    @abstractmethod
    def handle_death(self, army, dead_unit):
        pass

class OneOnOneStrategy(BattleStrategy):
    def perform_action(self, unit, enemy_unit):
        if unit.is_alive() and enemy_unit.is_alive():
            unit.attack(enemy_unit)
            if enemy_unit.is_alive():
                enemy_unit.attack(unit)

    def reform_armies(self, army1, army2):
        pass

    def handle_death(self, army, dead_unit):
        pass

class SplitArmyStrategy(BattleStrategy):
    def perform_action(self, unit, enemy_unit):
        if unit.is_alive() and enemy_unit.is_alive():
            if unit.__class__.__name__ == 'Mage':
                unit.clone(enemy_unit)
            else:
                unit.attack(enemy_unit)
                if enemy_unit.is_alive():
                    enemy_unit.attack(unit)

    def reform_armies(self, army1, army2):
        # Split the army into two halves
        mid1 = len(army1) // 2
        mid2 = len(army2) // 2
        return (army1[:mid1], army2[:mid2]), (army1[mid1:], army2[mid2:])

    def handle_death(self, army, dead_unit):
        pass

class AllOutStrategy(BattleStrategy):
    def perform_action(self, unit, enemy_unit):
        if unit.is_alive() and enemy_unit.is_alive():
            unit.attack(enemy_unit)
        if enemy_unit.is_alive() and unit.is_alive():
            enemy_unit.attack(unit)

    def reform_armies(self, army1, army2):
        pass

    def handle_death(self, army, dead_unit):
        pass
