from cookiecutter.main import cookiecutter

from apm2.utils.abstracts import BaseCommand
import logging

LOGGER = logging.getLogger("project_actions")


class InitialProject(BaseCommand):
    def __init__(self, payload):
        super().__init__(payload)
        LOGGER.debug("initializing initial project")
        self._prompt = self._payload["prompt"]
        self._language = self._payload["language"]
        self._function = self.__default_project if self._payload["type"] else self.__custom_project

    def execute(self):
        self._function()

    def __default_project(self):
        self.__generate_templates("https://github.com/aoricaan/apm-template", self._language)

    def __custom_project(self):
        LOGGER.info('Remember the project will be compatible with cookiecutter.')
        template = self._prompt("path to template: ")
        folder = self._prompt("specific folder?: ")
        args = (template, folder)
        self.__generate_templates(*args)

    @staticmethod
    def __generate_templates(package, directory=None):
        """
        Generates the templates for the project.
        """
        try:
            LOGGER.debug("building kwargs params.")
            kwargs = dict(template=package)
            if directory:
                kwargs.update(directory=directory)
            LOGGER.debug("building project.")
            cookiecutter(**kwargs)
        except Exception as e:
            LOGGER.error(f"{e}")
