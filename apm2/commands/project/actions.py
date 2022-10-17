from cookiecutter.main import cookiecutter

from apm2.utils.abstracts import BaseCommand


class InitialProject(BaseCommand):
    def __init__(self, payload):
        super().__init__(payload)
        self._prompt = self._payload["prompt"]
        self._function = self.__default_project if self._payload["type"] else self.__custom_project

    def execute(self):
        self._function()

    def __default_project(self):
        self.__generate_templates("https://github.com/aoricaan/apm-template.git")

    def __custom_project(self):
        print('Remember the project will be compatible with cookiecutter.')
        template = self._prompt("path to template: ")
        self.__generate_templates(template)

    @staticmethod
    def __generate_templates(package):
        """
        Generates the templates for the project.
        """
        try:
            cookiecutter(template=package)
        except Exception as e:
            print(f"{e}")
