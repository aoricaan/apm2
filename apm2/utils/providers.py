from apm2.utils.abstracts import Command, CommandGroup


class BasicProvider(CommandGroup):
    _on_start = None

    def execute_command(self):
        if isinstance(self._on_start, Command):
            self._on_start.execute()

    def set_command(self, command: Command):
        self._on_start = command
