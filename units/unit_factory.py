from units.archer import Archer
from units.mage import Mage
from units.light_warrior import LightWarrior
from units.hard_warrior import HardWarrior
from units.doctor import Doctor
from units.walk_town import WalkTown
from units.walk_town_adapter import WalkTownAdapter

class UnitFactory:

    def create_unit(self, unit_type):
        if unit_type == 'archer':
            return Archer()
        elif unit_type == 'mage':
            return Mage()
        elif unit_type == 'light_warrior':
            return LightWarrior()
        elif unit_type == 'hard_warrior':
            return HardWarrior()
        elif unit_type == 'doctor':
            return Doctor()
        elif unit_type == 'walk_town':
            walk_town = WalkTown()
            return WalkTownAdapter(walk_town)
        else:
            raise ValueError(f"Unknown unit type: {unit_type}")

# Пример использования фабричного класса
if __name__ == "__main__":
    factory = UnitFactory()

    archer = factory.create_unit('archer')
    mage = factory.create_unit('mage')
    light_warrior = factory.create_unit('light_warrior')
    hard_warrior = factory.create_unit('hard_warrior')
    doctor = factory.create_unit('doctor')
    walk_town = factory.create_unit('walk_town')

    units = [archer, mage, light_warrior, hard_warrior, doctor, walk_town]
    for unit in units:
        print(f"{unit.__class__.__name__} created with health {unit.health}, damage {unit.damage}")
