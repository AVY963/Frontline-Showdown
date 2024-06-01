from units.interfaces.unit import Unit
from units.walk_town import WalkTown

class WalkTownAdapter(Unit):
    def __init__(self, walk_town: WalkTown):
        self.walk_town = walk_town
        super().__init__(walk_town.hp, walk_town.dmg, walk_town.defence, 0, 0, 0)

    def attack(self, target):
        # WaltTown does not attack
        pass

    def take_damage(self, damage):
        return self.walk_town.take_damage(damage)

    def is_alive(self):
        return self.walk_town.is_alive()
