import os
from pathlib import Path

import toml
from dotenv import load_dotenv

from apm2.models.configuration import config_from_dict, Config
from apm2.utils.abstracts import Command, CommandGroup
from apm2.utils.constants import BASE_CONFIGURATION


class BasicProvider(CommandGroup):
    _on_start = None

    def __init__(self):
        self.__load_config()

    def execute_command(self):
        if isinstance(self._on_start, Command):
            self._on_start.execute()

    def set_command(self, command: Command):
        self._on_start = command

    def __load_config(self, path="apm_project.toml"):
        config_path = Path(path)
        if not config_path.exists():
            load_dotenv(".env")
            app_name = os.getenv("app_name") or ""
            config_path.write_text(BASE_CONFIGURATION.format(app_name=app_name))
        toml_config = toml.loads(config_path.read_text())
        self.configuration: Config = config_from_dict(toml_config["apm"])
