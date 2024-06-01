class CommandManager:
    def __init__(self):
        self.history = []
        self.current_index = -1

    def execute_command(self, command):
        if self.current_index < len(self.history) - 1:
            self.history = self.history[:self.current_index + 1]
        command.do()
        self.history.append(command)
        self.current_index += 1

    def undo_last_command(self):
        if self.current_index >= 0:
            command = self.history[self.current_index]
            command.undo()
            self.current_index -= 1

    def redo_last_command(self):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            command = self.history[self.current_index]
            command.redo()
