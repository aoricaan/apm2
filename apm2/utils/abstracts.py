from abc import ABC, abstractmethod


class Command(ABC):
    """
    The commamd interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self):
        pass


class CommandGroup(ABC):
    """
    The commamd interface declares a method for executing a command.
    """

    _on_start = None

    @abstractmethod
    def execute_command(self):
        pass

    @abstractmethod
    def set_command(self, a: Command):
        pass


class BaseCommand(Command):
    def __init__(self, payload):
        self._payload = payload
