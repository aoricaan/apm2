import os
from pathlib import Path

import toml
from dotenv import load_dotenv

from apm2.models.configuration import config_from_dict, Config
from apm2.utils.constants import BASE_CONFIGURATION


class Configuration:
    def __init__(self):
        self.__load_config()

    def __load_config(self, path="apm_project.toml"):
        config_path = Path(path)
        if not config_path.exists():
            load_dotenv(".env")
            app_name = os.getenv("app_name") or ""
            config_path.write_text(BASE_CONFIGURATION.format(app_name=app_name))
        toml_config = toml.loads(config_path.read_text())
        self.parameters: Config = config_from_dict(toml_config["apm"])
