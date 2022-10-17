from importlib.metadata import version as v

import typer
from dotenv import load_dotenv

from apm2.commands.endpoints.commands import swagger_app
from apm2.commands.lambdas.commands import lambda_app
from apm2.commands.project.commands import project_app

load_dotenv()

app = typer.Typer()
app.add_typer(lambda_app, name='lambda')
app.add_typer(project_app, name='project')
app.add_typer(swagger_app, name='endpoint')


@app.callback(invoke_without_command=True)
def callback_version(version: bool = False):
    """
    Prints the version of the CLI.
    """
    if version:
        typer.echo(f'version: {v("apm2")}')
