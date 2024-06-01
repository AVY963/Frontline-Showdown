from abc import ABC, abstractmethod


class Healable(ABC):
    @abstractmethod
    def heal(self):
        pass