
class WalkTown:
    def __init__(self):
        self.hp = 200
        self.dmg = 0
        self.defence = 50

    def take_damage(self, damage):
        # Calculate damage after armor reduction
        reduced_damage = max(damage - self.defence, 0)
        self.hp -= reduced_damage
        return reduced_damage

    def is_alive(self):
        return self.hp > 0
