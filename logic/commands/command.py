from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def do(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def redo(self):
        pass

class GameTurnCommand(Command):
    def __init__(self, army1, army2, strategy):
        self.army1 = army1
        self.army2 = army2
        self.strategy = strategy
        self.prev_state = self.save_state()

    def save_state(self):
        return [[(unit, unit.health) for unit in row] for row in self.army1 + self.army2]

    def restore_state(self, state):
        for i, row in enumerate(state[:len(self.army1)]):
            for j, (unit, health) in enumerate(row):
                self.army1[i][j].health = health
        for i, row in enumerate(state[len(self.army1):]):
            for j, (unit, health) in enumerate(row):
                self.army2[i][j].health = health

    def do(self):
        for row1, row2 in zip(self.army1, self.army2):
            for unit1, unit2 in zip(row1, row2):
                self.strategy.perform_action(unit1, unit2)

    def undo(self):
        self.restore_state(self.prev_state)

    def redo(self):
        self.do()

class ChangeStrategyCommand(Command):
    def __init__(self, game_manager, new_strategy):
        self.game_manager = game_manager
        self.new_strategy = new_strategy
        self.prev_strategy = game_manager.current_strategy

    def do(self):
        self.game_manager.set_strategy(self.new_strategy)

    def undo(self):
        self.game_manager.set_strategy(self.prev_strategy)

    def redo(self):
        self.do()
