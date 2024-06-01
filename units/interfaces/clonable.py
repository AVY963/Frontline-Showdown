from abc import ABC, abstractmethod

from units.interfaces import Unit


class Clonable(ABC):
    @abstractmethod
    def clone(self) -> Unit:
        pass

