from units.unit_factory import UnitFactory
from logic.commands.command_manager import CommandManager
from logic.commands.command import GameTurnCommand, ChangeStrategyCommand
from logic.strategies.strategy import OneOnOneStrategy, SplitArmyStrategy, AllOutStrategy

class GameManager:
    def __init__(self):
        self.unit_factory = UnitFactory()
        self.army1 = []
        self.army2 = []
        self.command_manager = CommandManager()
        self.current_strategy = OneOnOneStrategy()

    def create_armies(self):
        for _ in range(5):
            row1 = [self.unit_factory.create_unit('archer') for _ in range(5)]
            row2 = [self.unit_factory.create_unit('mage') for _ in range(5)]
            self.army1.append(row1)
            self.army2.append(row2)

    def set_strategy(self, strategy):
        self.current_strategy = strategy

    def execute_turn(self):
        game_turn_command = GameTurnCommand(self.army1, self.army2, self.current_strategy)
        self.command_manager.execute_command(game_turn_command)

    def change_strategy(self, new_strategy):
        change_strategy_command = ChangeStrategyCommand(self, new_strategy)
        self.command_manager.execute_command(change_strategy_command)

    def undo_last_command(self):
        self.command_manager.undo_last_command()

    def redo_last_command(self):
        self.command_manager.redo_last_command()

    def show_units(self):
        print("Army 1:")
        for row in self.army1:
            for unit in row:
                print(f"{unit.__class__.__name__}: Health={unit.health}, Damage={unit.damage}")

        print("Army 2:")
        for row in self.army2:
            for unit in row:
                print(f"{unit.__class__.__name__}: Health={unit.health}, Damage={unit.damage}")

# Пример использования
if __name__ == "__main__":
    game_manager = GameManager()

    game_manager.create_armies()
    game_manager.show_units()

    # Пример выполнения хода
    game_manager.execute_turn()
    game_manager.show_units()

    # Пример отмены последнего хода
    game_manager.undo_last_command()
    game_manager.show_units()

    # Пример повторения последнего хода
    game_manager.redo_last_command()
    game_manager.show_units()

    # Смена стратегии и выполнение хода
    game_manager.change_strategy(SplitArmyStrategy())
    game_manager.execute_turn()
    game_manager.show_units()

    # Смена стратегии и выполнение хода
    game_manager.change_strategy(AllOutStrategy())
    game_manager.execute_turn()
    game_manager.show_units()
