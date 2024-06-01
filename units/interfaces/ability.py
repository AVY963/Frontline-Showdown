from abc import ABC, abstractmethod

class Ability(ABC):
    @abstractmethod
    def use_ability(self, target):
        pass
