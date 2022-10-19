import typer

from apm2.commands.project.actions import InitialProject
from apm2.utils.data_types import TemplateLanguages
from apm2.utils.providers import BasicProvider

project_app = typer.Typer()
provider = BasicProvider()


@project_app.command('init')
def initialize_new_project(default: bool = typer.Option(False,
                                                        help="Create a new project with default template.",
                                                        prompt="Do you want to create a new project with "
                                                               "default template?"),
                           language: TemplateLanguages = typer.Option(TemplateLanguages.YAML,
                                                                      help='Language to generate all templates.',
                                                                      prompt='Ingress the language fot this project')):
    """
    Initialize a new empty project in the current path.

    """
    provider.set_command(InitialProject({"type": default, "prompt": typer.prompt, "language": language}))
    provider.execute_command()
    print('Project init successfully!')
