import typer

from apm2.commands.project.actions import InitialProject
from apm2.utils.providers import BasicProvider

project_app = typer.Typer()
provider = BasicProvider()


@project_app.command('init')
def initialize_new_project(default: bool = typer.Option(False,
                                                        help="Create a new project with default template.",
                                                        prompt="Do you want to create a new project with "
                                                               "default template?")):
    """
    Initialize a new empty project in the current path.

    """
    provider.set_command(InitialProject({"type": default, "prompt": typer.prompt}))
    print('Project init successfully!')
